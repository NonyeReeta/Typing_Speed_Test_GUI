from tkinter import *


def start_timer(self):
    window.after(6000, func=calc_speed)


def calc_speed():
    user_text = user_input.get()
    word_list = []
    for char in user_text:
        word_list.append(char)
    word_count = len(word_list)
    typing_speed = (word_count / 5) * 1
    instruction_label.destroy()
    user_input.destroy()
    speed_label = Label()
    speed_label.config(text=f"Your typing speed is: {typing_speed} WPM", bg="light blue", font=("Helvetica", 25))
    speed_label.grid(row=3, column=1)


def save_name():
    username = user_name.get()
    welcome_label.destroy()
    name_label.destroy()
    user_name.destroy()
    name_button.destroy()
    new_label = Label()
    new_label.config(text=f"Hi {username}", bg="light blue", font=("Helvetica", 15))
    new_label.grid(row=2, column=1)

window = Tk()
window.title("Typing Speed App")
window.config(padx=50, pady=50, bg="light blue")
window.geometry("600x400")

welcome_label = Label()
welcome_label.config(text="Hello!\nThis app calculates your typing speed per minute", bg="light blue",
                     font=("Helvetica", 15, "bold"))
welcome_label.grid(row=0, column=1)

name_label = Label()
name_label.config(text="Enter your name:", bg="light blue", font=("Helvetica", 15))
name_label.grid(row=2, column=1)

user_name = Entry(width=40)
user_name.grid(row=3, column=1)
user_name.icursor(0)
user_name.focus()

name_button = Button(text="Enter", width=5, command=save_name)
name_button.grid(row=3, column=2)

instruction_label = Label()
instruction_label.config(text="When you are ready start typing in the box below", bg="light blue",
                         font=("Helvetica", 15, "bold"))
instruction_label.grid(row=4, column=1)

user_input = Entry(font=("calibre", 10, "normal"), width=40)
user_input.grid(row=5, column=1, ipadx=40, ipady=30)
user_input.bind("<Button-1>", start_timer)
user_input.icursor(0)
user_input.focus()

window.mainloop()
