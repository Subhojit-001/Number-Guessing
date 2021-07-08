Developing "number guessing game" step by step
Programming Language used is  "Python"

Let's develop the "Guess game". Its rules are as follows:

Computer proposes a number from 1 to 100.
Human player tries to guess it. One enters a guess and computer tells if the number matches or it is smaller/greater than the proposed one.
Player will have 10 chances to guess the correct number.
Program will show how many guess has been taken and how many chances are left if wrong guess have been taken


Step 1: Secret Number
To propose a secret number, we declare a variable secretNumber of type int and use random function to give it random value in range 1..100.
import random
secretNumber = random.randint(0, 100)


Step 2: Initializing Number of Chances
Under a function, we declare a variable chances of type int and usedChances of type int to initialize the number of chances left and number of chances used.
def game():
    print("You have 10 chance to guess the number")
    chances = 10
    usedChances = 0
    
    
Step 3: Asking user for a guess
In order to get input from user, we declare another variable guess of type int. while is used so that user get 10 chance to guess the correct number.

while chances > 0:
    userInput = int(input("Enter your number\n"))
    
    
Step 4: Checking if the guess is right and calculating number chances used and left
Now let's check if human player's guess is right. If so program should print corresponding message. Otherwise, tell user that a guess is smaller/greater than the proposed number. To test the program let's try all three cases (remember that we peeked the secret number). And subtracting the value of chances and increasing the value of  usedChances.

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
    
    
Step 5: again() function
again() function is used so that program continue after the user guess the correct answer, if user want to continue the user choose Y/y or want to exit the game type E/e.

def again():
    r = input('''To Play again Enter \'Y\' or to Exit \'E\'''')
    if r == "Y" or r == "y":
        game()
    elif r == "E" or r == "e":
        print("See you later")
    else:
        print("Invalid Input")
    again()


game()
