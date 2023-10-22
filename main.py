import tkinter as tk
from turtle import bgcolor
from PIL import ImageTk

bg_color ="#3d6466"

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
    print("hello void")

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