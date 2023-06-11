import re
knownwords = ""
with open("wordsiknow.txt", "r", encoding="utf8") as book:
    knownwords = book.read()
knownwords = knownwords.split("\n")

text = ""
with open("HarryPotter1.txt", "r", encoding="utf8") as book:
    text = book.read()

# Remove characters that are not part of the Spanish alphabet or spaces
text = re.sub(r'[^a-zA-ZáéíóúñüÁÉÍÓÚÑÜ ]', '', text)
text = text.lower()

for word in knownwords:
    text = text.replace(" " + word + " ", " ")
text = text.split(" ")

# print(set(text))

from collections import Counter
counts = Counter(text)
dictionaryBook = dict(counts)

sorted_dict = dict(sorted(dictionaryBook.items(), key=lambda item: item[1]))
wordsToLearn = list(sorted_dict.keys())
wordsToLearn.reverse()
print(wordsToLearn)

with open("VocabularyLists/HarryPotter1Words.txt", "w", encoding="utf8") as outFile:
    outFile.write(', '.join(wordsToLearn))

