# COSC4427A Midterm Question 1
# Michael Buffone

import numpy as np
# [1, 4, 18, 5], [1, 3, 4], [9, 2, 6]

userInput = input("Sample input: ")
userInput = userInput.replace("[", "")
userInput = userInput.replace("]", "")
userInput = userInput.replace(",", "")
userInput = userInput.split()

for i in range(len(userInput)):
    userInput[i] = int(userInput[i])
userInput.sort()

print("One sorted list:", userInput)
print("Unique elements:", np.unique(userInput))
uniqueElements, count = np.unique(userInput, return_counts = True)
result = sorted(zip(uniqueElements, count))
print("Frequency:", result)
