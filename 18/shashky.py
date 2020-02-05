import tkinter

s1 = 0
zdvig = 100
step = 50
master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
for i in range(8):
    s1 += 1
    s = 0
    for j in range(8):
        s += 1
        canvas.create_rectangle((i * step + zdvig, j * step + zdvig), ((i + 1) * step + zdvig, (j + 1) * step + zdvig), fill='white')
        if (s + s1) % 2 == 0 and s < 4:
            canvas.create_oval((i * step + zdvig, j * step + zdvig), ((i + 1) * step + zdvig, (j + 1) * step + zdvig), fill='red')
        elif (s + s1) % 2 == 0 and s > 5:
            canvas.create_oval((i * step + zdvig, j * step + zdvig), ((i + 1) * step + zdvig, (j + 1) * step + zdvig), fill='blue')
canvas.pack()
master.mainloop()
