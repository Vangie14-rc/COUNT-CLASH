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

#Create the main window
app = tk.Tk()
app.title("MATH QUIZ")
app.geometry("1000x600")
app.resizable(False, False)

#CLose the main window
def close_window():
    app.destroy()
    print("Window Closing...")

#Easy level: basic word problems
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

#Medium level: image based graph questions
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

#Hard level: algebra, logic, worded maths
hard_questions = [
    {"question": "If 3x + 5 = 14, what is the value of x?",
     "answer": "3",
     "explanation": "Think of this equation like a balanced scale. To find x, we need to get it alone on one side. First, we subtract 5 from both sides to keep things balanced (3x = 9). Then, we divide both sides by 3, like splitting the weight equally, to find that x = 3.",
     },
    
    {"question": "Ben pays $40 per month to attend a weekly yoga class. His sister Ilene gets a discount at her yoga class and pays $35 per month. Over the course of one year, how much more money does Ben pay a year to attend his yoga class?",
     "answer": "60",
     "explanation": "Ben pays $5 more per month than Ilene. Over 12 months, that's $5 x 12 = $60 more per year. "
     },
    
    {"question": "Solve for y in the equation: y - 13 = -3",
     "answer": "10",
     "explanation": "To find y, add 13 to both sides of the equation. Since y minus 13 equals -3, adding 13 to -3 gives 10. So, equals 10."
     },
    
    {"question": "If p m q = p + q + p/q, the value of 8 m 2 is:",
     "answer": "14",
     "explanation": "For 8 m 2, add 8 and 2, then add 8 divided by 2. That's 8 + 2 + 4 = 14. So, the answer is 14."
     },
    
    {"question": "Simplify the expression: 4(2x - 3) + 2(x + 5)",
     "answer": "10x - 2",
     "explanation": "Firstly, multiply inside the parentheses: 4 times (2x - 3) is 8x - 12, and 2 times (x + 5) is 12 + 10. Then, add them together: 8x - 12 + 2x + 10 = 10x - 2"
     },
    
    {"question": "Y = 27j - 7 - 7j. If y = 13, what will j be equal to?",
     "answer": "1",
     "explanation": "First, combine like terms to get y equals 20j minus 7. Since y is 13, add 7 to both sides to get 20, then divide by 20. So, j equals 1."
     },
    
    {"question": "Solve for y: 2(y - 4) = 3(y + 2)?",
     "answer": "-14",
     "explanation": "First, multiply out both sides of the equation. You get 2y minus 8 on the left and 3y plus 6 on the right. Then, move the 2y to the right by sbtracting it from both sides, leaving -8 equals y plus 6. Next, subtract 6 from both sidies to isolate y, which gives you -14. So, y is -14"
     },
    
    {"question": "What is the slope of the line represented by the equation y = -2x + 5?",
     "answer": "-2",
     "explanation": "The -2 before the x shows the slope, which tells how steep the line is. Since it's negative, the line goes down as you move right."
     },
    
    {"question": "If a * b = 2 (a + b), then 5 * 2 is equal to:",
     "answer": "14",
     "explanation": "If a * b means twice the sum of a and b, then 5 * 2 is 2 times (5 + 2), which equals 14"
     },
    
    {"question": "What is the slope of a straight line that connects the following points.(1,2) & (4,11)",
     "answer": "3",
     "explanation": "To find the slope, subtract the y-values and divide by the difference of the x-values. SO, (11 - 2) divided by (4 - 1) equals 9 divided by 3, which is 3. The slope is 3"
     },]

