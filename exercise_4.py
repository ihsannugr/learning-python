#Exercise 4

#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

#input number
num = int(input("Please insert a number: "))

#create list of number up to num 
x = range(1, num + 1)

#create new element which consists of all num's divisor
res = []
res = [elem for elem in x if num % elem == 0]

#print result element
print("The divisor of " + str(num) + " is " + str(res))
