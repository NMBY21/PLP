// Part 1: Event Handling
document.getElementById("clickMeBtn").addEventListener("click", function() {
  document.getElementById("clickResult").textContent = "✅ Button clicked!";
});

// Part 2: Interactive Elements
// Light/Dark Mode Toggle
document.getElementById("modeToggleBtn").addEventListener("click", function() {
  document.body.classList.toggle("dark-mode");
});

// Counter
let counter = 0;
const counterValue = document.getElementById("counterValue");

document.getElementById("incrementBtn").addEventListener("click", function() {
  counter++;
  counterValue.textContent = counter;
});

document.getElementById("decrementBtn").addEventListener("click", function() {
  counter--;
  counterValue.textContent = counter;
});

// Collapsible FAQ
const questions = document.querySelectorAll(".faq-question");
questions.forEach(q => {
  q.addEventListener("click", () => {
    const answer = q.nextElementSibling;
    answer.style.display = answer.style.display === "block" ? "none" : "block";
  });
});

// Part 3: Form Validation
document.getElementById("signupForm").addEventListener("submit", function(event) {
  event.preventDefault(); // prevent default form submission

  let isValid = true;

  // Name validation
  const name = document.getElementById("name").value.trim();
  if (name.length < 3) {
    isValid = false;
    document.getElementById("nameError").textContent = "Name must be at least 3 characters.";
  } else {
    document.getElementById("nameError").textContent = "";
  }

  // Email validation
  const email = document.getElementById("email").value.trim();
  const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
  if (!emailPattern.test(email)) {
    isValid = false;
    document.getElementById("emailError").textContent = "Please enter a valid email.";
  } else {
    document.getElementById("emailError").textContent = "";
  }

  // Password validation
  const password = document.getElementById("password").value.trim();
  if (password.length < 6) {
    isValid = false;
    document.getElementById("passwordError").textContent = "Password must be at least 6 characters.";
  } else {
    document.getElementById("passwordError").textContent = "";
  }

  // Success feedback
  if (isValid) {
    document.getElementById("formSuccess").textContent = "✅ Form submitted successfully!";
    document.getElementById("signupForm").reset();
  } else {
    document.getElementById("formSuccess").textContent = "";
  }
});
