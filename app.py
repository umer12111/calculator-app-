import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")

        self.current_input = ""
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Display field
        self.result_label = tk.Label(self.root, textvariable=self.result_var, height=2, anchor="e", padx=10, font=('Arial', 24), bg="lightgray")
        self.result_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

        # Clear button
        self.clear_button = tk.Button(self.root, text="C", height=2, font=('Arial', 18), command=self.clear_input)
        self.clear_button.grid(row=5, column=0, columnspan=4, sticky="nsew")

    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, height=2, width=5, font=('Arial', 18), command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, sticky="nsew")

    def on_button_click(self, text):
        if text == "=":
            try:
                # Evaluate the expression and update the result
                self.current_input = str(eval(self.current_input))
            except Exception as e:
                self.current_input = "Error"
        else:
            self.current_input += text
        self.result_var.set(self.current_input)

    def clear_input(self):
        self.current_input = ""
        self.result_var.set("")

# Main part to run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
