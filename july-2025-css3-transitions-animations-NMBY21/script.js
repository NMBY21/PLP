// Part 2: Functions with scope, parameters & return values

// Global variable
let animationCount = 0;

// Function with parameters & return value
function calculateScale(base, factor) {
  return base * factor;
}

// Function demonstrating local scope
function logAnimation() {
  let localMsg = "Animation triggered!";
  console.log(localMsg);
  animationCount++;
  console.log("Total animations: " + animationCount);
}

// Part 3: Triggering animations with JavaScript

// Animate Box
const box = document.getElementById("animatedBox");
document.getElementById("magicBtn").addEventListener("click", () => {
  box.classList.toggle("animate");

  // Use function logic
  const newSize = calculateScale(100, 1.5);
  console.log("New box size should be: " + newSize + "px");
  logAnimation();
});

// Card Flip
const card = document.getElementById("flipCard");
card.addEventListener("click", () => {
  card.classList.toggle("flipped");
  logAnimation();
});

// Modal Popup
const modal = document.getElementById("modal");
const openModal = document.getElementById("openModal");
const closeModal = document.getElementById("closeModal");

openModal.addEventListener("click", () => {
  modal.style.display = "flex";
  logAnimation();
});

closeModal.addEventListener("click", () => {
  modal.style.display = "none";
});