#***************************HARD QUIZ WINDOW**********************************
def open_hard_quiz():
    global score
    score = 0
    hard_win = tk.Toplevel(app)
    hard_win.title("Hard Math Quiz")
    hard_win.geometry("1000x600")
    hard_win.resizable(False,False)

    current_question_index = [0]

    #Background image for the hard quiz window
    bg_hard_image = tk.PhotoImage(file="math.png")
    bg_label_hard = tk.Label(hard_win, image=bg_hard_image)
    #Keep a reference so image doesn't dissapear
    bg_label_hard.image = bg_hard_image
    bg_label_hard.place(x=0, y=0, relwidth=1, relheight=1)

    #Function to show the current question and image
    def show_question():
        question_data = hard_questions[current_question_index[0]]
        question_label.config(text=f"Q{current_question_index[0] + 1}: {question_data['question']}")
        answer_entry.delete(0, tk.END)
        
        
    #Move to the next question or end the quiz
    def next_question():
        current_question_index[0] += 1
        if current_question_index[0] < len(hard_questions):
            show_question()
        else:
            hard_win.destroy()
            show_score_hard_window()
            
    #Check the user's answer and update score
    def check_answer():
        global score
        student_answer = answer_entry.get().strip()
        correct_answer = hard_questions[current_question_index[0]]["answer"]
        explanation = hard_questions[current_question_index[0]]["explanation"]

        if student_answer == correct_answer:
            score+= 1
            messagebox.showinfo("Correct", "Good Job! Goodluck to the next part!")
        else:
            messagebox.showinfo("Incorrect", f"The correct answer was: {correct_answer},\n\n\n {explanation}")
            
      #Delay check answer before showing next question
        hard_win.after(1100, next_question)


    # Label to display the current math question
    question_label = tk.Label(hard_win, text="", font=("Adamina", 20),bg='#001122', fg="white", wraplength=550)
    question_label.place(relx=0.5, rely=0.27, anchor="center")
    
    # Entry box for typing answer
    answer_entry = tk.Entry(hard_win, font=("Nico Moji", 18), justify="center")
    answer_entry.place(relx=0.5, rely=0.47, relwidth=0.19, anchor="center") 
    
   # Submit button to check answer
    submit_btn = tk.Button(hard_win, text="SUBMIT", font=("Nico Moji", 16),bg='#001122', fg="white", command=check_answer)
    submit_btn.place(relx=0.44, rely=0.53, relwidth=0.13, relheight=0.09)
    
    #Back to difficulty menu
    back_btn = tk.Button(hard_win, text="BACK", font=("Nico Moji", 18), fg="white", bg='#001122', command=open_difficulty_window)
    back_btn.place(relx=0.01, rely=0.88, relwidth=0.10, relheight=0.09)

    #Restart the hard quiz
    restart_btn = tk.Button(hard_win, text="RESTART", font=("Nico Moji", 18), fg="white", bg='#001122', command=open_hard_quiz)
    restart_btn.place(relx=0.85, rely=0.88, relwidth=0.14, relheight=0.09)
   
    #Show the first question to start
    show_question()
     

#Hard score window, display the final score
def show_score_hard_window():
    score_hard_win = tk.Toplevel(app)
    score_hard_win.title("Final Score")                      
    score_hard_win.geometry("1000x600")
    score_hard_win.resizable(False,False)

    # Background Image
    bg_score_image = tk.PhotoImage(file="math3.png")
    bg_label_score = tk.Label(score_hard_win, image=bg_score_image)
    bg_label_score.image = bg_score_image
    bg_label_score.place(x=0, y=0, relwidth=1, relheight=1)

    #Get player name
    user_name = name_entry.get() or "Player"

    #Name display  
    name_label = tk.Label(score_hard_win, text=f"{user_name}", font=("Adamina", 23, "bold"), fg="white", bg='#001122' )
    name_label.place(relx=0.5, rely=0.43, anchor="center")

    #Text label "YOUR SCORE"
    score_display = tk.Label(score_hard_win, text=f"YOUR SCORE", font=("Adamina", 17 ), fg="white", bg='#001122' )
    score_display.place(relx=0.5, rely=0.50, anchor="center")
    
    #Score value
    s_display = tk.Label(score_hard_win, text=f" {score} / {len(easy_questions)}", font=("Adamina", 25, "bold"), fg="white", bg='#001122' )
    s_display.place(relx=0.5, rely=0.57, anchor="center")
    

    #Button to restart the hard quiz
    def hard_restart_quiz():
        score_hard_win.destroy()
        open_hard_quiz()

     #Button to go back to difficulty selection
    def continue_quiz():
        score_hard_win.destroy()
        open_difficulty_window()
        
     #Button to close the app
    def exit_quiz():
        app.destroy()

    #Restart button for score hard window
    restart_btn = tk.Button(score_hard_win, text="RESTART", font=("Nico Moji", 18), command=hard_restart_quiz, fg="white", bg='#001122')
    restart_btn.place(relx=0.28, rely=0.60, relwidth=0.14, relheight=0.09)

    #Continue button for score hard window
    continue_btn = tk.Button(score_hard_win, text="CONTINUE", font=("Nico Moji", 18), command=continue_quiz, fg="white", bg='#001122')
    continue_btn.place( relx=0.59, rely=0.60, relwidth=0.16, relheight=0.09)

    #Exit button for score hard window
    exit_btn = tk.Button(score_hard_win, text="EXIT", font=("Nico Moji", 18), fg="white", bg='#001122', command=exit_quiz)
    exit_btn.place(relx=0.01, rely=0.88, relwidth=0.10, relheight=0.09)
    

