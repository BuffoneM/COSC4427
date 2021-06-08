import numpy as np

num_list = np.random.randint(1, 500, 3)
print(num_list)

largestInteger = np.max(num_list)
print("Largest:", largestInteger)

smallestInteger = np.min(num_list)
print("Smallest:", smallestInteger)

secLargestValue = num_list[(np.argsort(num_list)[-2:])[0]]
print("2nd largest:", secLargestValue)

secSmallestValue = num_list[(np.argsort(num_list)[1])]
print("2nd smallest:", secSmallestValue)

print(num_list)
total = np.sum(num_list)
avg = np.average(num_list)
print("Sum:", total, "\nAverage:", avg)

stdDev = np.std(num_list)
print("Standard deviation:", stdDev)

median = np.median(num_list)
print("Median:", median)

