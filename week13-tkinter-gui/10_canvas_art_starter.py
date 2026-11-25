# Week 13 - Final challenge: Canvas Art (in your final-project team)
# Software Programming (IGS1931)
#
# Draw a flag or a small scene (a house, a robot, your campus...).
# Rules:
#   1. Use at least 4 DIFFERENT create_ methods
#      (create_oval, create_rectangle, create_line, create_polygon, create_arc, create_text).
#   2. Put your team name on it with create_text.
#   3. Keep the "Night" button working. Bonus: make it change more than the sky.
# Then we show every team's window on the projector and vote.

from tkinter import *


def night():
    C.config(bg="navy")
    C.itemconfig(sun, fill="white")     # BONUS idea: the sun becomes a moon


top = Tk()
top.title("Canvas Art")

C = Canvas(top, bg="skyblue", width=500, height=400)
C.pack()

# A start: a sun and some grass. Keep them, move them or delete them.
sun = C.create_oval(400, 30, 470, 100, fill="yellow", outline="")
C.create_rectangle(0, 320, 500, 400, fill="green", outline="")

# TODO: your drawing here


C.create_text(250, 20, text="Team: ____", font=("Arial", 14, "bold"))

Button(top, text="Night", command=night).pack()

top.mainloop()
