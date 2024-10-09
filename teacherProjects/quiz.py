print ("My Quiz")
score = 0


print ("Q1. What does CPU stand for? ")
answer = input()
if answer == "Central Processing Unit":
    print ("Correct")
    score = score +5
else:
    print ("Wrong")
    score = score -2


print (score)