#*********************************MEDIUM QUIZ WIDOW************************************
def open_medium_quiz():
    global score
    #Reset score to 0 for the new quiz
    score= 0
    medium_win = tk.Toplevel(app)
    medium_win.title("Medium Math Quiz")
    medium_win.geometry("1000x600")
    medium_win.resizable(False,False)

    current_question_index = [0]

    #Background image for the medium quiz window
    bg_medium_image = tk.PhotoImage(file="math.png")
    bg_label_medium = tk.Label(medium_win, image=bg_medium_image)
    #Keep a reference so image doesn't dissapear
    bg_label_medium.image = bg_medium_image
    bg_label_medium.place(x=0, y=0, relwidth=1, relheight=1)

    #Function to show the current question and image
    def show_question():
        question_data = medium_questions[current_question_index[0]]
        question_label.config(text=f"Q{current_question_index[0] + 1}: {question_data['question']}")

        try:
            #Load and rezise the imag for the current question
            image = Image.open(question_data["image"])
            image = image.resize((400,300), Image.LANCZOS)
            img = ImageTk.PhotoImage(image)
            image_label.config(image=img)
            image_label.image = img   
        except  FileNotFoundError:
            #If image file is missing, display error text instead
            image_label.config(image="", text="Image not found", font=("Arial", 14))
           
            
           #Clear any previous answer or feedback
            answer_entry.delete(0, tk.END)
            result_label.config(text="")

    #Move to the next question or end the quiz if finished
    def next_question():
        current_question_index[0] +=1
        if current_question_index[0] <len(medium_questions):
            show_question()
        else:
            medium_win.destroy()
            show_score_medium_window()

   #Check the user's answer and update score
    def check_answer():
        global score
        student_answer =answer_entry.get().strip()
        correct_answer = medium_questions[current_question_index[0]]["answer"]

        if student_answer == correct_answer:
            score+= 1
            messagebox.showinfo("Correct", "Nice Work! Goodluck to the next part")
        else:
            messagebox.showinfo("Incorrect", f"The correct answer was:{correct_answer}")

        #Wait seconds then move to the next question    
        medium_win.after(1000, next_question)

    # Label to display the current math question
    question_label = tk.Label(medium_win, text="", font=("Adamina", 20),bg='#001122', fg="white", wraplength=550)
    question_label.place(relx=0.72, rely=0.35, anchor="center")

    # Label to display the question image
    image_label = tk.Label(medium_win)
    image_label.place(relx=0.04, rely=0.20, relwidth=0.40)
    
    # Entry box for the user to type their answer
    answer_entry = tk.Entry(medium_win, font=("Nico Moji", 18), justify="center")
    answer_entry.place(relx=0.71, rely=0.52, relwidth=0.16, anchor="center") 
    
   # Submit button
    submit_btn = tk.Button(medium_win, text="SUBMIT", font=("Nico Moji", 16),bg='#001122', fg="white", command=check_answer)
    submit_btn.place(relx=0.65, rely=0.58, relwidth=0.13, relheight=0.09)

    #Back button returns to difficulty selection
    back_btn = tk.Button(medium_win, text="BACK", font=("Nico Moji", 18), fg="white", bg='#001122', command=open_difficulty_window)
    back_btn.place(relx=0.01, rely=0.88, relwidth=0.10, relheight=0.09)

    #Restart button start from easy quiz again
    restart_btn = tk.Button(medium_win, text="RESTART", font=("Nico Moji", 18), fg="white", bg='#001122', command=open_medium_quiz)
    restart_btn.place(relx=0.85, rely=0.88, relwidth=0.14, relheight=0.09)
   
    #Show the first question to start
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

    #Show the player's name
    name_label = tk.Label(score_medium_win, text=f"{user_name}", font=("Adamina", 23, "bold"), fg="white", bg='#001122' )
    name_label.place(relx=0.5, rely=0.43, anchor="center")

    #Label for score heading
    score_display = tk.Label(score_medium_win, text=f"YOUR SCORE", font=("Adamina", 17), fg="white", bg='#001122' )
    score_display.place(relx=0.5, rely=0.50, anchor="center")
    
    #Show the actual score
    s_display = tk.Label(score_medium_win, text=f" {score} / {len(easy_questions)}", font=("Adamina", 25, "bold"), fg="white", bg='#001122' )
    s_display.place(relx=0.5, rely=0.57, anchor="center")
    

    #Button to restart the quiz
    def medium_restart_quiz():
        score_medium_win.destroy()
        open_medium_quiz()

    #Button to go back to difficulty selection
    def continue_quiz():
        score_medium_win.destroy()
        open_difficulty_window()
        
    #Button to close the app
    def exit_quiz():
        app.destroy()


    restart_btn = tk.Button(score_medium_win, text="RESTART", font=("Nico Moji", 18), command=medium_restart_quiz, fg="white", bg='#001122')
    restart_btn.place(relx=0.28, rely=0.60, relwidth=0.14, relheight=0.09)
 
    continue_btn = tk.Button(score_medium_win, text="CONTINUE", font=("Nico Moji", 18), command=continue_quiz, fg="white", bg='#001122')
    continue_btn.place( relx=0.59, rely=0.60, relwidth=0.16, relheight=0.09)

    exit_btn = tk.Button(score_medium_win, text="EXIT", font=("Nico Moji", 18), fg="white", bg='#001122', command=exit_quiz)
    exit_btn.place(relx=0.01, rely=0.88, relwidth=0.10, relheight=0.09)
    

    
