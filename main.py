import tkinter as tk
from tkinter import messagebox
import sys
from bfs import water_jugs_bfs
from dfs import water_jugs_dfs

from gui.goal_state_frame import GoalStateFrame
from gui.method_selection_frame import MethodSelectionFrame
from gui.button_frame import ButtonFrame
from gui.output_frame import OutputFrame
from gui.clear_text_frame import ClearTextFrame
from gui.copy_delete_frame import CopyDeleteFrame
from gui.text_redirector import TextRedirector
from ucs import water_jugs_ucs

class WaterJugSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Water Jug Problem Solver")

        # Goal state entry
        self.goal_state_frame = GoalStateFrame(root)

        # Method selection
        self.method_selection_frame = MethodSelectionFrame(root)

        # Solve and Explanation buttons
        self.button_frame = ButtonFrame(root, self.solve, self.show_explanation)

        # Output text widget
        self.output_frame = OutputFrame(root)

        # Clear Text Checkbox
        self.clear_text_frame = ClearTextFrame(root)

        # Copy and Delete buttons
        self.copy_delete_frame = CopyDeleteFrame(root, self.copy_text, self.delete_text)

        # Make the window resizable and center it
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(4, weight=1)

        self.center_window()

    def solve(self):
        if self.clear_text_frame.var_clear_text.get():
            self.output_frame.text_output.delete(1.0, tk.END)

        try:
            goal_state = self.goal_state_frame.get_goal_state()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integer values for the goal state.")
            return

        method = self.method_selection_frame.get_selected_method()

        # Redirect stdout to the Text widget
        original_stdout = sys.stdout
        sys.stdout = TextRedirector(self.output_frame.text_output)

        if method == "BFS":
            water_jugs_bfs(goal_state)
        elif method == "DFS":
            water_jugs_dfs(goal_state)
        elif method == "UCS":
            water_jugs_ucs(goal_state)
        else:
            messagebox.showerror("Error", "Invalid method selected.")

        # Restore stdout
        sys.stdout = original_stdout

    def show_explanation(self):
        explanation = """
        This GUI allows you to solve the water jug problem using various search methods:

        1. BFS (Breadth-First Search): Explores all the neighbor nodes at the present depth before moving on to nodes at the next depth. In the context of the water jug problem, each state represents the current water levels in Jug A and Jug B. The algorithm starts with the initial state (0, 0) and explores all possible operations to reach the goal state specified by the user.The operations include filling Jug A, filling Jug B, pouring water from Jug A to Jug B, pouring water from Jug B to Jug A, emptying Jug A, and emptying Jug B. The algorithm continues this process until it finds a state that matches the user-defined goal state. The path taken to reach the goal state and the nodes expanded during the search are printed for reference.

        2. DFS (Depth-First Search): Explores as far as possible along one branch before backtracking. In the water jug problem, it starts with the initial state (0, 0) and explores the operations to reach the goal state. Unlike BFS, DFS goes as deep as possible before exploring other branches. The operations include filling Jug A, filling Jug B, pouring water from Jug A to Jug B, pouring water from Jug B to Jug A, emptying Jug A, and emptying Jug B. The algorithm backtracks when it reaches a dead-end, exploring other possibilities. The path taken to reach the goal state and the nodes visited during the search are printed for reference.

        3. UCS (Uniform-Cost Search): Explores nodes with the lowest cost first, where the cost is determined by the weights assigned to each state. In the water jug problem, the weight represents the cost associated with reaching a certain state. The operations include filling Jug A, filling Jug B, pouring water from Jug A to Jug B, pouring water from Jug B to Jug A, emptying Jug A, and emptying Jug B. The algorithm prioritizes states with lower weights, ensuring that it explores the most cost-effective paths first. The path taken to reach the goal state and the nodes expanded during the search are printed for reference.
        """
        messagebox.showinfo("Explanation", explanation)

    def copy_text(self):
        text_to_copy = self.output_frame.text_output.get(1.0, tk.END)
        self.root.clipboard_clear()
        self.root.clipboard_append(text_to_copy)
        self.root.update()  # required on macOS
        messagebox.showinfo("Copy Successful", "Text has been copied to the clipboard.")

    def delete_text(self):
        self.output_frame.text_output.delete(1.0, tk.END)

    def center_window(self):
        w = 600  # width for the window
        h = 700  # height for the window

        # get screen width and height
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()

        # calculate x and y coordinates for the window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        # set the dimensions of the screen and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))


if __name__ == "__main__":
    root = tk.Tk()
    app = WaterJugSolverGUI(root)
    root.mainloop()
