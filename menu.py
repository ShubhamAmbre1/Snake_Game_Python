import sqlite3
from tkinter import *
from sn import gameloop

def start():
    gameloop()

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

start = Button(root, text = "Start", command = gameloop).grid(row = 3, column = 1)

mainloop()

