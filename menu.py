import sqlite3
from tkinter import *
from sn import gameloop
from tkinter import colorchooser

root = Tk()
#root.geometry('780x600')

clr = None
score = int()
name_ent = StringVar()

conn = sqlite3.connect('test.db')
print("Connected to database")
c = conn.cursor()
c.execute("""
          CREATE TABLE if not exists data(
          player TEXT,
          score REAL
          )
          """)
conn.commit()

c.execute("SELECT * FROM data")
conn.commit()
data = c.fetchall()

for i in range(len(data)): #Rows
    #for j in range(len(data)): #Columns
    b = Label(root, text=data[i])
    b.grid(row=i,column=3)
#root.after(1000, update)



def start():
    name = name_ent.get()
    if clr == None:
        color = (0,0,0)
        score = gameloop(color)
        sql(name, score)
    else:
        score = gameloop(clr[0])
        sql(name, score)

def snake_color():
    global clr
    clr = colorchooser.askcolor(title='Select Color')
    #print(clr)

def sql(name, score):
    if name == "":
        name = "Unknown"

    print("Working")
    c.execute("""
              CREATE TABLE if not exists data(
              player TEXT,
              score REAL
              )
              """)
    conn.commit()

    c.execute("INSERT INTO data(player, score) VALUES(:player, :score)", {"player": name, "score": int(score)})
    conn.commit()


    c.execute("SELECT * FROM data")
    conn.commit()
    data = c.fetchall()

    for i in range(len(data)): #Rows
        #for j in range(len(data)): #Columns
        b = Label(root, text=data[i])
        b.grid(row=i,column=3)
#root.after(1000, update)


label_user = Label(root, text="Enter Player Name: ").grid(row = 1, column = 0)
entry_user = Entry(root, textvariable = name_ent).grid(row = 1, column = 1)

start = Button(root, text = "Start", command = start).grid(row = 3, column = 0)
color_button = Button(root, text= "Snake Color", command = snake_color ).grid(row=3, column=1)


root.mainloop()

conn.close()
