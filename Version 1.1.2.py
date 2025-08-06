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
from PIL import Image, ImageTk

# Initialize the main app window
app = tk.Tk()
app.title("MATH QUIZ")
app.geometry("1000x600")
app.resizable(False, False)


def close_window():
    app.destroy()
    print("Window Closing...")

# List of easy level math questions and answers
easy_questions = [
    {"question": "Vangie has 15 apples. She ate 5 apples. How many apples does she have now?", "answer": "10" },
    {"question": "There are 6 birds on a tree. 4 fly away. How many are left?", "answer": "2" },
    {"question": "Pranav has 5 pencils. He gives 3 to his friends. How many does he have left?","answer": "2" },
    {"question": "Ralph baked 8 cookies. He ate 3. How many are left?", "answer": "5" },
    {"question": "Gorgy have 10 candies. She give away 4. How many do you have now?","answer": "6" },
    {"question": "Liam has 7 toy cars. He buys 2 more. How many does he have?", "answer": "9" },
    {"question": "A jar has 9 sweets. You eat 5. How many are in the jar now?", "answer": "4" },
    {"question": "There are 100 frogs. 60 more join but, 10 frogs leave. How many frogs are there now?", "answer": "150" },
    {"question": "Abhishek has 20 balloons. 7 flies away. How many are left?", "answer": "13" },
    {"question": "You have 20 dollars.You buy an apple worth 4 dollars. How much money do you have?", "answer": "16" },
]

#List of medium level match questions and answers
medium_questions = [
    {"image": "fig8.png", "question": "What is the gradient of the line EF?", "answer": "3"},
    {"image": "fig1.png", "question": "What is y-intercept?", "answer": "3"},
    {"image": "fig10.png","question": "How would you describe the gtradient of all the lines? Positive, Negative, or Zero", "answer": "Positive"},
    {"image": "fig3.png", "question": "What is the slope of the line?", "answer": "-4"},
    {"image": "fig5.png","question": "How would you describe the gradient of all the lines? Positive, Negative, or Zero", "answer": "Negative"},
    {"image": "fig4.png", "question": "What is the y-intercept?", "answer": "4"},
    {"image": "fig6.png", "question": "What is the gradient of the line KL?", "answer": "-1"},
    {"image": "fig7.png", "question": "How would you describe the gradient of all the lines? Positive, Negative, or Zero", "answer": "Zero"},
    {"image": "fig9.png", "question": "What is the gradient of the line GH?", "answer": "-2/11"},
    {"image": "fig2.png", "question": "What is the slope?", "answer": "-2"},
    ]


