#Exercise 3

#write a program that prints out all the elements of the list that are less than 5.

#Extras:
#1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#2. Write this in one line of Python.
#3. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

#create lists
sourcelist = [1 ,1 ,2 ,3 ,5 ,8 ,13 ,21 ,34 ,55 ,89]
newlist = []

#insert element less than 5 from sourcelist to newlist using list comprehension
newlist = [element for element in sourcelist if element < 5]
        
print(newlist)

#clear newlist
newlist.clear()

#insert element less than a number from sourcelist to newlist using list comprehension
num = int(input("Please insert a number: "))

newlist = [element for element in sourcelist if element < num]

print("This is a list of elements that less than " + str(num) + " : " + str(newlist))
