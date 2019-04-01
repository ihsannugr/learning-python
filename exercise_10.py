#Exercise 10

#Take two lists, say for example these two:

#	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension.

#Extra: Randomly generate two lists to test this

import random

samplerange = int(input("Insert range limit of the List : "))
samplesize_a = int(input("Insert size limit of the List 1 : "))
samplesize_b = int(input("Insert size limit of the List 2 : "))

a = random.sample(range(samplerange), samplesize_a)
b = random.sample(range(samplerange), samplesize_b)
c = []

c = [elem for elem in a if elem in b and elem not in c]

print("List 1 = " + str(a))
print("List 2 = " + str(b))
print("Common value(s) = " + str(c))



