import tkinter
import random
from tkinter import messagebox as msg

class Application(object):
    def __init__(self):
        self.root = root = tkinter.Tk()
        root.title("Elementary Math")
        root.geometry("600x400+200+100")
        self.setup()
    
    def setup(self):
        self.addition_frame = tkinter.Frame(self.root)
        self.addition_frame.place(relx=0,rely=0, relwidth=1, relheight=1)
        self.numbers_ = ""
        self.number_1 = tkinter.IntVar()
        self.number_2 = tkinter.IntVar(value=random.randint(0, 20))
        self.set_number_1()
        self.answer = tkinter.IntVar()
        self.operand = tkinter.StringVar(value="+")
        self.operand_text = tkinter.StringVar(value="Addition")
        label_cnf = {
            "font": ("courier", 18),
            "bd": 2
            }
        entry_cnf = {
            "font": ("courier", 18),
            "bd": 2
            }
        button_cnf = {
            "font": ("courier", 18),
            "bg": "#00ff00",
            "fg": "#ffffff",
            "cursor": "hand2",
            "relief": "raised"
        }
        tkinter.Label(self.addition_frame, textvariable=self.operand_text, cnf=label_cnf).place(relx=0.0, rely=0.0, relwidth=1, relheight=0.1)
        tkinter.Label(self.addition_frame, textvariable=self.number_1, cnf=label_cnf).place(relx=0.4, rely=0.2, relwidth=0.3, relheight=0.1)
        tkinter.Label(self.addition_frame, textvariable=self.number_2, cnf=label_cnf).place(relx=0.4, rely=0.35, relwidth=0.3, relheight=0.1)
        tkinter.Label(self.addition_frame, textvariable=self.operand, cnf=label_cnf).place(relx=0.3, rely=0.35, relwidth=0.1, relheight=0.1)
        self.answer_entry = tkinter.Entry(self.addition_frame, textvariable=self.answer, cnf=entry_cnf)
        self.answer_entry.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)
        tkinter.Button(self.addition_frame, text="Submit", command=self.calculate, cnf=button_cnf).place(relx=0.3, rely=0.7, relwidth=0.4, relheight=0.1)
        tkinter.Button(self.addition_frame, text="Change", command=self.change_operand).place(relx=0.9, rely=0.9, relwidth=0.1, relheight=0.1)
    
    def change_operand(self, event=True):
        self.operand.set("+" if self.operand.get() == "-" else "-")
        self.operand_text.set("Addition" if self.operand.get() == "+" else "Subtraction")
        
    def calculate(self, event=True):
        try:
            answer = self.answer.get()
        except:
            msg.showerror("Value error", "Invalid text entered for anwser")
            return
        correct_answer = eval(f"{self.number_1.get()}{self.operand.get()}{self.number_2.get()}")
        if answer != correct_answer:
            hint = "small" if correct_answer > answer else "big"
            msg.showerror("Incorrect answer", f"You answer: {answer} is too {hint}!")
            self.answer.set(0)
            return
        
        msg.showinfo("Correct", f"Well done\t:\n{self.number_1.get()} {self.operand.get()} {self.number_2.get()} = {answer}\nCongratulations")
        self.set_number_1()
        self.number_2.set(random.randint(0, 20))
        self.answer.set(0)
        self.answer_entry.focus_set()
    
    def set_number_1(self):
        while self.number_1.get() < self.number_2.get():
            self.number_1.set(random.randint(0, 20))
        
        
        
    def run(self):
        self.root.mainloop()

def main():
    app = Application()
    app.run()

if __name__ == "__main__":
    main()