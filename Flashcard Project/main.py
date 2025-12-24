import random
from tkinter import *
import pandas as pd

''' 
This is a Flashcard Capstone Project - Animal and its Baby name. 
Used button to reveal the baby name line no 36,37, 75 to 77 shall be commented for a normal flash card. 
'''

BACKGROUND_COLOR = "#B1DDC6"
random_dict = {}

try:
    to_learn_data = pd.read_csv("data/to_learn_animal_and_baby_names.csv")
except FileNotFoundError:
    full_data = pd.read_csv("data/animal_and_baby_names.csv")
    data_dict_list = full_data.to_dict(orient="records")
else:
    data_dict_list = to_learn_data.to_dict(orient="records")


def show_animal_card():
    global random_dict,flip_timer
    window.after_cancel(flip_timer)
    random_dict = random.choice(data_dict_list)
    canvas.itemconfig(animal_card,image=front_image)
    canvas.itemconfig(animal_title, text="Animal",fill="black")
    canvas.itemconfig(animal_name,text=random_dict["Animal"],fill='black')
    flip_timer = window.after(5000, func=show_baby_card)

def show_baby_card():
    canvas.itemconfig(animal_card, image=back_image)
    canvas.itemconfig(animal_title, text="Baby",fill='white')
    canvas.itemconfig(animal_name,text="")

def	reveal_ans():
    canvas.itemconfig(animal_name,text=random_dict["Baby Name"],fill='white')

def save_to_learn():
    data_dict_list.remove(random_dict)
    pd.DataFrame(data_dict_list).to_csv("data/to_learn_animal_and_baby_names.csv",index=False)
    show_animal_card()



window = Tk()
window.minsize(300, 300)
window.title("Animal FlashCard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(5000, func=show_baby_card)


front_image = PhotoImage(file="images/card_front.png").subsample(2,2)
back_image = PhotoImage(file="images/card_back.png").subsample(2,2)

canvas = Canvas(window, width=800, height=526, background=BACKGROUND_COLOR,highlightthickness=0)
animal_card = canvas.create_image(400,263, image=front_image)
animal_title = canvas.create_text(400, 155, text="", font=("Tahoma", 40, "bold"),fill="black")
animal_name = canvas.create_text(380, 250, text="", font=("Tahoma", 40),fill="black")
canvas.grid(row=0, column=0, columnspan=2)


#Correct or wrong button
right_image = PhotoImage(file="images/right.png").subsample(2,2)
wrong_image = PhotoImage(file="images/wrong.png").subsample(2,2)

wrong_btn = Button(window, image=wrong_image,highlightthickness=0,borderwidth=0)
wrong_btn.config(command=show_animal_card)
wrong_btn.grid(row=1, column=0)

correct_btn = Button(window, image=right_image,highlightthickness=0,borderwidth=0)
correct_btn.config(command=save_to_learn)
correct_btn.grid(row=1, column=1)

show_answer = Button(window, text="Click to reveal",width=30)
show_answer.config(command=reveal_ans)
show_answer.grid(row=1, column=2)

show_animal_card()






window.mainloop()


