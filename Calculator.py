import math

class Calculator:
    def __init__(self):
        self.memory = 0

    def evaluate(self, expression):
        try:
            # Secure evaluation context
            allowed_names = {
                k: v for k, v in math.__dict__.items() if not k.startswith("__")
            }
            allowed_names.update({
                "abs": abs,
                "round": round
            })
            result = eval(expression, {"__builtins__": {}}, allowed_names)
            return result
        except ZeroDivisionError:
            return "❌ Cannot divide by zero."
        except Exception as e:
            return f"❌ Invalid expression: {e}"

    def memory_add(self, value):
        self.memory += value

    def memory_subtract(self, value):
        self.memory -= value

    def memory_recall(self):
        return self.memory

    def memory_clear(self):
        self.memory = 0

def show_menu():
    print("""
========= PYTHON CALCULATOR =========
Supported operations:
- Basic: +, -, *, /, %, **
- Functions: sin(x), cos(x), tan(x), log(x), sqrt(x), abs(x), round(x)
- Memory: M+ (add), M- (subtract), MR (recall), MC (clear)
- Use math constants like pi, e
- Example: sin(pi/2) + log(10) * sqrt(4)

Commands:
  exit  → Quit calculator
======================================
""")

def main():
    calc = Calculator()
    show_menu()

    while True:
        user_input = input(">>> ")

        if user_input.lower() == "exit":
            break
        elif user_input == "M+":
            val = float(input("Value to add to memory: "))
            calc.memory_add(val)
            print("✅ Added to memory.")
        elif user_input == "M-":
            val = float(input("Value to subtract from memory: "))
            calc.memory_subtract(val)
            print("✅ Subtracted from memory.")
        elif user_input == "MR":
            print("🧠 Memory =", calc.memory_recall())
        elif user_input == "MC":
            calc.memory_clear()
            print("🧹 Memory cleared.")
        else:
            result = calc.evaluate(user_input)
            print("🧮 Result =", result)

if __name__ == "__main__":
    main()
