from PIL import Image, ImageTk, ImageDraw
import random
import tkinter as tk
# from tkinter import messagebox

window = tk.Tk()
window.title("Rock Paper Scissor game")
window.minsize(width=1000,height=800)

choices = ["rock","paper","scissor"]
images = {}

for choice in choices:
    try:
        imag = Image.open(f"{choice}.jpg").resize((100,100))
    except FileNotFoundError:
        imag = Image.new('RGB',(100,100),color='gray')
        d = ImageDraw.Draw(imag)
        d.text((10,40),choice,fill=(255,255,255))
    #imag = Image.open(f"{choice}.jpg").resize((100,100))
    images[choice] = ImageTk.PhotoImage(imag)


user_label = tk.Label(window)
user_label.pack(side='left',padx=50,pady=20)
comp_label = tk.Label(window)
comp_label.pack(side='right',padx=50,pady=20)
user_score_label = tk.Label(window)
user_score_label.pack(side='left',padx=100,pady=40)
comp_score_label = tk.Label(window)
comp_score_label.pack(side='right',padx=100,pady=40)
result_label = tk.Label(window,text=" ",font=("Arial",24))
result_label.pack(pady=20)

comp_score = 0
user_score = 0


def play(user_choice):
    global comp_score
    global user_score
    comp_choice = random.choice(choices)
    if user_choice == comp_choice:
        result = "It's draw"
    elif (user_choice == 'rock' and comp_choice == 'scissor') or \
            (user_choice ==  'paper' and comp_choice == 'rock') or \
            (user_choice == 'scissor' and comp_choice == 'paper'):
        result = 'You win'
        user_score += 1
    else:
        result = "Computer win"
        comp_score += 1

    user_label.config(image=images[user_choice])
    user_label.image = images[user_choice]
    comp_label.config(image=images[comp_choice])
    comp_label.image = images[comp_choice]
    result_label.config(text=result)
    user_text = f"You scored {user_score} points"
    comp_text = f"Computer scored {comp_score} points"
    user_score_label.config(text=user_text)
    comp_score_label.config(text=comp_text)

button_frame = tk.Frame(window)
button_frame.pack(side='top',pady=20)

for choice in choices:
    btn = tk.Button(button_frame,text=choice.capitalize(),command=lambda c=choice:play(c))
    btn.pack(side='left',padx=10)



window.mainloop()