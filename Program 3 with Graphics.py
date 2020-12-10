from random import *
from graphics import*

def get_a_roll():
            return randrange(1,7)


def display_die (roll):
            if roll == 1:
                        return "one.gif"
            if roll == 2:
                        return "two.gif"
            if roll == 3:
                        return "three.gif"
            if roll == 4:
                        return "four.gif"
            if roll == 5:
                        return "five.gif"
            if roll ==6:
                        return "six.gif"            
                        
def main():
            win = GraphWin("Don't Match!!", 700, 550)
            win.setCoords(0,0, 699, 549)
            
            roll = get_a_roll()
            firstRoll=roll
            
            title1 = Text(Point(375, 500),"The game of 'Don't Match'")
            title1.setStyle('bold')
            title1.draw(win)
            
            firstRoll=str(firstRoll)
            
            title2 = Text(Point(380, 400),(("Your first roll is ")+ firstRoll))
            title2.setStyle('bold')
            title2.draw(win)                       
            
            pic1 = Image(Point(100,400), display_die(roll))
            pic1.draw(win)            
            
                      
            
            #print("You can roll as long as you don't roll another", firstRoll)
            title3 = Text(Point(380, 375),(("You can roll as long as you don't roll another ")+ firstRoll))
            title3.setStyle('bold')
            title3.draw(win)            
            #print("You have $", firstRoll)
            title4 = Text(Point(380, 350),(("You have $")+ firstRoll))
            title4.setStyle('bold')
            title4.draw(win)
            
            title5 = Text(Point(380, 50),(("You won $")+ firstRoll))
            title5.setStyle('bold')
            title5.draw(win)
            
            title6 = Text(Point(380, 325),"Do you want to roll again?")
            title6.draw(win)             
            
            total = 0
            iteration = 0
            
            gameOver=False
            title8 = Text(Point(380, 350),(""))
            title8.draw(win)
                              
            title9 = Text(Point(380, 50),(""))
            title9.draw(win)
            
            yesBox = Rectangle(Point(295,100), Point(370,175))
            yesBox.draw(win)
            
            yesboxTitle = Text(Point(332,137), "YES")
            yesboxTitle.setStyle('bold')
            yesboxTitle.draw(win) 
            
            noBox = Rectangle(Point(390,100), Point(465,175))
            noBox.draw(win)
                            
            noboxTitle = Text(Point(427,137), "NO")
            noboxTitle.setStyle('bold')
            noboxTitle.draw(win)            
            
            while gameOver!=True:
                
                iteration+=1               
                
                click=win.getMouse()
                clickX=click.getX()
                clickY=click.getY()
                
                if clickX > 295 and clickX < 370:
                            x = "yes"
                else:
                            x = "no"
                                    
                if clickY > 100 and clickY < 175:
                            y = "yes"
                else:
                            y = "no"
                            
                if x == "yes" and y == "yes":
                            playAgain="y"
                else:
                            playAgain="n"
                            
                firstRoll=int(firstRoll)
                    
                       
                if playAgain=="y":
                            roll = get_a_roll()
                            
                if playAgain=="n":
                              yesBox.undraw()
                              yesboxTitle.undraw()
                              noBox.undraw()
                              noboxTitle.undraw()                              
                              title4.undraw()
                              title9.undraw()
                              title6.undraw()
                              title5.undraw()
                              earnings=total+firstRoll
                              earnings=str(earnings)
                              title7 = Text(Point(380, 35),(("You left with $")+ earnings))
                              title7.setStyle('bold')
                              title7.draw(win)
                              title12 = Text(Point(380, 10),("Click to exit"))
                              title12.setStyle('bold')
                              title12.draw(win)                              
                              
                              gameOver=True
                            
                if roll!=firstRoll and gameOver!=True:
                              title4.undraw()
                              title5.undraw()
                              title8.undraw()
                              title9.undraw()
                              pic4 = Image(Point(100,100), "blank.gif")
                              pic4.draw(win)
                              pic2 = Image(Point(100,100), display_die(roll))
                              pic2.draw(win) 
                                
                              total+=roll
                              
                              earnings=str(total+firstRoll)
                              stringRoll=str(roll)
                              
                              title8 = Text(Point(380, 350),(("You have $")+ earnings))
                              title8.setStyle('bold')
                              title8.draw(win)
                              
                              title9 = Text(Point(380, 50),(("You won $")+ stringRoll))
                              title9.setStyle('bold')
                              title9.draw(win)
                        
                if roll==firstRoll and iteration >1:
                              yesBox.undraw()
                              yesboxTitle.undraw()
                              noBox.undraw()
                              noboxTitle.undraw()                              
                              title4.undraw()
                              title5.undraw()
                              title6.undraw()
                              title9.undraw()                              
                              pic4 = Image(Point(100,100), "blank.gif")
                              pic4.draw(win)                              
                              pic3 = Image(Point(100,100), display_die(roll))
                              pic3.draw(win)
                              title10 = Text(Point(380, 60),("Sorry!"))
                              title10.setStyle('bold')
                              title10.draw(win)
                              title11 = Text(Point(380, 35),("You matched! You lost all your money!"))
                              title11.setStyle('bold')
                              title11.draw(win)
                              title12 = Text(Point(380, 10),("Click to exit"))
                              title12.setStyle('bold')
                              title12.draw(win)                              

                              gameOver=True
            win.getMouse()
            win.close()                
                        
main()