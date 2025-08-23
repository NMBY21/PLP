// Part 1: JavaScript Basics

// Variables, conditionals, input/output
document.getElementById("checkAgeBtn").addEventListener("click", function () {
  let age = parseInt(document.getElementById("ageInput").value);

  if (age >= 18) {
    document.getElementById("ageResult").textContent =
      "✅ You are eligible to vote!";
  } else {
    document.getElementById("ageResult").textContent =
      "❌ You are not eligible to vote.";
  }
});

// Part 2: Functions
// Function 1: Sum calculator
function calculateSum(a, b) {
  return a + b;
}

// Function 2: Format string
function formatGreeting(name) {
  return `Hello, ${name}! Welcome 🎉`;
}

// Event listener using custom function
document.getElementById("calcBtn").addEventListener("click", function () {
  let num1 = parseFloat(document.getElementById("num1").value);
  let num2 = parseFloat(document.getElementById("num2").value);

  let result = calculateSum(num1, num2);
  document.getElementById("sumResult").textContent = "Sum: " + result;
  console.log(formatGreeting("Student")); // Example function call
});

// Part 3: Loops
document.getElementById("loopBtn").addEventListener("click", function () {
  let list = document.getElementById("countdownList");
  list.innerHTML = ""; // clear before regenerating

  // Example loop: countdown from 5
  for (let i = 5; i >= 1; i--) {
    let li = document.createElement("li");
    li.textContent = i;
    list.appendChild(li);
  }

  // Example while loop (console only)
  let counter = 1;
  while (counter <= 3) {
    console.log("While Loop Counter:", counter);
    counter++;
  }
});

// Part 4: DOM Manipulation
document
  .getElementById("changeColorBtn")
  .addEventListener("click", function () {
    document.body.classList.toggle("highlight");
  });

document.getElementById("addItemBtn").addEventListener("click", function () {
  let ul = document.getElementById("itemList");
  let li = document.createElement("li");
  li.textContent = "New Item " + (ul.children.length + 1);
  ul.appendChild(li);
});

// Extra DOM styling toggle via CSS
document.body.classList.add("default");