#**************************EASY QUIZ WINOW*******************************
def open_easy_quiz():
    global score
    score = 0
    easy_win = tk.Toplevel(app)
    easy_win.title("Easy Math Quiz")
    easy_win.geometry("1000x600")
    easy_win.resizable(False,False)

    #Keep track of wich question's we're on
    current_question_index = [0]
    
    # Background image
    bg_easy_image = tk.PhotoImage(file="math.png")
    bg_label_easy = tk.Label(easy_win, image=bg_easy_image)
    bg_label_easy.image = bg_easy_image
    bg_label_easy.place(x=0, y=0, relwidth=1, relheight=1)

    #Function to show the current  question
    def show_question():
        question_data = easy_questions[current_question_index[0]]
        question_label.config(text=f"Q{current_question_index[0] + 1}: {question_data['question']}")
        answer_entry.delete(0, tk.END) 
        
    #Move to the next question or show final score
    def next_question():
        current_question_index[0] += 1
        if current_question_index[0] < len(easy_questions):
            show_question()
        else:
            easy_win.destroy()
            show_score_easy_window()
            
    #Check if the user answer is correct
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

    #Show the player's name
    name_label = tk.Label(score_easy_win, text=f"{user_name}", font=("Adamina", 23, "bold"), fg="white", bg='#001122' )
    name_label.place(relx=0.5, rely=0.43, anchor="center")

    #Label for score heading
    score_display = tk.Label(score_easy_win, text=f"YOUR SCORE", font=("Adamina", 17), fg="white", bg='#001122' )
    score_display.place(relx=0.5, rely=0.50, anchor="center")
    
    #Show the actual score
    s_display = tk.Label(score_easy_win, text=f" {score} / {len(easy_questions)}", font=("Adamina", 25, "bold"), fg="white", bg='#001122' )
    s_display.place(relx=0.5, rely=0.57, anchor="center")
    

    #Button to restart the quiz
    def easy_restart_quiz():
        score_easy_win.destroy()
        open_easy_quiz()

     #Button to go back to difficulty selection
    def continue_quiz():
        score_easy_win.destroy()
        open_difficulty_window()
        
   #Button to close the app
    def exit_quiz():
        app.destroy()

    
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
    
    #Difficulty Image Background Window
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
    hard_btn = tk.Button(diff_win, text="HARD", font=("Nico Moji", 18), fg="white", bg='#001122', command=open_hard_quiz)
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

#Name entry field
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
