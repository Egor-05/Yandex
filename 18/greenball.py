import tkinter


def move_wrap(canvas, obj, move):
    canvas.move(obj, move[0], move[1])
    x = canvas.coords(obj)[0]
    y = canvas.coords(obj)[1]
    if 100 < y < 500 and 100 < x < 500:
        canvas.itemconfig(obj, fill='green')
    else:
        canvas.itemconfig(obj, fill='red')
    if x < 0 or x > 600:
        canvas.move(obj, x / abs(x) * -600, 0)
    if y < 0 or y > 600:
        canvas.move(obj, 0, y / abs(y) * -600)


def key_pressed(event):
    if event.keysym == 'space':
        canvas.coords(oval, (300, 300, 310, 310))
        canvas.itemconfig(oval, fill='green')
    if event.keysym == 'Up':
        move_wrap(canvas, oval, (0, -10))
    elif event.keysym == 'Down':
        move_wrap(canvas, oval, (0, 10))
    elif event.keysym == 'Right':
        move_wrap(canvas, oval, (10, 0))
    elif event.keysym == 'Left':
        move_wrap(canvas, oval, (-10, 0))
    # if y < 100 or y > 500 or x < 100 or x > 500:
    #     canvas.itemconfig(oval, fill='red')
    # elif canvas.coords(oval)[1] :
    #     canvas.itemconfig(oval, fill='red')
    # elif canvas.coords(oval)[0] :
    #     canvas.itemconfig(oval, fill='red')
    # elif canvas.coords(oval)[0] :
    #     canvas.itemconfig(oval, fill='red')
    # else:
    #     canvas.itemconfig(oval, fill='green')


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
oval = canvas.create_oval((300, 300), (310, 310), fill='green')
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
