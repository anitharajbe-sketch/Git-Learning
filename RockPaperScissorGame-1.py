import random
from tkinter import *

user_score = 0
comp_score = 0
count = 0

choices = ['rock', 'paper', 'scissor']
image = {}


window = Tk()
window.title("Rock Paper Scissor Game")
window.minsize(width=400, height=400)



def set_game_gui():
    global user_label, user_score_l, comp_label, comp_score_l, result_label, count
    count = 0

# Labels for user image, comp image, score, result
    user_label = Label(window)
    user_label.pack(side='left', padx=50, pady=20)
    comp_label = Label(window)
    comp_label.pack(side='right', padx=50, pady=20)
    result_label = Label(window)
    result_label.pack(side='top')
    user_score_l = Label(window)
    user_score_l.config(text=" ", font=('Arial', 20))
    user_score_l.pack(side='left', padx=30, pady=30)
    comp_score_l = Label(window)
    comp_score_l.config(text=" ", font=('Arial', 20))
    comp_score_l.pack(side='right', padx=30, pady=30)

    for choice in choices:
        if choice == 'paper':
            x, y = 10, 10
        else:
            x, y = 5, 5
        image[choice] = PhotoImage(file=f"{choice}.png").subsample(x, y)

    button_frame = Frame(window)
    button_frame.pack(side='top', pady=10)

    clear_button = Button(text='End game')
    clear_button.config(command=stop_game)
    clear_button.pack(side='bottom', padx=10, pady=10)

    for choice in choices:
        new_image = image[choice]
        button = Button(button_frame, image=new_image, command=lambda c=choice: play(c))
        button.pack(side='left', padx=10)


def start_game():
    global count
    count = 0
    stop_game()
    set_game_gui()


def play(user_choice):
    global user_score, comp_score, count
    count += 1
    if count < 10:
        comp_choice = random.choice(choices)
        if comp_choice == user_choice:
            result = "It's draw"
        elif (user_choice == 'scissor' and comp_choice == 'paper') or \
                (user_choice == 'rock' and comp_choice == 'scissor') or \
                (user_choice == 'paper' and comp_choice == 'rock'):
            result = "You win"
            user_score += 1
        else:
            result = "Computer win"
            comp_score += 1
        user_label.config(image=image[user_choice])
        comp_label.config(image=image[comp_choice])
        result_label.config(text=result, font=('Arial', 25, 'bold'))
        user_score_l.config(text=f"Score: {user_score} points")
        comp_score_l.config(text=f"Score: {comp_score} points")
    else:
        stop_game()
        show_results()


def show_results():
    global user_score, comp_score
    if user_score > comp_score:
        new_text = f"You are the winner"
    elif comp_score > user_score:
        new_text = f"Computer is the winner"
    else:
        new_text = "It's draw"

    Label(window,
          text=new_text,
          font=("Arial", 30, 'bold')).pack(side='top')

    start_text = Button(window)
    start_text.config(text='New game', command=start_game)
    start_text.pack(side='bottom',padx=100,pady=100)
    user_score = 0
    comp_score = 0

def stop_game():
    for widgets in window.winfo_children():
        widgets.destroy()


# to start the game for the first time
set_game_gui()

window.mainloop()
