# --------------- IMPORTS ---------------------#
from tkinter import *

# --------------- CONSTANTS ---------------------#
BACKGROUND_COLOR = "#B1DDC6"
WHITE_BACKGROUND_COLOR = "#ffffff"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

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
canvas.create_image(400, 263, image=card_back)

language_text = canvas.create_text(400, 150, text="Title", fill="black", font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 263, text="Word", fill="black", font=WORD_FONT)

# Define the Buttons
wrong_btn = Button(image=wrong, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0)
wrong_btn.grid(row=1, column=0)

right_btn = Button(image=right, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0)
right_btn.grid(row=1, column=1)

window.mainloop()
