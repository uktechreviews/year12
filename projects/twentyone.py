## The counting game 
## The objective is get to 21
print ("The counting to 21 game")
print ("--- -------- -- -- ----")
print ("\n Rules")
print ("\n")
print ("1. Player 1 starts with the number 1, you can then say either 1 or 2")
print ("2. Player 2 starts with the next number after player 1 and then can their say +1 or +2")
print ("3. Repeat until you get to 21")

win = False
total = 0

def checkValid(number):
    if number >=1 and number <=2:
        return True
    else:
        return False
    
def checkWin(total):
    if total == 21:
        return True
    else:
        return False

while win != True:
    player1 = int(input("Player 1: Enter a number between 1 and 2 "))
    if checkValid(player1) == True:
        total = total + player1
        print (f"The total is {total}")
        if checkWin(total) == True:
            print ("Player 1 Wins")
            winner = "player 1"
            win = True
            break
    else:
        print ("Not a valid number - you forefit yor go")

    player2 = int(input("Player 2: Enter a number between 1 and 2 "))
    if checkValid(player2) == True:
        total = total + player2
        print (f"The total is {total}")
        if checkWin(total) == True:
            print ("Player 2 Wins")
            win = True
            winner = "player 2"
    else:
        print ("Not a valid number - you forefit your go")

print (f"Game Over! - Well done {winner}")
    
