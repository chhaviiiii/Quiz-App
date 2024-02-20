import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import font as tkFont
from tkinter import scrolledtext

class Quiz:
    def __init__(self, master):
        self.master = master
        master.title("Quiz App")
        master.configure(bg='#000000')  # Black background

        self.customFont = tkFont.Font(family="Helvetica", size=12)

        self.question_answer_pairs = []
        self.current_question_index = 0
        self.score = 0

        self.question_list_box = scrolledtext.ScrolledText(master, height=4, font=self.customFont, bg="#333333", fg="white")
        self.question_list_box.pack(pady=5)
        self.question_list_box.insert(tk.END, "Added Questions:\n")
        self.question_list_box.configure(state='disabled')

        self.question_label = tk.Label(master, text="Click 'Add Question' to start", font=self.customFont, bg='#000000', fg='white')
        self.question_label.pack(pady=10)

        self.entry = tk.Entry(master, font=self.customFont)
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Submit Answer", command=self.check_answer, font=self.customFont)
        self.submit_button.pack(pady=5)

        self.add_question_button = tk.Button(master, text="Add Question", command=self.add_question, font=self.customFont)
        self.add_question_button.pack(side=tk.LEFT, padx=10, pady=20)

        self.next_question_button = tk.Button(master, text="Next Question", command=self.next_question, font=self.customFont)
        self.next_question_button.pack(side=tk.RIGHT, padx=10, pady=20)

    def add_question(self):
        question = simpledialog.askstring("Input", "Enter your question", parent=self.master)
        answer = simpledialog.askstring("Input", "Enter the answer", parent=self.master)
        if question and answer:
            self.question_answer_pairs.append((question, answer))
            self.question_list_box.configure(state='normal')
            self.question_list_box.insert(tk.END, f"{len(self.question_answer_pairs)}. {question}\n")
            self.question_list_box.configure(state='disabled')
            if len(self.question_answer_pairs) == 1:
                self.next_question()

    def next_question(self):
        if self.current_question_index < len(self.question_answer_pairs):
            current_pair = self.question_answer_pairs[self.current_question_index]
            self.question_label.config(text=current_pair[0])
            self.entry.delete(0, tk.END)
            self.current_question_index += 1
        else:
            messagebox.showinfo("End of Quiz", f"Quiz finished! Your score: {self.score}")
            self.master.quit()

    def check_answer(self):
        user_answer = self.entry.get()
        correct_answer = self.question_answer_pairs[self.current_question_index - 1][1]
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect!", f"The correct answer was: {correct_answer}")
        self.next_question()

root = tk.Tk()
root.geometry("400x300")  # Set window size
my_quiz = Quiz(root)
root.mainloop()
