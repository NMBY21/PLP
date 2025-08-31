# 🍲 Recipe Recommender (Food Matcher)

Simple full‑stack app: users enter ingredients, backend asks an AI model for 3 quick recipes, stores results in MySQL, and shows them as clickable cards.

## Stack
- Frontend: HTML5, CSS (recipe cards), JavaScript (filtering + fetch)
- Backend: Python (Flask), CORS, OpenAI API
- Database: MySQL (tables: `users`, `recipes`, `user_recipes`)

## Features
- Enter ingredients (e.g., "chicken, rice").
- Generate 3 simple recipes via OpenAI.
- Save results to MySQL and display as cards.
- Mark favorites per user (demo uses a mock user id).
- Basic filtering on the client.

## 🗂 Project Structure
```
frontend/
  index.html
  styles.css
  main.js
backend/
  app.py
  requirements.txt
  .env.example
db/
  schema.sql
```

## 🚀 Quick Start (Dev)
### 1) Database (MySQL)
Create a database (e.g., `recipes_db`) and run the schema:
```bash
mysql -u root -p < db/schema.sql
```
Or copy/paste the SQL into your MySQL client.

### 2) Backend
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate ; macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# edit .env with your credentials + OpenAI key
python app.py
```
Backend will start at `http://localhost:5000` by default.

### 3) Frontend
Open `frontend/index.html` in your browser (it calls the Flask API at `http://localhost:5000`).

> If the browser blocks CORS or mixed content, run a simple static server:
```bash
# from the project root
python -m http.server 8080
# then open http://localhost:8080/frontend/
```

## 🔐 Environment Variables
Create `backend/.env`:
```
OPENAI_API_KEY=sk-...
DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=recipes_db
# Optional
PORT=5000
OPENAI_MODEL=gpt-4o-mini
```
> If `OPENAI_API_KEY` is missing, the backend replies with **dummy recipes** so you can still demo.

## 📦 API
### POST /api/recipes
Request JSON:
```json
{"ingredients": "chicken, rice", "user_id": 1}
```
Response JSON:
```json
{"recipes":[{"id":123,"title":"...", "ingredients":"...", "steps":"..."}]}
```

### POST /api/favorites
```json
{"user_id":1, "recipe_id":123}
```

### GET /api/favorites?user_id=1
Returns the user's saved recipes.

## 🧪 Judging Checklist Mapping
- **Problem Clarity**: Reduces meal decision friction; uses available ingredients.
- **Solution Quality**: Working prototype, persistent history, favorites.
- **Market Insight**: Universal need (home cooking, food waste reduction).
- **Creativity/Design**: Card UI + client filtering.
- **Code Quality & Efficiency**: Clear routes, parameterized queries, on-demand API calls.
- **Security & Fault Tolerance**: .env secrets, input validation, try/except, DB reconnects.
- **Performance**: Lightweight routes; single AI hit per query.
- **Dev Process / Docs**: This README + schema + clear setup.
- **Documentation & Testing**: Docstrings, simple curl examples; easy to extend tests.

## 🧭 Next Ideas (Optional)
- Auth (JWT) + real user accounts.
- Cache generated recipes per ingredient set to save tokens.
- Tags/diet filters (vegan, halal, gluten-free).
- Export to PDF or share links.
- Add images by querying a free image API (optional).

---

Made for hackathon speed: clear, small, yet impressive.
