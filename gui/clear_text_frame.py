import tkinter as tk

class ClearTextFrame:
    def __init__(self, root):
        self.frame = tk.Frame(root)
        self.frame.grid(row=4, column=0, columnspan=2, padx=(15,0), pady=(0, 5), sticky='nsew')

        self.var_clear_text = tk.BooleanVar()
        self.check_clear_text = tk.Checkbutton(self.frame, text="Clear Text Before Search", variable=self.var_clear_text)
        self.check_clear_text.grid(row=0, column=0, columnspan=2, pady=(0, 5), sticky='nsew')
