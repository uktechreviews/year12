def hashWord(word):
    value = 0
    for letter in word:
        value = value + (ord(letter))
        hash = value % wordCount
    return hash



sentence = "Hello my name is Spencer Organ"
count = 0
words = sentence.split()
wordCount = len(words)

print (f"Word Count: {wordCount}")
records = []

for record in range(0,wordCount):
    records.append("")
print (records)

for word in words:
    value = hashWord(word)
    records[count] = value
    count = count +1

print (words)
print (records)

