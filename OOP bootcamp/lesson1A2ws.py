books = [] 

 

print("What is the title of the first book?") 

book1 = input() 

book1 = book1.capitalize() 

index = 0 

for book in books: 

  if book[0] < book1[0]: 

    index = index + 1 

books.insert(index, book1) 

 

print("What is the title of the second book?") 

book2 = input() 

book2 = book2.capitalize() 

index = 0 

for book in books: 

  if book[0] < book2[0]: 

    index = index + 1 

books.insert(index, book2) 

 

print("What is the title of the third book?") 

book3 = input() 

book3 = book3.capitalize() 

index = 0 

for book in books: 

  if book[0] < book3[0]: 

    index = index + 1 

books.insert(index, book3) 

 

print("Your alphabetical collection is...") 
print (books)