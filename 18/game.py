import tkinter
import random


def prepare_and_start():
    global player, exit, fires, enemy
    canvas.delete("all")
    enemy_pos = (random.randint(1, N_X - 1) * step,
                 random.randint(1, N_Y - 1) * step)
    player_pos = (random.randint(1, N_X - 1) * step,
                  random.randint(1, N_Y - 1) * step)
    exit_pos = (random.randint(1, N_X - 1) * step,
                random.randint(1, N_Y) * step)
    enemy = canvas.create_oval(
        (enemy_pos[0], enemy_pos[1]),
        (enemy_pos[0] + step, enemy_pos[1] + step),
        fill='black')
    player = canvas.create_oval(
        (player_pos[0], player_pos[1]),
        (player_pos[0] + step, player_pos[1] + step),
        fill='green')
    exit = canvas.create_oval(
        (exit_pos[0], exit_pos[1]),
        (exit_pos[0] + step, exit_pos[1] + step),
        fill='yellow')
    N_FIRES = 6  # Число клеток, заполненных огнем
    fires = []
    xx = []
    yy = []
    for i in range(N_FIRES):
        x = random.randint(1, N_X - 1) * step
        y = random.randint(1, N_Y - 1) * step
        if x in xx and y in yy:
            while 1:
                x = random.randint(1, N_X - 1) * step
                y = random.randint(1, N_Y - 1) * step
                if x not in xx:
                    xx.append(x)
                    break
                if y not in yy:
                    yy.append(y)
                    break
        fire_pos = (x, y)
        fire = canvas.create_oval(
            (fire_pos[0], fire_pos[1]),
            (fire_pos[0] + step, fire_pos[1] + step),
            fill='red')
        fires.append(fire)
    label.config(text="Найди выход!")
    master.bind("<KeyPress>", key_pressed)


def move_enemy()


def move_wrap(obj, move):
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


def do_nothing(x):
    pass


def check_move():
    if canvas.coords(player) == canvas.coords(exit):
        label.config(text="Победа!")
        master.bind("<KeyPress>", do_nothing)
    for f in fires:
        if canvas.coords(player) == canvas.coords(f) or canvas.coords(player) == canvas.coords(enemy):
            label.config(text="Ты проиграл!")
            master.bind("<KeyPress>", do_nothing)


def key_pressed(event):
    if event.keysym == 'Up':
        move_wrap(player, (0, -step))
    elif event.keysym == 'Down':
        move_wrap(player, (0, step))
    elif event.keysym == 'Right':
        move_wrap(player, (step, 0))
    elif event.keysym == 'Left':
        move_wrap(player, (-step, 0))
    check_move()


master = tkinter.Tk()

step = 60  # Размер клетки
N_X = 10
N_Y = 10   # Размер сетки
master = tkinter.Tk()
label = tkinter.Label(master, text="Найди выход")
label.pack()
canvas = tkinter.Canvas(master, bg='blue',
                        height=N_X * step, width=N_Y * step)
canvas.pack()
restart = tkinter.Button(master, text="Начать заново",
                         command=prepare_and_start)
restart.pack()
prepare_and_start()
master.mainloop()