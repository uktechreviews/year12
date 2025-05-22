#Cipher project
#Verman cipher

import random

from colorama import Fore, Back, Style

#range of printing ASCII characters = 32 - 128

def printCharacters():
    for i in range (32,127,1):
        print (i, chr(i))

def plainText():
    print (Fore.BLACK)
    print ("Enter your plain text message ")
    print ("Warning: This will be displayed on the screen ")
    print (Fore.RED + "*** Watch out for shoulder surfers ***")
    print (Fore.BLACK)
    valid = False
    while valid != True:
        plainTextMessage = input("[Plain Text Message] ")
        if plainTextMessage == "":
            print (Fore.RED + "Empty string detected - try again" + Fore.BLACK)
        else:
            print (Fore.GREEN + "Plain text accepted" + Fore.BLACK)
            return plainTextMessage
            valid = True

def generateKey(plainTextMessage):
    lenOfKey = len(plainTextMessage) * 2
    key = ""
    for count in range (0,lenOfKey,1):
        randomValue=random.randrange(32,127)
      #  print (randomValue,chr(randomValue))
        key = key + chr(randomValue)
    print ("*** Key generated ***")
    return key

def generateCipher(plainTextMessage,key,type):
    cipher = ""
    binary = ""
    for count in range (0,len(plainTextMessage)):
        character = bin(ord(plainTextMessage[count])  ^ ord(key[count]))
        binary = binary + (character[2:]) + " "
        cipher = cipher + chr(int(character[2:]))
    if type == True:
        return binary
    else:
        return cipher



plainTextMessage = plainText()
key = generateKey(plainTextMessage)
cipher = generateCipher(plainTextMessage,key,False)
print (cipher)

