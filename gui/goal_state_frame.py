import tkinter as tk

class GoalStateFrame:
    def __init__(self, root):
        self.frame = tk.Frame(root)
        self.frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='w')

        self.label_goal_state = tk.Label(self.frame, text="Enter Goal State (Jug A, Jug B):", anchor="w")
        self.label_goal_state.grid(row=0, column=0, padx=(10, 5), pady=10, sticky='w')

        self.entry_goal_a = tk.Entry(self.frame)
        self.entry_goal_b = tk.Entry(self.frame)

        self.entry_goal_a.grid(row=0, column=1, padx=5, pady=10, sticky='w')
        self.entry_goal_b.grid(row=0, column=2, padx=(5, 10), pady=10, sticky='w')

    def get_goal_state(self):
        return int(self.entry_goal_a.get()), int(self.entry_goal_b.get())
