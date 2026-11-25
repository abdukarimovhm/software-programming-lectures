# Week 13 - Build-along: Mini To-Do, step 1 of 5
# Software Programming (IGS1931)
#
# Step 1: an empty window with a title.
# Fell behind? Open the next step file: each one is complete and runs.

from tkinter import *

root = Tk()
root.title("Mini To-Do")
root.geometry("320x400")

Label(root, text="My Tasks", font=("Arial", 18, "bold")).pack(pady=10)

root.mainloop()
