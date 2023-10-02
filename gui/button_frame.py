import tkinter as tk

class ButtonFrame:
    def __init__(self, root, solve_callback, explanation_callback):
        self.frame = tk.Frame(root)
        self.frame.grid(row=2, column=0, columnspan=3, pady=(20, 10), sticky='nsew')

        self.button_solve = tk.Button(self.frame, text="Solve", command=solve_callback)
        self.button_solve.grid(row=0, column=0, padx=(20, 10), pady=10, sticky='nsew')

        self.button_explanation = tk.Button(self.frame, text="Explanation", command=explanation_callback)
        self.button_explanation.grid(row=0, column=1, pady=10, sticky='nsew')
