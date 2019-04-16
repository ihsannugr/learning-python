#Exercise 12

#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

import random

def create_list(length) :
	listname = random.sample(range(1000), length)
	return listname
	
def filter_list(listname) :
	listresult = []
	listresult.append(listname[0])
	listresult.append(listname[-1])
	return listresult
	
def print_result(listname) :
	result = filter_list(listname)	
	print("Random List : \n")	
	print(listname)
	print("\nFirst & Last Elements of List : \n")
	print(result)

print_result((create_list(10)))
