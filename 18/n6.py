import tkinter


def show_key(event):
    a1 = [event.keysym, event.char, event.keycode, event.keysym_num]
    a1 = [str(i) for i in a1]
    label.config(text=', '.join(a1))


master = tkinter.Tk()
label = tkinter.Label(master, text="Hello world!")
label.pack()
master.bind("<KeyPress>", show_key)
master.mainloop()
