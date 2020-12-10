#Adam Wolff
#Section 13
#Email:adamkwolff@hotmail.com
#Date:11/4/13
#Name of Program:The game of don't match
#Purpose: A virtual game using a 6 sided die. User will select if they want to
#keep playing or if they would like to walk away with the amount of money they
#have won.
#Preconditions:The user will select if they would like to roll again or not.
#Postconditions: The game will accumulate their money they win until the user
#selects something other than yes or if they get the same roll as their first roll.

#import random
from random import *

#get_a_roll
#Preconditions: None
#Purpose: To greturn a random number between 1 and 6
#Postconditions: Returns a number 1-6 including 1 and 6.
#Design:
def get_a_roll():
            return randrange(1,7)#1.Returns a random number between 1 and 6

#display_die
#Preconditions: The parameters for this will be a number associated with roll
#which is a variable that contains an integer between 1 and 6
#Purpose: To call whichever function that is associated with the same number
#assigned to roll.
#Postconditions: Calls a function( either one() two() three() four() five() or
#six() ) depending on what integer is assigned to the roll variable.
#Design:
def display_die (roll):
            if roll == 1:#If roll variable is equal to 1:
                        one()#call one()
            if roll == 2:#If roll variable is equal to 2:
                        two()#call two()
            if roll == 3:#If roll variable is equal to 3:
                        three()#call three()
            if roll == 4:#If roll variable is equal to 4:
                        four()#call four()
            if roll == 5:#If roll variable is equal to 5:
                        five()#call five()
            if roll ==6:#If roll variable is equal to 6:
                        six()#call six()

#functions one through six
#Preconditions: None
#Purpose: To print a card that resembles a die face in the shell.
#Postconditions: Prints a card in the shell when called upon by the display_die
#function.
def one():
    
    print("+---+")
    print("|   |")
    print("| * |")
    print("|   |")
    print("+---+")
    

def two():
    
    print("+---+")
    print("|  *|")
    print("|   |")
    print("|*  |")
    print("+---+")
    

def three():
    
    print("+---+")
    print("|  *|")
    print("| * |")
    print("|*  |")
    print("+---+") 
    


def four():
    
    print("+---+")
    print("|* *|")
    print("|   |")
    print("|* *|")
    print("+---+") 


def five():
    
    print("+---+")
    print("|* *|")
    print("| * |")
    print("|* *|")
    print("+---+")
    


def six():
    
    print("+---+")
    print("|* *|")
    print("|* *|")
    print("|* *|")
    print("+---+")
    
#main
#Preconditions: none
#Purpose: To play the match game.
#Postconditions: The user will paly the game and will either leave with their
#winnings or they will lose it all.

def main():
    #Step 1. Show introduction.       
    print("")

    print("The game of 'Don't Match'")
    
    print("")
    
    #Step 2. Get a number between 1 and 6 using the get_a_roll function and
    #assign it to the variable "roll".
    roll = get_a_roll()
    #Step 3. Asssign the number of the first roll to the variable "firstRoll"
    firstRoll=roll
    #Step 4.Output to the shell what their first roll was.
    print(("Your first roll is "), firstRoll)
    #Step 5. Display the die corresponding to that roll.
    display_die(roll)
    
    #Step 6.Output to the shell the rules and how much money they have.
    print("You can roll as long as you don't roll another", firstRoll)
    print("You have $", firstRoll)
    #Step 7. Set the accumulaters total and iteration equal to zero.
    total = 0
    iteration = 0
    
    #Step 8. Set the flag "gameOver" equal to FALSE
    gameOver=False
    
    #Step 9. Start a while loop that says while the flag is still true.
    while gameOver!=True:
        
        #Step 9.1 Ask the user if they would like to roll again and assign their
        #response to the variable playAgain.
        print("")
        playAgain=input("Would you like to roll again? (y/n)")
        
        #Step 9.2 add 1 to iteration.
        iteration+=1
        
        #Step 9.3 Create an if statement that says if they answer y or Y for
        #playAgain then you will get a new roll.
        if playAgain=="y" or playAgain=="Y":
            roll = get_a_roll()
        
        #Step 9.4 Create an if statement that says if they answer anything other
        #than y or Y then to tell them how much money they left with and assigns
        #True to gameOver which ends the loop and the game.
        if playAgain!="y" and playAgain!="Y":
            print("You left with $", total+firstRoll)
            gameOver=True
        
        #Step 9.5 Create an if statement that says if their game is not over and
        #their roll isnt equal to their first roll then display the dice, add
        #the roll to the total accumulator  and print out how much money they
        #won and how much money they have.
        if roll!=firstRoll and gameOver!=True:
            
            display_die(roll)
                
            total+=roll
            print("You Won $", roll)
            print("You now have $", firstRoll+total)
        
        #Step 9.6 Create an if statement that says if roll is equal to the first
        #roll and the iteration accumulator is more than 1 then display the die
        #they rolled, print "You Lose", and assign True to gameOVER to jump out
        #of the loop and end the game.
        if roll==firstRoll and iteration >1:
                    display_die(roll)
                    print("You lose")
                    gameOver=True
    k=input("Press Enter to Exit:")
main()
    
