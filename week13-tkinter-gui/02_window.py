# Week 13 - Part 1: the window and mainloop()
# Software Programming (IGS1931)
#
# Run it and watch the Shell: which lines are printed, and when?
# Then close the window and look again.

from tkinter import *

print("1. Before Tk()")

window = Tk()
window.title("Hello Python")
window.geometry("600x400+60+40")    # width x height + x + y (x, y = distance from the screen's top-left)
window.resizable(False, False)      # the user cannot make it bigger or smaller

print("2. The window is made. Now mainloop() starts...")

window.mainloop()                   # waits here and handles clicks and key presses

print("3. After mainloop(): printed only when you CLOSE the window")
