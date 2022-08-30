from tkinter import *
import random
import os


attempts = 10
number = round(random.uniform(1, 10), 1)


def check(event):
    global attempts
    global text

    attempts -= 1

    guess = float(entry_window.get())

    if number == guess:
        text.set("You win ! Congrats !!!\n Correct Number " + str(number))
        btn_check.pack_forget()
        btn_Play.pack()

    elif attempts == 0:
        text.set("Game Over !!!\nNumber is " + str(number))
        text1.set("Retry")
        btn_check.pack_forget()
        btn_Play.pack()

    elif guess < number:
        text.set("Increase your guess !\nChance Left  " + str(attempts) + "\nLast Choice " + str(entry_window.get()))
        entry_window.delete(0, END)

    elif guess > number:
        text.set("Decrease your number !\nChance Left  " + str(attempts) + "\nLast Choice " + str(entry_window.get()))
        entry_window.delete(0, END)

    return


def play():
    root.destroy()
    os.popen("NumberGuessing.py")


root = Tk()

root.title("Guess the number")

root.geometry("500x150")
label = Label(root, text="Guess the Number 1 to 10")
label.pack()

entry_window = Entry(root, width=40, borderwidth=4)
entry_window.pack()

btn_check = Button(root, text="Press Enter", command=check)
btn_check.pack()

root.bind('<Return>', check)

text1 = StringVar()
text1.set("Play Again")

btn_Play = Button(root, textvariable=text1, command=play)

btn_quit = Button(root, text="QUIT", command=root.destroy)
btn_quit.pack()

text = StringVar()
text.set("You have 10 attempt remaining! Good Luck!!!")

guess_attempts = Label(root, textvariable=text)
guess_attempts.pack()

root.mainloop()
