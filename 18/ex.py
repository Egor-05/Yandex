import tkinter

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
canvas.create_rectangle((100, 100), (500, 500), fill='red')
canvas.create_oval((100, 100), (500, 500), fill='blue')
canvas.pack()
master.mainloop()
