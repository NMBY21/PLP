import tkinter as tk
from math import sin, cos, tan, sqrt, log, pi, e

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Python Calculator")
        self.root.configure(bg="#f3f4f6")
        self.expression = ""
        self.last_was_equal = False

        self.display = tk.Entry(root, font=("Segoe UI", 22), bd=0, relief="flat",
                                bg="#e5e7eb", fg="#111827", justify='right')
        self.display.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=20, pady=10, sticky="nsew")

        buttons = [
            ["AC", "⌫", "(", ")", "/"],
            ["7", "8", "9", "*", "sqrt"],
            ["4", "5", "6", "-", "log"],
            ["1", "2", "3", "+", "sin"],
            ["0", ".", "π", "e", "="]
        ]

        for i, row in enumerate(buttons):
            for j, btn in enumerate(row):
                self.create_button(btn, i + 1, j)

        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(5):
            self.root.grid_columnconfigure(j, weight=1)

    def create_button(self, text, row, col):
        bg = "#f9fafb" if text not in {"=", "AC", "⌫"} else "#d1d5db"
        fg = "#111827"

        b = tk.Button(self.root, text=text, font=("Segoe UI", 16), bg=bg, fg=fg,
                      relief="flat", activebackground="#e5e7eb", activeforeground=fg,
                      command=lambda: self.click(text))
        b.grid(row=row, column=col, sticky="nsew", padx=2, pady=2, ipadx=10, ipady=10)

    import tkinter as tk
from math import sin, cos, tan, sqrt, log, pi, e

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Python Calculator")
        self.root.configure(bg="#f3f4f6")
        self.expression = ""
        self.last_was_equal = False

        self.display = tk.Entry(root, font=("Segoe UI", 22), bd=0, relief="flat",
                                bg="#e5e7eb", fg="#111827", justify='right')
        self.display.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=20, pady=10, sticky="nsew")

        buttons = [
            ["AC", "⌫", "(", ")", "/"],
            ["7", "8", "9", "*", "sqrt"],
            ["4", "5", "6", "-", "log"],
            ["1", "2", "3", "+", "sin"],
            ["0", ".", "π", "e", "="]
        ]

        for i, row in enumerate(buttons):
            for j, btn in enumerate(row):
                self.create_button(btn, i + 1, j)

        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(5):
            self.root.grid_columnconfigure(j, weight=1)

    def create_button(self, text, row, col):
        bg = "#f9fafb" if text not in {"=", "AC", "⌫"} else "#d1d5db"
        fg = "#111827"

        b = tk.Button(self.root, text=text, font=("Segoe UI", 16), bg=bg, fg=fg,
                      relief="flat", activebackground="#e5e7eb", activeforeground=fg,
                      command=lambda: self.click(text))
        b.grid(row=row, column=col, sticky="nsew", padx=2, pady=2, ipadx=10, ipady=10)

    def click(self, key):
        if self.expression == "Error":
            self.expression = ""

        if key == "=":
            try:
                result = eval(self.expression, {
                    "sin": sin,
                    "cos": cos,
                    "tan": tan,
                    "sqrt": sqrt,
                    "log": log,
                    "pi": pi,
                    "e": e
                })
                self.expression = str(result)
                self.last_was_equal = True
            except Exception:
                self.expression = "Error"
                self.last_was_equal = False
        elif key == "AC":
            self.expression = ""
            self.last_was_equal = False
        elif key == "⌫":
            self.expression = self.expression[:-1]
            self.last_was_equal = False
        elif key == "π":
            if self.last_was_equal:
                self.expression = "pi"
            else:
                self.expression += "pi"
            self.last_was_equal = False
        elif key == "e":
            if self.last_was_equal:
                self.expression = "e"
            else:
                self.expression += "e"
            self.last_was_equal = False
        else:
            if self.last_was_equal and key not in "+-*/":
                self.expression = str(key)
            else:
                self.expression += str(key)
            self.last_was_equal = False

        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.minsize(400, 500)
    root.mainloop()


    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.minsize(400, 500)
    root.mainloop()
