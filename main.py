import random
from tkinter import *
import textwrap


def get_words():
    """collecting words from the txt file"""
    with open("words.txt", "r") as file:
        words_test = file.read().split("\n")
    random_string = ""
    """number of random words to be displayed"""
    n = 0
    while n < 100:
        random_string += f"{random.choice(words_test)} "
        n += 1
    """Tweaking the random_words strings so it fits in the canvas"""
    random_words = textwrap.fill(random_string, width=60)
    return random_words


current_words = get_words()


def start_timer(self):
    """configure the entry widget to allow input on click"""
    user_input.config(state=NORMAL)
    """sets timer to 60secs"""
    window.after(6000, func=calc_speed)


def calc_speed():
    global current_words
    """collects the user input and convert to a list. same for the text words"""
    input_list = list(user_input.get().split(" "))
    random_list = list(current_words.split(" "))
    """initialising list of words the users gets right or wrong"""
    wrong_words = []
    right_words = []
    """iterating through users input and test words for accuracy"""
    n = 0
    for word in input_list:
        if word == random_list[n] and n <= len(input_list) - 1:
            right_words.append(word)
            n += 1
        elif word != input_list[n]:
            wrong_words.append(word)
            n += 1
        elif word == input_list[-1]:
            n = 0
            word_bg.itemconfig(display_words, text=current_words)

    word_count = len(right_words)
    typing_speed = (word_count / 5) * 1
    instruction_label.destroy()
    user_input.destroy()
    speed_label = Label()
    word_bg.destroy()
    speed_label.config(text=f"Your typing speed is: {typing_speed} WPM"
                            f"\nYou got {len(right_words)}/{len(input_list) - 1}"f" right"
                            f"\nYou got {len(wrong_words)}/{len(input_list) - 1} wrong"
                       , bg="light blue", font=("Helvetica", 25))
    speed_label.grid(row=2, column=1)


def try_again():
    new_words = get_words()
    word_bg.itemconfig(display_words, text=new_words)


window = Tk()
window.title("Typing Speed App")
window.config(padx=100, pady=40, bg="DeepSkyBlue4")
window.geometry("900x600+50+50")

welcome_label = Label()
welcome_label.config(text="Hello!\nThis app calculates your typing speed per minute", bg="DeepSkyBlue4",
                     font=("Helvetica", 20, "bold"))
welcome_label.grid(row=0, column=1)

word_bg = Canvas(width=700, height=300, bg="light blue")
display_words = word_bg.create_text(350, 150, text=current_words, font=("Arial", 17, "italic"), fill="black")
word_bg.grid(row=1, column=1)

instruction_label = Label()
instruction_label.config(text="When you are ready start typing in the box below", bg="light gray",
                         font=("calibre", 15, "bold"))
instruction_label.grid(row=4, column=1)

user_input = Entry(font=("calibre", 10, "normal"), width=40, state=DISABLED)
user_input.grid(row=5, column=1, ipadx=60, ipady=5)
user_input.bind("<Button-1>", start_timer)
user_input.icursor(0)
user_input.focus()

try_again_button = Button(text="Try Again", highlightthickness=0, command=try_again())
try_again_button.grid(row=6, column=2)

exit_button = Button(window, text="Quit", highlightthickness=0, command=window.quit())
exit_button.grid(row=6, column=0)

window.mainloop()
exit(0)
