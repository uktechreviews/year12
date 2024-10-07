import math
import time

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    colors = [PURPLE,CYAN,DARKCYAN,BLUE,GREEN,YELLOW,RED]

coins = ["one pence", "two pence", "five pence", "ten pence", "twenty pence", "fifty pence", "one pound", "two pound"]
value = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2]

end = [0] * len(coins) 

total = 0
index = 0
while index < len(coins):
    print ("")
    print (" How many",color.YELLOW,coins[index],color.END,"coins do you have?")
    no_coins = int(input(" ")) 

    number = no_coins * value[index]
    total = total + number  
    index = index + 1
    print(color.DARKCYAN,"Total so far:",color.END,"£",round(total, 2))  
    print ("-"*40)

total = round(total, 2)  
print(color.RED,"Your total is:",color.END,color.BOLD,color.UNDERLINE,"£",total,color.END)
print ("-"*40)
print ("")


spend = float(input("How much would you like to spend? "))
if spend > total:
    print("You do not have enough coins to spend that amount.")
    more = spend - total
    more = round(more,2)
    print ("You need", color.CYAN, "£",more,color.END, "more to spend the amount of",color.PURPLE,"£",spend, color.END)
    print ("")
    enough = False
else:
    total = total - spend
    time.sleep(1)
    print ("")
    print ("Processing . . .")
    time.sleep(1)
    print ("")
    total = round(total, 2)
    print("£",spend, "has been spent")
    print ("")
    time.sleep(0.5)
    print("You now have £",total,"left")
    print ("")
    enough = True

index2 = len(value) - 1  
while total > 0 and index2 >= 0:
    count = 0
    while total >= value[index2]:  
        total = total - value[index2]
        total = round(total, 2) 
        count = count + 1
    end[index2] = count  
    index2 = index2 - 1

type = 0
if enough == True:
    for i in range(len(coins)):
        if end[i] > 0:
            print ((color.colors[type]),(end[i]),"x",(coins[i]),color.END)
            time.sleep(0.5)
            type = type + 1
