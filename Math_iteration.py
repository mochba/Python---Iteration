# Write a program which repeatedly reads numbers until the user enters 
# “done”. Once “done” is entered, print out the total, count, and average of the 
# numbers. If the user enters anything other than a number, detect their mistake using 
# try and except and print an error message and skip to the next number.

sum = 0 
count = 0 
while True :
	useri = input("Enter a number:")
	if useri == 'Done' or useri == 'DONE' or useri == 'done' :
		break
	else:
		try:
			u = float(useri)
		except:
			print("Enter a valid number!!!!")
			continue
		count = count + 1
		sum  = sum + u
		ave   = sum/count                        
print("Sum of number :",sum)        
print("Count of number :",count)        
print("Average of number :",ave)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              