#Opne Medium Quiz Window
def open_medium_quiz():
    global score
    score= 0
    medium_win = tk.Toplevel(app)
    medium_win.title("Medium MAth Quiz")
    medium_win.geometry("1000x600")
    medium_win.resizable(False,False)

    current_question_index = [0]

    #Background Image to Medium Quiz
    bg_medium_image = tk.PhotoImage(file="math.png")
    bg_label_medium = tk.Label(medium_win, image=bg_medium_image)
    bg_label_medium.image = bg_medium_image
    bg_label_medium.place(x=0, y=0, relwidth=1, relheight=1)

    def show_question():
        question_data = medium_questions[current_question_index[0]]
        question_label.config(text=f"Q{current_question_index[0] + 1}: {question_data['question']}")

        try:
            #Medium image question
            image = Image.open(question_data["image"])
            image = image.resize((400,300), Image.LANCZOS)
            img = ImageTk.PhotoImage(image)
            image_label.config(image=img)
            image_label.image = img   
        except  FileNotFoundError: 
            image_label.config(image="", text="Image not found", font=("Arial", 14))
           
            
           #Reset answer entry and result label for the new question
            answer_entry.delete(0, tk.END)
            result_label.config(text="")

    def next_question():
        current_question_index[0] +=1
        if current_question_index[0] <len(medium_questions):
            show_question()
        else:
            medium_win.destroy()
            show_score_medium_window()

    def check_answer():
        global score
        student_answer =answer_entry.get().strip()
        correct_answer = medium_questions[current_question_index[0]]["answer"]

        if student_answer == correct_answer:
            score+= 1
            messagebox.showinfo("Correct", "Nice Work! Goodluck to the next part")
        else:
            messagebox.showinfo("Incorrect", f"The correct answer was:{correct_answer}")
            
        medium_win.after(1000, next_question)

    # Label to display the current math question
    question_label = tk.Label(medium_win, text="", font=("Adamina", 20),bg='#001122', fg="white", wraplength=550)
    question_label.place(relx=0.72, rely=0.35, anchor="center")

    # Display the image related to the question
    image_label = tk.Label(medium_win)
    image_label.place(relx=0.04, rely=0.20, relwidth=0.40)
    
    # Entry box for the user to type their answer
    answer_entry = tk.Entry(medium_win, font=("Nico Moji", 18), justify="center")
    answer_entry.place(relx=0.71, rely=0.52, relwidth=0.16, anchor="center") 
    
   # Button to submit the answer and trigger the check_answer function
    submit_btn = tk.Button(medium_win, text="SUBMIT", font=("Nico Moji", 16),bg='#001122', fg="white", command=check_answer)
    submit_btn.place(relx=0.65, rely=0.58, relwidth=0.13, relheight=0.09)

    back_btn = tk.Button(medium_win, text="BACK", font=("Nico Moji", 18), fg="white", bg='#001122', command=open_difficulty_window)
    back_btn.place(relx=0.01, rely=0.88, relwidth=0.10, relheight=0.09)

    restart_btn = tk.Button(medium_win, text="RESTART", font=("Nico Moji", 18), fg="white", bg='#001122', command=open_easy_quiz)
    restart_btn.place(relx=0.85, rely=0.88, relwidth=0.14, relheight=0.09)
   
    #Start with the first question
    show_question()
    
# Show the score screen after quiz ends
def show_score_medium_window():
    score_medium_win = tk.Toplevel(app)
    score_medium_win.title("Final Score")                      
    score_medium_win.geometry("1000x600")
    score_medium_win.resizable(False,False)

    # Background image
    bg_score_image = tk.PhotoImage(file="math3.png")
    bg_label_score = tk.Label(score_medium_win, image=bg_score_image)
    bg_label_score.image = bg_score_image
    bg_label_score.place(x=0, y=0, relwidth=1, relheight=1)
    
    user_name = name_entry.get() or "Player"

    #Name and score display  
    name_label = tk.Label(score_medium_win, text=f"{user_name}", font=("Adamina", 15), fg="white", bg='#001122' )
    name_label.place(relx=0.5, rely=0.42, anchor="center")

    #Score Display
    score_display = tk.Label(score_medium_win, text=f"YOUR SCORE", font=("Adamina", 15), fg="white", bg='#001122' )
    score_display.place(relx=0.5, rely=0.49, anchor="center")
    
    #Score Display
    s_display = tk.Label(score_medium_win, text=f" {score} / {len(easy_questions)}", font=("Adamina", 15), fg="white", bg='#001122' )
    s_display.place(relx=0.5, rely=0.55, anchor="center")
    

    #Restart the quiz
    def medium_restart_quiz():
        score_medium_win.destroy()
        open_medium_quiz()

    #Continue to next level
    def continue_quiz():
        score_medium_win.destroy()
        open_difficulty_window()
        
    #Exit the progam
    def exit_quiz():
        app.destroy()

    # Buttons for score window
    restart_btn = tk.Button(score_medium_win, text="RESTART", font=("Nico Moji", 18), command=medium_restart_quiz, fg="white", bg='#001122')
    restart_btn.place(relx=0.28, rely=0.60, relwidth=0.14, relheight=0.09)

    continue_btn = tk.Button(score_medium_win, text="CONTINUE", font=("Nico Moji", 18), command=continue_quiz, fg="white", bg='#001122')
    continue_btn.place( relx=0.59, rely=0.60, relwidth=0.16, relheight=0.09)

    exit_btn = tk.Button(score_medium_win, text="EXIT", font=("Nico Moji", 18), fg="white", bg='#001122', command=exit_quiz)
    exit_btn.place(relx=0.01, rely=0.88, relwidth=0.10, relheight=0.09)
    

    
