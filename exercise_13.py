#Exercise 13

#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.
	
def fibonacci() :
	numbers = int(input("Insert numbers of Fibonacci generated : "))
	i = 1	
	fibo = [0, 1]
	if numbers < 1 :
		fibo = []
	elif numbers == 1 :
		fibo = [0]
	elif numbers == 2 :
		fibo = [0, 1]
	else :
		while i != (numbers - 1) :
			fibo.append(fibo[i] + fibo[i - 1])
			i += 1
		
	return fibo


while 1 == 1 :
	print(fibonacci())
