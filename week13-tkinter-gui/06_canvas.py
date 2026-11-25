# Week 13 - Part 5: drawing on a Canvas
# Software Programming (IGS1931)
#
# (0, 0) is the TOP-LEFT corner. x grows to the right, y grows DOWN.
# Most shapes take a box: x0, y0 (top-left corner) and x1, y1 (bottom-right corner).

from tkinter import *

top = Tk()
top.title("Canvas")

C = Canvas(top, bg="white", height=300, width=400)

C.create_rectangle(20, 20, 120, 100, fill="yellow")            # box from (20, 20) to (120, 100)
C.create_oval(140, 20, 240, 100, fill="pink")                  # the oval fits inside its box
C.create_polygon(320, 20, 380, 100, 260, 100, fill="green")    # corners (320,20) (380,100) (260,100)
C.create_line(20, 140, 380, 140, width=3)                      # from (20, 140) to (380, 140)

coord = 20, 170, 140, 290
C.create_arc(coord, start=0, extent=150, fill="red")           # the arc from the slides

C.create_text(270, 230, text="Hello Canvas", font=("Arial", 16))

C.pack()
top.mainloop()
