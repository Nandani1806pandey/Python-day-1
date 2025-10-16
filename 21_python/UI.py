from tkinter import *

THEME_COLOR = "#375362"
class quizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row = 0, column = 1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,125,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 14, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

    
        # ✅ True button
        true_image = PhotoImage(file="True.jpg")
        self.true_button = Button(image=true_image,highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        # ✅ False button
        false_image = PhotoImage(file="False.jpg")
        self.false_button = Button(image=false_image,highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_question():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz! 🎉")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)