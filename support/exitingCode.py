# Examples for exiting code


# quit() can be used when you are developing projcects but don't use in final production

for i in range (1,10,2):
    print (i)
    if i == 7:
        print ("Ending the program")
        quit()

# exit() can be used in a similar way to quit() and again should not be used in final production

for i in range (1,10,2):
    print (i)
    if i == 7:
        print ("Ending the program")
        exit()

# sys.exit() is a better choice to use for production code.  You will need to use the sys 
# module which is always available

import sys
for i in range (1,10,2):
    print (i)
    if i == 7:
        print ("Ending the program")
        sys.exit("The program has ended cleanly")

