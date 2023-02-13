"""program to output the integers from 20 to 25 inclusive and their sum.
"""

# initialise variables
lowest = int(20)
highest = int(25)
total = 0

# for loop of range of lowest to highest
for i in range(lowest, highest + 1):
    total = total + i
    i = i + 1
    # print all numbers below the highest
    if i <= highest:
            print("", i)
# print the total of the numbers in range
print(total)
