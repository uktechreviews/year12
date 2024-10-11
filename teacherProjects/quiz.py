print ("My Quiz")
score = 0


######
print ("Q1. What does CPU stand for? ")
print ("Hint: ")
answer = input()
if answer == "Central Processing Unit":
    print ("Correct")
    score = score +5
else:
    print ("Wrong")
    score = score -2
######

print ("What is ROM \n A: Read only memory \n B: Read or memory \n C: Random access memory")
answer = input()
if answer == "A":
	print ("Correct")
	score = score + 5
else:
	print ("You are wrong")
	score = score -2

######

print ("Does a gaming computer need a big or small amount of RAM")
answer = input():
if answer == "big":
	print ("Correct")
	score = score + 10
else:
	print ("Incorrect")
	score = score - 5

######


if score > 30:
	print ("You are amazing")
elif score >10 or score <29:
	print ("You are good")
else:
	print ("Try harder next time")


