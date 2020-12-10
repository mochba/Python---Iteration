
while True:
    userinput = input(">")
    if userinput[0] == '#':
        continue
    if userinput == 'Done' or 'done' or 'Done':
        break
    print(userinput)
print("Good Job")

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

# Print the sum of the numbers and its average in the list, smallest number and 
# largest number from the list

count = 0
numbers = [4,6,5]
sum = 0
smallest = None
largest  = None
for number in numbers:
    sum = sum + number
    count = count + 1
    if smallest is None or smallest > number:
        smallest = number
    if largest is None or largest < number:
        largest = number
    print("My number is", number)
print("Smallest of the above number is",smallest)
print("Largest of the above number is",largest)
print("Number of items are ", count)    
print("Sum of all numbers", sum)
print("Average ", sum/count)
print("Done")