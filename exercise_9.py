#Exercise 9

#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

#Extras:

#1. Keep the game going until the user types “exit”
#2. Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

num = random.randint(1, 9)
playgame = True

print("Welcome to Guess Number Game!\n")

while playgame == True :
    
    attempt = 0
    guess = 0

    while guess != num :
        
        guess = int(input("Guess the Number (1-9) : "))
    
        if guess == num :
            attempt += 1
            print("\nCorrect! the number is " + str(num))
            print("attempt : " + str(attempt) + "\n") 
            continue       
        elif guess < num and guess > 0 :
            print("Too Low.\n")
            attempt += 1
        elif guess > num and guess < 10 :
            print("Too High.\n")
            attempt += 1  
        elif guess < 1 or guess > 9 :
            print("Please guess 1-9 only.\n")      

    exit = str(input("exit game(y/n)?\n"))
    
    if exit == "y" :
        playgame = False
        print("\nThanks for playing. -Ihsan Nugraha\n")
    elif exit == "n" :
        print("\nGood Luck.\n")
    else :
        print("\nWrong input. I guess you want to play again. Good Luck.\n")
