# --------------- IMPORTS ---------------------#
import json
import random
from tkinter import *

# --------------- CONSTANTS ---------------------#
BACKGROUND_COLOR = "#B1DDC6"
WHITE_BACKGROUND_COLOR = "#ffffff"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

# --------------- GLOBAL VARIABLES ---------------------#
data_list = []


# --------------- LOOPING QUESTIONS ---------------------#
def next_question():
    if len(data_list):
        info = random.choice(data_list)
        canvas.delete("all")
        canvas.create_image(400, 263, image=card_front)
        canvas.create_text(400, 150, text="French", fill="black", font=LANGUAGE_FONT)
        canvas.create_text(400, 263, text=info[0], fill="black", font=WORD_FONT)
        window.after(5000, count_down, info)


# --------------- COUNTER MANAGER ---------------------#
def count_down(word_list):
    canvas.delete("all")
    canvas.create_image(400, 263, image=card_back)
    canvas.create_text(400, 150, text="English", fill="white", font=LANGUAGE_FONT)
    canvas.create_text(400, 263, text=word_list[1], fill="white", font=WORD_FONT)


# --------------- WINDOW MANAGEMENT ---------------------#
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Define the Photo Images to use in the window
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")

# Define the canvas for the image
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)
canvas.create_image(400, 263, image=card_front)

language_text = canvas.create_text(400, 150, text="Title", fill="black", font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 263, text="Word", fill="black", font=WORD_FONT)

# Define the Buttons
wrong_btn = Button(image=wrong, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=next_question)
wrong_btn.grid(row=1, column=0)

right_btn = Button(image=right, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=next_question)
right_btn.grid(row=1, column=1)

# --------------- FILE MANAGEMENT ---------------------#

try:
    data_file = open("./data/french_words.csv")
except FileNotFoundError:
    canvas.itemconfig(
        word_text,
        text="Be sure you got the french_words.csv\n in your data folder before continuing",
        font=LANGUAGE_FONT
    )
    canvas.itemconfig(language_text, text="Unable to open file")
    right_btn.config(state=DISABLED)
    wrong_btn.config(state=DISABLED)
else:
    data = json.load(data_file)
    data_list = [[row, data["English"][index]] for index, row in data["French"].items()]
    next_question()

window.mainloop()
