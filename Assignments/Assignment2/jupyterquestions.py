import random
import math

num_list = [random.randrange(1,500) for i in range(0, 50)]
#num_list = [5,4,3,2,1]         # Testing purposes
print(num_list)

largestValue = max(num_list)
print("Largest:", largestValue)

smallestValue = min(num_list)
print("Smallest:", smallestValue)

temp = list(num_list)
temp.remove(max(temp))
secLargestValue = max(temp)
print("2nd largest:", secLargestValue)

temp = list(num_list)
temp.remove(min(temp))
secSmallestValue = min(temp)
print("2nd smallest:", secSmallestValue)

print(num_list)
total = sum(num_list)
avg = (total) / (len(num_list))
print("Sum:", total, "\nAverage:", avg)

sum = 0
for num in num_list:
    sum += (num - avg) ** 2
variance = sum / (len(num_list))
stdDev = math.sqrt(variance)
print("Variance:", variance, "\nStandard deviation:", stdDev)

num_list.sort()
print("Sorted list:", num_list)
median = num_list[int((len(num_list) - 1) / 2)]
print("Median:", median)