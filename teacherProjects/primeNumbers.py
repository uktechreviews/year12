# Prime number project

print ("Enter a five digit value from 10000 to 99999")
valid = False

while valid != True:
    value = int(input())
    if value ==0:
        print ("try again")
        valid = False
    else:
        print (f"You picked the number {value}")
        valid = True

flag = False

for i in range (2,value-1):
    if value % i == 0:
        flag = True
        break

if flag == True:
    print (f"Sorry the number {value} is not a prime number")
else:
    print (f"Yay! The number {value} is a prime number")
    print ("Would you like to see all the prime numbers between 2 and your number [Yes or No]")
    answer = input().lower()
    if answer == "yes":
        for i in range (2,value):
            for j in range (2,i):
                flag = False
                if i%j ==0:
                    flag = True
                    break
            if flag == False:
                print (i)
    else:
        print ("have a nice day")




