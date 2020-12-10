#Adam Wolff
#Section 13
#Email:adamkwolff@hotmail.com
#Date:11/10/13
#Name of Program:The game of don't match
#Purpose: A virtual game using a 6 sided die. User will select if they want to
#keep playing or if they would like to walk away with the amount of money they
#have won.
#Preconditions:The user will select if they would like to roll again or not.
#Postconditions: The game will accumulate their money they win until the user
#selects something other than yes or if they get the same roll as their first roll.

#import random
from random import *

#import graphics
from graphics import*

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
#Purpose: To call whichever picture that is associated with the same number
#assigned to roll.
#Postconditions: Returns the name of the correct photo that should diplay.
#Design:
def display_die (roll):
            if roll == 1:#If roll variable is equal to 1:
                        return "one.gif"#return "one.gif"
            if roll == 2:#If roll variable is equal to 2:
                        return "two.gif"#return "two.gif"
            if roll == 3:#If roll variable is equal to 3:
                        return "three.gif"#return "three.gif"
            if roll == 4:#If roll variable is equal to 4:
                        return "four.gif"#return "four.gif"
            if roll == 5:#If roll variable is equal to 5:
                        return "five.gif"#return "five.gif"
            if roll == 6:#If roll variable is equal to 6:
                        return "six.gif"#return "six.gif"            
                        
