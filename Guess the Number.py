def game():
    import random
    secretNumber = random.randint(0, 100)
    print("You have 10 chance to guess the number")
    print("Enter a number between 1-100")
    chances = 10
    usedChances = 0

    while chances > 0:
        userInput = int(input("Enter your number\n"))
        chances -= 1
        usedChances += 1
        if userInput < secretNumber:
            print("Increase you number")
        elif userInput == secretNumber:
            print("Correct guess ", secretNumber)
            print("Life used = ", usedChances)
            break
        else:
            print("Decrease your number")
        print("You have ", chances, "chance left")

    if usedChances == 10:
        print("Game Over!!!!")
    again()


def again():
    r = input('''To Play again Enter \'Y\' or to Exit \'E\'\n''')
    if r == "Y" or r == "y":
        game()
    elif r == "E" or r == "e":
        print("See you later")
        exit()
    else:
        print("Invalid Input")
    again()


game()
