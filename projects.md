# Example coding activities
## From Mr Organ

> [!TIP]
Use these examples when you have a free lesson or want to practice programming

### Activity 1 Random number code breaker

- [ ] Ask the user to enter a random three digit number from 111 to 999
- [ ] Generate randon numbers in the range 111 to 999 and check to see if it matches
- [ ] Print out the final code number

**Stretch**
- [ ] Count how many times the random number was generated before it cracked it

**Super stretch**
- [ ] Append the random number to a list and if it has already been checked. Don't try it again

___

### Activity 2 Bingo grid

- [ ] Create a 2d array of 4 columns and 2 rows
- [ ] Populate the array with random numbers from 1 to 99
- [ ] Display the grid
- [ ] Generate a random number between 1 and 99. Tell the user
what number is being called.
- [ ] Check to see if the number is on the grid. If it is 
replace it with a 'X'
- [ ] Once all 8 numbers have been matched display 'Bingo' and 
end the game 

___

### Activity 3 username 

- [ ] Ask for the user's first name
- [ ] Ask for the user's second name
- [ ] Ask for the user's year of birth (4 digits eg 1975)
- [ ] Generate a username based on the last two digits of the year of birth, the first two letters from their first name and the first three letters of the surname.


> [!TIP]
You can extract a range of letters from a string using

```
string = "Elephant"
string = string[0:3] # This will only keep the index value 0,1,2
```
You also might find some of these [String handling methods](https://www.w3schools.com/python/python_ref_string.asp) useful.

___

### Activity 4 Random word generators

- [ ] Create three lists, each containing 20 random words
- [ ] Generate three random words, one from each list
- [ ] Create a new word by concatinating the three random words, one from each list

> [!TIP] 
There are a couple of different ways you can approach this. One method would be to use random.choice()

```
import random
list = ["Cat" , "Dog" , "Fish"]
word =random.choice(list)
```
___

### Activity 5 Key word jumble

- [ ] Ask the user for a word of more than 5 letters
- [ ] Check the length of the word
- [ ] Take each letter of the word and add it to a list
- [ ] Pick a randon number in the range 0, length of word
- [ ] If the letter is a vowel replace with a * otherwise replace with a £
- [ ] Repeat until all the letters are replaced
- [ ] If the same letter is picked more than once replace with a %

___

### Activity 6 Binary sort

> [!TIP]
You will need to have a sorted list before you can do a binary search

- [ ]   Create a list of 10 numbers (in numberical order)
``` 
list = [1, 5, 27, 89, 125, 256, 257, 300, 310, 320]
```
- [ ]    Pick a random number from the list
- [ ]    Carry out a binary search
- [ ]    Output the index position of the number you searched from