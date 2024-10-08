flag = False

value = int(input("Enter a number "))

for i in range (2,value):
    print (f"checking {i}")
    if value % i == 0:
        flag = True
        break

print (i)

if flag == True:
    print (f" {value} is not a prime - it can be divided by {i}")
    print (f" {value} divided by {i} is {(value/i)}")
else:
    print (f" {value} is a prime")


