""" Write program to find the maximum and minimum of the numbers from the list of number."""
count = 0
numbers = [999, 5, 1, 7, 3, 0]
sum = 0
smallest = None
largest  = None
for number in numbers:
    sum = sum + number
    count = count + 1
    if largest is None or number > largest :
        largest = number
    elif smallest is None or number < smallest:
        smallest = number
print("Smallest of the above number is",smallest)
print("Largest of the above number is",largest)
print("Number of items are ", count)    
print("Sum of all numbers", sum)
print("Average ", sum/count)
print("Done")