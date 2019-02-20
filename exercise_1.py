#Exercise-1

#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

#Extra: 
#1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
#2. Print out that many copies of the previous message on separate lines.

#import datetime
import datetime

#input name (string) and age (integer)
name = input('Tell me your name: ')
age = int(input('Tell me your age: '))

#get the current time
now = datetime.datetime.now()

#calculate the age difference
yrs = 100 - age

#show when that person turn 100 years old
res = 'Hi ' + name + ', you will turn 100 years old in ' + str(now.year+yrs)
print(res)

#input any number and create a number copies of previous message
num = int(input('Input any number of result copies: '))
for x in range(num):
    print(res)

