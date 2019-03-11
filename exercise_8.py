#Exercise 8

#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

playgame = "yes"

print("Welcome to Rock-Paper-Scissor Game.\n")

while playgame == "yes" :

    player_1 = str(input("Player 1 (rock / scissor / paper) : "))
    player_2 = str(input("Player 2 (rock / scissor / paper) : "))

    if player_1 == player_2 :
        print("\nDraw. Try Again!\n")

    elif player_1 == "rock" :
        if player_2 == "scissor" :
            print("\nPlayer 1 win. Congrats!\n")
        elif player_2 == "paper" :
            print("\nPlayer 2 win. Congrats!\n")
        else :
            print("\nWrong choice, Player 2! Please choose between rock / scissor / paper\n")

    elif player_1 == "scissor" :
        if player_2 == "paper" :
            print("\nPlayer 1 win. Congrats!\n")
        elif player_2 == "rock" :
            print("\nPlayer 2 win. Congrats!\n") 
        else :
            print("\nWrong choice, Player 2! Please choose between rock / scissor / paper\n")

    elif player_1 == "paper" :
        if player_2 == "rock" :
            print("\nPlayer 1 win. Congrats!\n")
        elif player_2 == "scissor" :
            print("\nPlayer 2 win. Congrats!\n")
        else :
            print("\nWrong choice, Player 2! Please choose between rock / scissor / paper\n")

    else :
        print("\nWrong choice, Player 1! Please choose between rock / scissor / paper\n")
    

    playgame = str(input("Do you want to play again? (yes/no)\n"))       
    if playgame == "no" :
        print("\nGame Over.\n")
        break
