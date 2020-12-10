"""Write another program that prompts for a list of numbers and at the end 
prints out both the maximum and minimum of the numbers instead of the average."""

max = None
min = None
while True:
    userIP = input("Enter a number")
    if userIP == 'Done' or userIP == 'DONE' or userIP =='done':
        break
    else:
        try:
            userIP = float(userIP)
        except:
            print("ENTER A VALID NUMBER")
            continue
    if max is None or userIP > max:
        max = userIP
    elif min is None or userIP < min:
        min = userIP
print(min)
print(max)