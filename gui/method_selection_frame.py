import tkinter as tk

class MethodSelectionFrame:
    def __init__(self, root):
        self.frame = tk.Frame(root)
        self.frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='w')

        self.label_method = tk.Label(self.frame, text="Select Method:", anchor="w")
        self.label_method.grid(row=0, column=0, padx=(10, 5), pady=10, sticky='w')

        self.var_method = tk.StringVar()
        self.var_method.set("BFS")

        methods = ["BFS", "DFS", "UCS"]
        for i, method in enumerate(methods):
            tk.Radiobutton(self.frame, text=method, variable=self.var_method, value=method).grid(row=0, column=i + 1, padx=(2, 2), pady=10, sticky='w')

    def get_selected_method(self):
        return self.var_method.get()