#Open the easy quiz window
def open_easy_quiz():
    global score
    score = 0
    easy_win = tk.Toplevel(app)
    easy_win.title("Easy Math Quiz")
    easy_win.geometry("1000x600")
    easy_win.resizable(False,False)

    current_question_index = [0]
    
    # Background image
    bg_easy_image = tk.PhotoImage(file="math.png")
    bg_label_easy = tk.Label(easy_win, image=bg_easy_image)
    bg_label_easy.image = bg_easy_image
    bg_label_easy.place(x=0, y=0, relwidth=1, relheight=1)

    #Show the current  question
    def show_question():
        question_data = easy_questions[current_question_index[0]]
        question_label.config(text=f"Q{current_question_index[0] + 1}: {question_data['question']}")
        answer_entry.delete(0, tk.END)
        
        
    #Move to the next question or end the quiz
    def next_question():
        current_question_index[0] += 1
        if current_question_index[0] < len(easy_questions):
            show_question()
        else:
            easy_win.destroy()
            show_score_easy_window()
            
    #Check if the user name is correct
    def check_answer():
        global score
        student_answer = answer_entry.get().strip()
        correct_answer = easy_questions[current_question_index[0]]["answer"]

        if not validate_input(student_answer):
            messagebox.showwarning("Invalid Input", "Please enter a number.")
            return

        if student_answer == correct_answer:
            score+= 1
            messagebox.showinfo("Correct", "Good Job! Goodluck to the next part!")
        else:
            messagebox.showinfo("Incorrect", f"The correct answer was: {correct_answer}")
            

        easy_win.after(1000, next_question)

        
    #Validate input is a number and not empty 
    def validate_input(input_value):
        """Validate that the input is a non-empty numeric value."""
        if input_value.strip() =="":
            return False
        if not input_value.isdigit():
            return False
        return True

    # Label to display the current math question
    question_label = tk.Label(easy_win, text="", font=("Adamina", 20),bg='#001122', fg="white", wraplength=550)
    question_label.place(relx=0.5, rely=0.27, anchor="center")
    
    # Entry box for the user to type their answer
    answer_entry = tk.Entry(easy_win, font=("Nico Moji", 18), justify="center")
    answer_entry.place(relx=0.5, rely=0.40, relwidth=0.13, anchor="center") 
    
   # Button to submit the answer and trigger the check_answer function
    submit_btn = tk.Button(easy_win, text="SUBMIT", font=("Nico Moji", 16),bg='#001122', fg="white", command=check_answer)
    submit_btn.place(relx=0.44, rely=0.50, relwidth=0.13, relheight=0.09)

    back_btn = tk.Button(easy_win, text="BACK", font=("Nico Moji", 18), fg="white", bg='#001122', command=open_difficulty_window)
    back_btn.place(relx=0.01, rely=0.88, relwidth=0.10, relheight=0.09)

    restart_btn = tk.Button(easy_win, text="RESTART", font=("Nico Moji", 18), fg="white", bg='#001122', command=open_easy_quiz)
    restart_btn.place(relx=0.85, rely=0.88, relwidth=0.14, relheight=0.09)
   
    #Start with the first question
    show_question()
     

