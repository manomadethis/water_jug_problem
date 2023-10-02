import tkinter as tk

class CopyDeleteFrame:
    def __init__(self, root, copy_callback, delete_callback):
        self.frame = tk.Frame(root)
        self.frame.grid(row=5, column=0, columnspan=2, pady=10, sticky='nsew')

        self.button_copy = tk.Button(self.frame, text="Copy", command=copy_callback)
        self.button_copy.grid(row=0, column=0, padx=(20,10), pady=10, sticky='nsew')

        self.button_delete = tk.Button(self.frame, text="Delete", command=delete_callback)
        self.button_delete.grid(row=0, column=1, pady=10, sticky='nsew')
