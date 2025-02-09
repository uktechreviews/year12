def hashWord(word):
    value = 0
    for letter in word:
        value = value + (ord(letter))
        hash = value % maxRecords
    return hash

maxRecords = 11
records = ["","","","","","","","","",""]

sentence = "Hello my name is spencer"
count = 0
words = sentence.split()

for word in words:
    value = hashWord(word)
    records[count] = value
    count = count +1

print (words)
print (records)