def main():
            #Step 1: Draw the graph.
            win = GraphWin("Don't Match!!", 700, 550)
            
            #Step 1.2: Set the Coords.
            win.setCoords(0,0, 699, 549)
            
            #Step 2: Assign a an integer between 1 and 6 using the get_a_roll
            #function and assign it to the variable "roll"
            roll = get_a_roll()
            
            #Step 3: Assign the same value to the variable "firstRoll"
            firstRoll=roll
            
            #Step 4: Draw the title of the game.
            title1 = Text(Point(375, 500),"The game of 'Don't Match'")
            title1.setStyle('bold')
            title1.draw(win)
            
            #Step 5: Turn firstRoll into a string.
            firstRoll=str(firstRoll)
            
            #Step 6: Display the first roll text.
            title2 = Text(Point(380, 400),(("Your first roll is ")+ firstRoll))
            title2.setStyle('bold')
            title2.draw(win)                       
            
            #Step 7: Display the firstroll picture.
            pic1 = Image(Point(100,400), display_die(roll))
            pic1.draw(win)            
            
            #Step 8: Display the rules of the game
            title3 = Text(Point(380, 375),(("You can roll as long as you don't roll another ")+ firstRoll))
            title3.setStyle('bold')
            title3.draw(win)            
            
            #Step 9: Display how much money they have.
            title4 = Text(Point(380, 350),(("You have $")+ firstRoll))
            title4.setStyle('bold')
            title4.draw(win)
            
            #Step 10: Display how much money they won from the previous roll.
            title5 = Text(Point(380, 50),(("You won $")+ firstRoll))
            title5.setStyle('bold')
            title5.draw(win)
            
            #Step 11: Display text that asks if they would like to roll again.
            title6 = Text(Point(380, 325),"Do you want to roll again?")
            title6.draw(win)             
            
            #Step 12: Create an accumulator so the total theyve won will display.
            total = 0
            
            #Step 13: Create an accumulator so the game won't end the game on
            #the first round.
            iteration = 0
            
            #Step 14: Set the flag "gameOver" equal to False
            gameOver=False
            
            #Step 15: Set title8 equal to text and draw it so it can be undrawn
            #later in the loop without a problem.
            title8 = Text(Point(380, 350),(""))
            title8.draw(win)
            
            #Step 16: Set title9 equal to text and draw it so it can be undrawn
            #later in the loop without a problem.                              
            title9 = Text(Point(380, 50),(""))
            title9.draw(win)
            
            #Step 17: Create a box for the user to click yes.
            yesBox = Rectangle(Point(295,100), Point(370,175))
            yesBox.draw(win)
            
            #Step 18: Create text inside the box that says "YES"
            yesboxTitle = Text(Point(332,137), "YES")
            yesboxTitle.setStyle('bold')
            yesboxTitle.draw(win) 
            
            #Step 19: Creates a boc for the user to click no.
            noBox = Rectangle(Point(390,100), Point(465,175))
            noBox.draw(win)
            
            #Step 20: Create text inside the boc that says "YES"             
            noboxTitle = Text(Point(427,137), "NO")
            noboxTitle.setStyle('bold')
            noboxTitle.draw(win)            
            
            #Step 21:Create a while loop that says while gameOver does not equal
            #true then continue.
            while gameOver!=True:
                
                #Step 21.1: Add one to iteration each time.
                iteration+=1               
                
                #Step 21.2: Get a mouse click from the user
                click=win.getMouse()
                
                #Step 21.3: Assign the X and Y coordinates of the mouse click in
                #the variable "clickX" and "clickY"
                clickX=click.getX()
                clickY=click.getY()
                
                #Step 21.4: Decide whether the mouse click was inside the "YES"
                #box or if it was outside of the box.
                if clickX > 295 and clickX < 370:
                            x = "yes"
                else:
                            x = "no"
                                    
                if clickY > 100 and clickY < 175:
                            y = "yes"
                else:
                            y = "no"
            
                #Step 21.5: If the mouse click was inside the box playAgain will
                #be equal to "y" otherwise it will be "n"
                if x == "yes" and y == "yes":
                            playAgain="y"
                else:
                            playAgain="n"
                
                #Step 21.5: Turn firstRoll into an integer            
                firstRoll=int(firstRoll)
                    
                #Step 21.6: If playAgain is equal to "y" then roll will be
                #assigned a new value using the get_a_roll function
                if playAgain=="y":
                            roll = get_a_roll()
                
                #Step 21.7: If playAgain is equal to no then"           
                if playAgain=="n":
                              yesBox.undraw()#undraw the yes box
                              yesboxTitle.undraw()#undraw the yes
                              noBox.undraw()#undraw the no box
                              noboxTitle.undraw()#undraw the no                              
                              title4.undraw()#undraw text
                              title9.undraw()#undraw text
                              title6.undraw()#undraw text
                              title5.undraw()#undraw text
                              earnings=total+firstRoll#total up the earnings
                              earnings=str(earnings)#turn earnings into a string.
                              title7 = Text(Point(380, 35),(("You left with $")+ earnings))#display the earnings.
                              title7.setStyle('bold')
                              title7.draw(win)
                              title12 = Text(Point(380, 10),("Click to exit"))#display the click to exit text.
                              title12.setStyle('bold')
                              title12.draw(win)                              
                              
                              #set gameOver equal to True
                              gameOver=True
                
                #Step 21.8: If the current roll does not equal the firstroll
                #and gameOver does not equal True then:
                if roll!=firstRoll and gameOver!=True:
                              title4.undraw()#undraw text
                              title5.undraw()#undraw text
                              title8.undraw()#undraw text
                              title9.undraw()#undraw text
                              pic4 = Image(Point(100,100), "blank.gif")#Display a blank picture to cover up the old picture.
                              pic4.draw(win)
                              pic2 = Image(Point(100,100), display_die(roll))#Display the new picture of the die roll.
                              pic2.draw(win) 
                              
                              #add the value of roll to the total accumulator.  
                              total+=roll
                              
                              #accumulate the earnings and turn that varible into a string.
                              earnings=str(total+firstRoll)
                              #turn roll into a string and assign it to the varible stringRoll
                              stringRoll=str(roll)
                              
                              #Display the earnings.
                              title8 = Text(Point(380, 350),(("You have $")+ earnings))
                              title8.setStyle('bold')
                              title8.draw(win)
                              
                              #Display the amount won off of the last roll.
                              title9 = Text(Point(380, 50),(("You won $")+ stringRoll))
                              title9.setStyle('bold')
                              title9.draw(win)
                
                #Step 21.9: If their current roll is equal to their first roll and the iteration
                #accumulator is larger than 1 then:
                if roll==firstRoll and iteration >1:
                              yesBox.undraw()#undraw the yes box
                              yesboxTitle.undraw()#undraw the yes
                              noBox.undraw()#undraw the no box
                              noboxTitle.undraw()#undraw the no                             
                              title4.undraw()#undraw text
                              title5.undraw()#undraw text
                              title6.undraw()#undraw text
                              title9.undraw()#undraw text                             
                              pic4 = Image(Point(100,100), "blank.gif")#Display a blank picture to cover up the old picture.
                              pic4.draw(win)                              
                              pic3 = Image(Point(100,100), display_die(roll))#Display the new picture of the die roll.
                              pic3.draw(win)
                              title10 = Text(Point(380, 60),("Sorry!"))#Display "Sorry!"
                              title10.setStyle('bold')
                              title10.draw(win)
                              title11 = Text(Point(380, 35),("You matched! You lost all your money!"))#Display "You matched! 
                              #You lost all your  money!"
                              title11.setStyle('bold')
                              title11.draw(win)
                              title12 = Text(Point(380, 10),("Click to exit"))#Display "Click to exit"
                              title12.setStyle('bold')
                              title12.draw(win)                              

                              gameOver=True#Set gameOver equal to True
            
            #Step 22: Wait for a mouse click
            win.getMouse()
            
            #Step 23: Close the program.
            win.close()                
                        
main()