# Show the score screen after quiz ends
def show_score_easy_window():
    score_easy_win = tk.Toplevel(app)
    score_easy_win.title("Final Score")                      
    score_easy_win.geometry("1000x600")
    score_easy_win.resizable(False,False)

    # Background image
    bg_score_image = tk.PhotoImage(file="math3.png")
    bg_label_score = tk.Label(score_easy_win, image=bg_score_image)
    bg_label_score.image = bg_score_image
    bg_label_score.place(x=0, y=0, relwidth=1, relheight=1)
    
    user_name = name_entry.get() or "Player"

    #Name and score display  
    name_label = tk.Label(score_easy_win, text=f"{user_name}", font=("Adamina", 15), fg="white", bg='#001122' )
    name_label.place(relx=0.5, rely=0.42, anchor="center")

    #Score Display
    score_display = tk.Label(score_easy_win, text=f"YOUR SCORE", font=("Adamina", 15), fg="white", bg='#001122' )
    score_display.place(relx=0.5, rely=0.49, anchor="center")
    
    #Score Display
    s_display = tk.Label(score_easy_win, text=f" {score} / {len(easy_questions)}", font=("Adamina", 15), fg="white", bg='#001122' )
    s_display.place(relx=0.5, rely=0.55, anchor="center")
    

    #Restart the quiz
    def easy_restart_quiz():
        score_easy_win.destroy()
        open_easy_quiz()

    #Continue to next level
    def continue_quiz():
        score_easy_win.destroy()
        open_difficulty_window()
        
    #Exit the progam
    def exit_quiz():
        app.destroy()

    # Buttons for score window
    restart_btn = tk.Button(score_easy_win, text="RESTART", font=("Nico Moji", 18), command=easy_restart_quiz, fg="white", bg='#001122')
    restart_btn.place(relx=0.28, rely=0.60, relwidth=0.14, relheight=0.09)

    continue_btn = tk.Button(score_easy_win, text="CONTINUE", font=("Nico Moji", 18), command=continue_quiz, fg="white", bg='#001122')
    continue_btn.place( relx=0.59, rely=0.60, relwidth=0.16, relheight=0.09)

    exit_btn = tk.Button(score_easy_win, text="EXIT", font=("Nico Moji", 18), fg="white", bg='#001122', command=exit_quiz)
    exit_btn.place(relx=0.01, rely=0.88, relwidth=0.10, relheight=0.09)
    

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
    easy_btn = tk.Button(diff_win, text="EASY", font=("Nico Moji", 18), fg="white", bg='#001122', command=open_easy_quiz)
    easy_btn.place(relx=0.27, rely=0.55, relwidth=0.13, relheight=0.09)
    #Medium Button   
    medium_btn = tk.Button(diff_win, text="MEDIUM", font=("Nico Moji", 18), fg="white", bg='#001122', command=open_medium_quiz )
    medium_btn.place(relx=0.59, rely=0.55, relwidth=0.13, relheight=0.09)
    #Hard Buton
    hard_btn = tk.Button(diff_win, text="HARD", font=("Nico Moji", 18), fg="white", bg='#001122')
    hard_btn.place(relx=0.43, rely=0.65, relwidth=0.13, relheight=0.09)
    #Exit Button
    exit_btn = tk.Button(diff_win, text="EXIT", font=("Nico Moji", 18), fg="white", bg='#001122', command=close_window)
    exit_btn.place(relx=0.01, rely=0.88, relwidth=0.10, relheight=0.09)


# Starts the quiz by validating the name entry and opening difficulty selection
def start(name_entry):
    user_input = name_entry.get()
    
    if user_input =="":
        messagebox.showinfo("Invalid Name", "Plase enter your name to start.")
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
start_button.place(relx=0.44, rely=0.71, relwidth=0.13, relheight=0.09)

# Exit button
exit_button = tk.Button(app, text="EXIT", font=("Nico Moji", 18), fg="white",  bg='#001122', command=close_window)
exit_button.place(relx=0.01, rely=0.88, relwidth=0.10, relheight=0.09)

# Start the Tkinter event loop
app.mainloop()
