import numpy as np

num_list = np.random.randint(1, 500, 10)
print(num_list)

largestInteger = np.max(num_list)
print(largestInteger)

smallestInteger = np.min(num_list)
print(smallestInteger)

secLargestValue = num_list[(np.argsort(num_list)[-2:])[0]]
print("2nd largest:", secLargestValue)

secSmallestValue = num_list[(np.argsort(num_list)[1])]
print("2nd smallest:", secSmallestValue)



#print(num_list)
#total = sum(num_list)
#avg = total/len(num_list)
#print("Sum:", total, "\nAverage:", avg)

#stdDev = 0
#print("Standard deviation:", stdDev)

#print("Sorted list:", num_list)
#median = 0
#print("Median:", median)

