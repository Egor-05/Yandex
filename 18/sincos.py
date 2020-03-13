import tkinter
import math


points = []
a = int(input())
master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
for i in range(a):
    points.append((round(300 + (math.cos(2 * math.pi * i / a) * 100)),
                   round(300 + (math.sin(2 * math.pi * i / a) * 100))))
a1 = a // 3 + 1
s = 0
for i in range(a + 1):
    s1 = s
    s = (s + a1) % a
    canvas.create_line(points[s1], points[s], fill='red')
canvas.pack()
master.mainloop()
