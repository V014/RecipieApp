import tkinter as tk
import sqlite3
from PIL import ImageTk
from numpy import random
import pyglet

# set colours
bg_color ="#3d6466"

def fetch_db():
    connection = sqlite3.connect("assets/recipies.db")
    cursor = connection.cursor()
    # fetch all the table names
    cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
    all_tables = cursor.fetchall()
    # choose random recipie idx
    idx = random.randint(0, len(all_tables)-1)

    # fetch ingredients
    table_name = all_tables[idx][1]
    cursor.execute("SELECT * FROM " + table_name + ";")
    table_records = cursor.fetchall()

    connection.close()
    return table_name, table_records

def pre_process(table_name, table_records):
    title = table_name[:-6]
    title = "".join([char if char.islower() else " " + char for char in title])
    print(title)

def load_frame1():
    frame1.pack_propagate(False)
    # frame1 widgets
    logo_img = ImageTk.PhotoImage(file="assets/img/icon.png") 
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack()

    tk.Label(frame1,
          text="Ready for your random recipie?",
          bg=bg_color,
          fg="white",
          font=("TkMenuFont", 14)
         ).pack()

    # button widget
    tk.Button(
        frame1,
        text="SHUFFLE",
        font=("TkHeadingFont", 20),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame2()
        ).pack(pady=20)

def load_frame2():
    table_name, table_records = fetch_db()
    pre_process(table_name, table_records)

# initallize app
root = tk.Tk()
root.title("Recipe Picker")
#root.eval("tk::PlaceWindow . center")

# place app in the center of the screen
x= root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)
root.geometry('500x500+' + str(x) + '+' + str(y))

#create a frame widget
frame1 = tk.Frame(root, width=500, height=500, bg=bg_color)
frame2 = tk.Frame(root, bg=bg_color)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0)

load_frame1()

# run app
root.mainloop()