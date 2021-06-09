import numpy as np

num_list = np.random.randint(1, 500, 50)
#num_list = [5,4,3,2,1]         # Testing purposes
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

variance = np.var(num_list)
stdDev = np.std(num_list)
print("Variance:", variance, "\nStandard deviation:", stdDev)

median = np.median(num_list)
print("Median:", median)