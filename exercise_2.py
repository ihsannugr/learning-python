#Exercise_2

#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

#Extra
#1. If the number is a multiple of 4, print out a different message.
#2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

#input number
num = int(input("Please input a number: "))

#check whether the number is odd or even. If even, check if the number is multiple of 4 or not
if num%2 == 0:
    print(str(num) + " is even.")
    if num%4 == 0:
        print(str(num) + " is multiple of 4.")
else:
    print(str(num) + " is odd.")

pass

#input number and divider
check = int(input("Please input a number: "))
div = int(input("Please input a divider: "))

#check whether a number can evenly divisible by another number 
if check % div == 0:
    print(str(check) + " is evenly divisible by " +str(div))
else:
    print(str(check) + " is not evenly divisible by " +str(div))







