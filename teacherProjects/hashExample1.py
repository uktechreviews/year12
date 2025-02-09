key = 0
maxRecords = 11

while key != -1:
    key = int(input("Enter your key "))
    if key == -1:
        break
    address = key % maxRecords
    print (address)

