import random
from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}

try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer=window.after(3000, func=flip_card)


def flip_card():

    canvas.itemconfig(card_background, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"])

def is_known():
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn", index=False)
    next_card()
window=Tk()
window.title("Flashyy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer =  window.after(3000, func=flip_card)




canvas=Canvas(height=526, width=800)
card_front=PhotoImage(file="images/card_front.png")
card_back=PhotoImage(file="images/card_back.png")
card_background=canvas.create_image(400,263,image=card_front)
card_title=canvas.create_text(400,150, text="", font=("Ariel", 40, "italic"))
card_word=canvas.create_text(400,263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_img=PhotoImage(file="images/wrong.png")
unknown_button=Button(image=wrong_img, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

right_img=PhotoImage(file="images/right.png")
known_button=Button(image=right_img, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()
window.mainloop()


