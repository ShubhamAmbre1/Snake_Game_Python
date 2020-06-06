import sqlite3
from tkinter import *
from sn import gameloop
from tkinter import colorchooser

clr = None

def start():
    if clr == None:
        color = (0,0,0)
        score = gameloop(color)
    else:
        score = gameloop(clr[0])
    print(score)

def snake_color():
    global clr
    clr = colorchooser.askcolor(title='Select Color')
    print(clr)

def sql(name, score):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    c.execute("""
              CREATE TABLE if not exists data(
              player TEXT,
              score REAL
              )
              """)
    conn.commit()

    c.execute("INSERT INTO data(player, score) VALUES(:player, :score)", {"player": name, "score": score})
    conn.commit()
    conn.close()

root = Tk()

label_user = Label(root, text="Enter Player Name: ").grid(row = 1, column = 0)
label_best_score = Label(root, text = "High Score").grid(row = 2, column = 0)

start = Button(root, text = "Start", command = start).grid(row = 3, column = 0)
color_button = Button(root, text= "Snake Color", command = snake_color ).grid(row=3, column=1)

mainloop()

