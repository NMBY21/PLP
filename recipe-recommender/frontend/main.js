const API_BASE = "http://localhost:5000/api";
const USER_ID = 1; // demo user

function el(tag, attrs={}, ...children){
  const e = document.createElement(tag);
  Object.entries(attrs).forEach(([k,v]) => {
    if (k === "class") e.className = v;
    else if (k.startsWith("on") && typeof v === "function") e.addEventListener(k.slice(2), v);
    else e.setAttribute(k, v);
  });
  for (const c of children) {
    if (typeof c === "string") e.appendChild(document.createTextNode(c));
    else if (c) e.appendChild(c);
  }
  return e;
}

function card(recipe, favoriteBtn=true){
  const c = el("div", {class:"card"});
  c.appendChild(el("h3", {}, recipe.title || "Untitled"));
  if (recipe.ingredients) c.appendChild(el("p", {}, "Ingredients: " + recipe.ingredients));
  if (recipe.steps) c.appendChild(el("p", {}, recipe.steps));
  const actions = el("div", {class:"actions"});
  const copyBtn = el("button", {class:"ghost", onclick: async () => {
    const text = `${recipe.title}\nIngredients: ${recipe.ingredients}\nSteps: ${recipe.steps}`;
    await navigator.clipboard.writeText(text);
    copyBtn.textContent = "Copied!";
    setTimeout(()=>copyBtn.textContent="Copy", 1500);
  }}, "Copy");
  actions.appendChild(copyBtn);

  if (favoriteBtn && recipe.id){
    const favBtn = el("button", {onclick: async () => {
      await fetch(`${API_BASE}/favorites`, {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({user_id: USER_ID, recipe_id: recipe.id})
      });
      loadFavorites();
    }}, "Save");
    actions.appendChild(favBtn);
  }
  c.appendChild(actions);
  return c;
}

async function generate(){
  const ingredients = document.getElementById("ingredients").value.trim();
  if (!ingredients) return alert("Please enter ingredients");
  const res = await fetch(`${API_BASE}/recipes`, {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({ingredients, user_id: USER_ID})
  });
  const data = await res.json();
  const results = document.getElementById("results");
  results.innerHTML = "";
  (data.recipes || []).forEach(r => results.appendChild(card(r)));
}

async function loadFavorites(){
  const res = await fetch(`${API_BASE}/favorites?user_id=${USER_ID}`);
  const data = await res.json();
  const fav = document.getElementById("favorites");
  fav.innerHTML = "";
  (data.recipes || []).forEach(r => fav.appendChild(card(r, false)));
}

document.getElementById("generate").addEventListener("click", generate);

document.getElementById("filter").addEventListener("input", (e)=>{
  const q = e.target.value.toLowerCase();
  document.querySelectorAll("#results .card").forEach(card => {
    const text = card.textContent.toLowerCase();
    card.style.display = text.includes(q) ? "" : "none";
  });
});

// initial favorites
loadFavorites();
