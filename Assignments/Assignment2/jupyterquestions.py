import random
import math

num_list = [random.randrange(1,500) for i in range(0, 3)]
print(num_list)

largestValue = max(num_list)
print("Largest:", largestValue)

smallestValue = min(num_list)
print("Smallest:", smallestValue)

temp = max(num_list)
num_list.remove(max(num_list))
secLargestValue = max(num_list)
print("2nd largest:", secLargestValue)
num_list.append(temp)

temp = min(num_list)
num_list.remove(min(num_list))
secSmallestValue = min(num_list)
print("2nd smallest:", secSmallestValue)
num_list.append(temp)

print(num_list)
total = sum(num_list)
avg = total/len(num_list)
print("Sum:", total, "\nAverage:", avg)

sum = 0
for num in num_list:
    sum += (num - avg) ** 2
stdDev = math.sqrt(sum / (len(num_list)))
print("Standard deviation:", stdDev)

num_list.sort()
print("Sorted list:", num_list)
median = num_list[int((len(num_list) - 1) / 2)]
print("Median:", median)