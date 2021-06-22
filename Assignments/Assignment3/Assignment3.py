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
    wordDictionary = []
    for line in file:
        for word in line.split():
            wordDictionary.append(word)
    wordSeries = pd.Series(wordDictionary)
    return len(pd.Series(wordDictionary).unique())

# P4: Count the number of lines.
def countLines(file):
    count = 0
    for line in file:
            count += 1
    return count

# P5: Find and print the longest word
def longestWord(file):
    return 0
    
# P6: Find and print the 10 most common words.
def mostCommon(file):
    return 0

# P7: Find and print the 10 least common words.
def leastCommon(file):
    return 0

# P8: Count the number of words that begin with each English letter.
def startWithLetter(file):
    return 0

# P9: List unique words by each English letter.
def listByLetter(file):
    return 0

# P10: Count the number of digits.
def countDigits(file):
    return 0

# Codes of the loading "the_bible.txt" file goes here
fileName = "Assignment3/test.txt"
file = open(fileName, "r")

with open(fileName, "r") as file:
    print("Number of characters:", countChars(file))
with open(fileName, "r") as file:
    print("Number of words:", countWords(file))
with open(fileName, "r") as file:
    print("Number of unique words:", countUniqueWords(file))
with open(fileName, "r") as file:
    print("Number of lines:", countLines(file))
