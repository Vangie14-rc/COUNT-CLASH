"""
Author:         [Vangie Coloma]
Date:           2025/05/15
Version:        1.1.0
Description:    This program is a math quiz for primary school students. It uses a simple Tkinter interface to ask questions, check answers,
                and give feedback to help kids practice basic and medium math skills.
Language:       Python 3.10
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage


# Initialize the main app window
app = tk.Tk()
app.title("MATH QUIZ")
app.geometry("1000x600")
app.resizable(False, False)


def close_window():
    app.destroy()
    print("Window Closing...")

#Difficulties Window, Image Background and Difficcultiy Button
def open_difficulty_window():
    print("Difficulties Window Opening...")
    diff_win = tk.Toplevel(app)
    diff_win.title("MATH QUIZ")
    diff_win.geometry("1000x600")
    diff_win.resizable(False, False)
    
    #Difficulty Image Window
    bg_diff_image = tk.PhotoImage(file="math2.png")
    bg_label_diff = tk.Label(diff_win, image=bg_diff_image)
    bg_label_diff.image = bg_diff_image
    bg_label_diff.place(x=0, y=0, relwidth=1, relheight=1)



    #Easy Button
    easy_btn = tk.Button(diff_win, text="EASY", font=("Nico Moji", 18), fg="white", bg='#001122')
    easy_btn.place(relx=0.28, rely=0.55, relwidth=0.13, relheight=0.09)
    #Medium Button   
    medium_btn = tk.Button(diff_win, text="MEDIUM", font=("Nico Moji", 18), fg="white", bg='#001122' )
    medium_btn.place(relx=0.59, rely=0.55, relwidth=0.13, relheight=0.09)
    #Hard Buton
    hard_btn = tk.Button(diff_win, text="HARD", font=("Nico Moji", 18), fg="white", bg='#001122')
    hard_btn.place(relx=0.44, rely=0.65, relwidth=0.13, relheight=0.09)
    #Exit Button
    exit_btn = tk.Button(diff_win, text="EXIT", font=("Nico Moji", 18), fg="white", bg='#001122')
    exit_btn.place(relx=0.01, rely=0.88, relwidth=0.10, relheight=0.09)


# Starts the quiz by validating the name entry and opening difficulty selection
def start(name_entry):
    user_input = name_entry.get()
    
    if user_input =="":
        messagebox.showerror("Invalid Name", "Plase enter your name to start.")
        print ("Plase no Blanks!")
    else:
        open_difficulty_window()


#Main window background image
bg_image = PhotoImage(file="math1.png")
bg_label = tk.Label(app, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

name_entry = tk.Entry(app, font=("Nico Moji", 15), justify="center")
name_entry.place(relx=0.5, rely=0.65, anchor="center") 

#Start Button
start_button = tk.Button(app, text="START", font=("Nico Moji", 18), fg="white",  bg='#001122', command=lambda: start(name_entry))
start_button.place(relx=0.44, rely=0.75, relwidth=0.13, relheight=0.09)

# Exit button
exit_button = tk.Button(app, text="EXIT", font=("Nico Moji", 18), fg="white",  bg='#001122', command=close_window)
exit_button.place(relx=0.01, rely=0.88, relwidth=0.10, relheight=0.09)

# Start the Tkinter event loop
app.mainloop()
