import tkinter as tk

class OutputFrame:
    def __init__(self, root):
        self.frame = tk.Frame(root)
        self.frame.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

        self.text_output = tk.Text(self.frame, height=15, width=50, wrap=tk.WORD)
        self.text_output.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

        self.scrollbar = tk.Scrollbar(self.frame, command=self.text_output.yview)
        self.scrollbar.grid(row=0, column=2, sticky='nsew')
        self.text_output['yscrollcommand'] = self.scrollbar.set
