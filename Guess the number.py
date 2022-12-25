# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

from tkinter import *
import math
import random

num_range = 100
remaining_guess = int(math.ceil(math.log(num_range,2)))
secret_number = random.randrange(0, num_range)
mode = "Normal Mode: "

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global remaining_guess
    global secret_number
    
    remaining_guess = int(math.ceil(math.log(num_range,2)))
    secret_number = random.randrange(0, num_range)
    # window.mainloop()
    
    print()
    print()
    print()
    print("New game:")
    print()
    print("Let's play, 'Guess the Number!'")
    print()
    print("   You have selected " + mode)
    print("   Select from a number from 0 to " + str(num_range - 1) + ":")
    print("   Number of remaining guesses is " + str(remaining_guess))
    

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    global mode
    
    num_range = 100
    mode = "Normal Mode: "
    
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    global mode
    
    num_range = 1000
    mode = "Hard Mode: "
    
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global remaining_guess
    
    print()
    print("Your guess is... " + guess)
        
    if (guess.isdigit() == True):
        
        if (int(guess) == secret_number):
            print("Correct!")
            print("Congratulations! You win!!!")
            new_game()
        elif (int(guess) > secret_number) and (int(guess) <= int(num_range-1)):
            remaining_guess -= 1
        
            if (remaining_guess > 0):
                print("Lower!")
                print("Chances = " + str(remaining_guess))
            elif remaining_guess == 0:
                print("Sorry, you have no more chances remaining.")
                print("You lose! Try again...")
                new_game()
            
        elif (int(guess) < secret_number) and (int(guess) <= int(num_range-1)):
            remaining_guess -= 1
        
            if (remaining_guess > 0):
                print("Higher!")
                print("Chances = " + str(remaining_guess))
            elif remaining_guess == 0:
                print("Sorry, you have no more chances remaining.")
                print("You lose! Try again...")
                new_game()

        else:
            print("Error! Not in range!")
            print("Enter a number from 0 to " + str(num_range - 1))
    
    else:
        print("Error! Input is not an Integer!")
        print("Enter an Integer from 0 to " + str(num_range - 1))


def main():
    # create frame
    window = Tk()
    window.title("Guess the Number!")
    window.geometry("200x200")

    # add buttons for range
    button1 = Button(window, text="Normal Mode(Range 0-100)", command=range100)
    button1.pack()

    button2 = Button(window, text="Hard Mode(Range 0-1000)", command=range1000)
    button2.pack()

    # Input text
    txt = Entry(window, width=10)
    txt.pack()
    txt.focus()

    def process(event=None):
        content = txt.get()  # get contents of entry widget
        input_guess(content)
        txt.delete(0, END)

    txt.bind('<Return>', process)

    # Set initial range
    range100()

    # start mainloop
    window.mainloop()


if __name__ == "__main__":
    main()


# always remember to check your completed program against the grading rubric
