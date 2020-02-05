import tkinter
import random


def draw(event):
    a1 = random.randint(1, 600)
    a2 = random.randint(1, 600)
    a3 = random.randint(1, 600)
    a4 = random.randint(1, 600)
    canvas.create_oval((a1, a2), (a3, a4), fill='red')
    return


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
canvas.pack()
master.bind("<KeyPress>", draw)
master.mainloop()
