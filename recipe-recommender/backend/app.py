import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error
from datetime import datetime

# OpenAI (new SDK)
try:
    from openai import OpenAI
except Exception:
    OpenAI = None  # allow running without the package for read-only review

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "127.0.0.1"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "recipes_db"),
    "autocommit": True,
    "charset": "utf8mb4",
}

app = Flask(__name__)
CORS(app)


def get_db():
    return mysql.connector.connect(**DB_CONFIG)


def ensure_tables():
    sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(190) UNIQUE,
        password VARCHAR(200),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE IF NOT EXISTS recipes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(190) NOT NULL,
        ingredients TEXT,
        steps TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE IF NOT EXISTS user_recipes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        recipe_id INT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE KEY uq_user_recipe (user_id, recipe_id),
        CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        CONSTRAINT fk_recipe FOREIGN KEY (recipe_id) REFERENCES recipes(id) ON DELETE CASCADE
    );
    """
    conn = get_db()
    cur = conn.cursor()
    for stmt in [s.strip() for s in sql.split(";") if s.strip()]:
        cur.execute(stmt)
    cur.close()
    conn.close()


ensure_tables()


def parse_recipes_from_ai(text: str):
    """
    Expect the model to return JSON with a 'recipes' array; but be resilient:
    try to parse JSON; fallback to splitting lines into pseudo recipes.
    """
    try:
        data = json.loads(text)
        if isinstance(data, dict) and "recipes" in data:
            return data["recipes"]
        elif isinstance(data, list):
            return data
    except Exception:
        pass

    # Fallback: naive split into up to 3 recipes
    lines = [l.strip("- • ").strip() for l in text.split("\n") if l.strip()]
    out = []
    for i, chunk in enumerate(lines[:3]):
        out.append({
            "title": f"Recipe {i+1}",
            "ingredients": "Based on: " + chunk,
            "steps": chunk
        })
    return out


def ai_generate_recipes(ingredients: str):
    # If no key or library missing, return dummy recipes for demo
    if not OPENAI_API_KEY or OpenAI is None:
        return [
            {
                "title": "Quick Garlic Chicken Rice",
                "ingredients": "chicken, rice, garlic, oil, salt, pepper",
                "steps": "Sauté garlic, add chicken cubes, season, add cooked rice, toss 3–4 min."
            },
            {
                "title": "Herbed One-Pot Chicken & Rice",
                "ingredients": "chicken, rice, onion, stock, mixed herbs",
                "steps": "Brown onion and chicken; add rice + stock; simmer 15–18 min covered."
            },
            {
                "title": "Spicy Chicken Rice Stir-Fry",
                "ingredients": "chicken, rice, chili, soy, scallion",
                "steps": "Stir-fry chicken; add day-old rice, chili, soy; finish with scallions."
            },
        ]

    client = OpenAI(api_key=OPENAI_API_KEY)
    system = (
        "You are a cooking assistant. Return STRICT JSON only. "
        "Schema: {\"recipes\":[{\"title\":\"string\",\"ingredients\":\"comma list\",\"steps\":\"short steps\"}]} "
        "Use everyday ingredients available in Africa. 3 recipes max. Keep steps under 40 words each."
    )
    user = f"Ingredients: {ingredients}. Generate 3 simple recipes."
    try:
        resp = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[{"role": "system", "content": system},
                      {"role": "user", "content": user}],
            temperature=0.4,
            max_tokens=450,
        )
        content = resp.choices[0].message.content
        return parse_recipes_from_ai(content)
    except Exception as e:
        # graceful fallback
        return [
            {
                "title": "Pan Chicken with Rice",
                "ingredients": ingredients,
                "steps": f"Error calling AI; fallback. Cook chicken; add cooked rice; season. ({e})"
            }
        ]


def upsert_recipe(conn, title: str, ingredients: str, steps: str):
    cur = conn.cursor()
    # try to find existing by title+steps hash-ish
    qry = "SELECT id FROM recipes WHERE title=%s AND steps=%s LIMIT 1"
    cur.execute(qry, (title, steps))
    row = cur.fetchone()
    if row:
        rid = row[0]
    else:
        ins = "INSERT INTO recipes (title, ingredients, steps) VALUES (%s, %s, %s)"
        cur.execute(ins, (title, ingredients, steps))
        rid = cur.lastrowid
    cur.close()
    return rid


@app.route("/api/health")
def health():
    return jsonify(ok=True, time=datetime.utcnow().isoformat() + "Z")


@app.route("/api/recipes", methods=["POST"])
def generate_recipes():
    data = request.get_json(silent=True) or {}
    ingredients = (data.get("ingredients") or "").strip()
    user_id = data.get("user_id", 1)  # demo default user
    if not ingredients:
        return jsonify(error="ingredients_required"), 400

    recipes = ai_generate_recipes(ingredients)

    try:
        conn = get_db()
        # ensure demo user exists
        cur = conn.cursor()
        cur.execute("INSERT IGNORE INTO users (id, name, email, password) VALUES (1,'Demo','demo@example.com','x')")
        conn.commit()
        cur.close()

        # store recipes
        saved = []
        for r in recipes:
            rid = upsert_recipe(conn, r.get("title","Untitled")[:190], r.get("ingredients",""), r.get("steps",""))
            saved.append({"id": rid, **r})
        conn.close()
    except Error as e:
        return jsonify(error="db_error", details=str(e), recipes=recipes), 200  # still return recipes for demo

    return jsonify(recipes=saved), 200


@app.route("/api/favorites", methods=["POST"])
def add_favorite():
    data = request.get_json(silent=True) or {}
    user_id = data.get("user_id")
    recipe_id = data.get("recipe_id")
    if not user_id or not recipe_id:
        return jsonify(error="user_id_and_recipe_id_required"), 400

    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT IGNORE INTO user_recipes (user_id, recipe_id) VALUES (%s, %s)", (user_id, recipe_id))
        conn.commit()
        cur.close()
        conn.close()
    except Error as e:
        return jsonify(error="db_error", details=str(e)), 500

    return jsonify(ok=True)


@app.route("/api/favorites", methods=["GET"])
def list_favorites():
    user_id = request.args.get("user_id", type=int, default=1)
    try:
        conn = get_db()
        cur = conn.cursor(dictionary=True)
        cur.execute("""
            SELECT r.id, r.title, r.ingredients, r.steps, ur.created_at AS saved_at
            FROM user_recipes ur
            JOIN recipes r ON r.id = ur.recipe_id
            WHERE ur.user_id = %s
            ORDER BY ur.created_at DESC
        """, (user_id,))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(recipes=rows)
    except Error as e:
        return jsonify(error="db_error", details=str(e)), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
