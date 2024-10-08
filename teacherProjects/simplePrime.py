# value = int(input("Enter a number "))

for n in range (111111,99999999999):
    flag = False
    for i in range (2,n):
        #print (f"checking {i}")
        if n % i == 0:
            flag = True
            break

    if flag!=True:
        print (f" {n} is a prime")


