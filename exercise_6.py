#Exercise 6

#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

#input word
word = input("Please input a word: ")

#create reverse of word
reverse = word[::-1]

#word comparison
if word == reverse :
    print("the word is palindrome.")
else :
    print("the word isn't palindrome.")
