import pandas as pd
import numpy as np

# P1: Count the number of characters.
def countChars(file):
    count = 0
    for line in file:
            for word in line.split():
                count += len(word)
    return count
    
# P2: Count the number of words (separated by whitespaces, tabs, and newlines characters).
def countWords(file):
    count = 0
    for line in file:
            for word in line.split():
                count += 1
    return count

# P3: Count the number of unique words (separated by whitespaces, tabs, and newlines characters).
def countUniqueWords(file):
    words = []
    for line in file:
        for word in line.split():
            words.append(word)
    return len(np.unique(words))

# P4: Count the number of lines.
def countLines(file):
    count = 0
    for line in file:
            count += 1
    return count

# P5: Find and print the longest word
def longestWord(file):
    words = []
    for line in file:
        for word in line.split():
            words.append(word)
    longest = max(words, key=len)       
    print("Longest word:", longest, "-", len(longest), "characters long")
    
# P6: Find and print the 10 most common words.
def mostCommon(file):
    words = []
    for line in file:
        for word in line.split():
            words.append(word)
    
    word, count = np.unique(words, return_counts = True)
    result = sorted(zip(count, word))
    print(result[-10:])

# P7: Find and print the 10 least common words.
def leastCommon(file):
    words = []
    for line in file:
        for word in line.split():
            words.append(word)
    
    word, count = np.unique(words, return_counts = True)
    result = sorted(zip(count, word))
    print(result[:10])

# P8: Count the number of words that begin with each English letter.
def startWithLetter(file):
    count = 0
    for line in file:
            for word in line.split():
                if word[0].isalpha():
                    count += 1
    return count

# P9: List unique words by each English letter.
def listByLetter(file):
    words = []
    for line in file:
        for word in line.split():
            words.append(word)
            
    uniqueWords = np.unique(words)
    for item in uniqueWords:
        if item[0].isalpha():
            print(item)

# P10: Count the number of digits.
def countDigits(file):
    count = 0
    for line in file:
            for word in line.split():
                for currChar in word:
                    if currChar.isdigit():
                        count += 1
    return count

# Codes of the loading "the_bible.txt" file goes here
fileName = "Assignment3/The_Bible.txt"
file = open(fileName, "r")

with open(fileName, "r") as file:
    print("Number of characters:", countChars(file))
with open(fileName, "r") as file:
    print("Number of words:", countWords(file))
with open(fileName, "r") as file:
    print("Number of unique words:", countUniqueWords(file))
with open(fileName, "r") as file:
    print("Number of lines:", countLines(file))
with open(fileName, "r") as file:
    longestWord(file)
with open(fileName, "r") as file:
    print("Most common words:")
    mostCommon(file)
with open(fileName, "r") as file:
    print("Least common words:")
    leastCommon(file)
with open(fileName, "r") as file:
    print("Words that start with letters:", startWithLetter(file))
with open(fileName, "r") as file:
    print("Unique words that start with only English letters:")
    listByLetter(file)
with open(fileName, "r") as file:
    print("The number of digits as characters are:", countDigits(file))