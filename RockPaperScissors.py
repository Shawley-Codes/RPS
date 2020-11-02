#6/3/2019
#Scott Hawley 
#Rock, Paper Scissors

#import all modules to be used
import random


#larger loop, allows replayability, if not exit code
playAgain = "y"
while playAgain == "y":
    
    #Get a number of games the user wants to play then validate
    print("\nWelcome to the Rock Paper Scissors game. Can you beat the bot?")
    numGames = int(input("To start, please enter a best of how many games you want to play: "))

    #ensure number is odd, then 
    while (numGames % 2) == 0:
        print("Invalid input, please enter an odd number.\n")
        numGames = int(input("Please enter a best of how many games you want to play: "))
        
    #reset variables
    winNeeded = numGames/2
    numWins = 0
    numLoss = 0
    #define quit, then use for loop condition
    quit = "n"
    while quit == "n":
    
        #get user input for either rock, paper or scissers; then validate
        print("\nIt is time! Rock! Paper! Scissors!")
        userChoice = str(input("Please enter either r, p or s: "))
        
        #validate whether it is one of the 3 input choices, then correct if needed
        while userChoice != "r" and userChoice != "p" and userChoice != "s":
            userChoice = input("Invalid answer, Please enter either r,p or s: ")
        
        #computer chooses random response
        computerChoice = random.randint(1,3)

        #determine and print winner
        #add to scores, and dertime if there is a final winner
        if userChoice == "r":
            print("\nYou chose Rock!\n")
            if computerChoice == 1:
                print("Your opponent chose Rock! Tie, again!")
            if computerChoice == 2:
                print("Your opponent chose Paper! You lose!")
                numLoss += 1
            if computerChoice == 3:
                print("Your opponent chose Scissors! You Win!")
                numWins += 1
        elif userChoice == "p":
            print("\nYou chose Paper!\n")
            if computerChoice == 1:
                print("Your opponent chose Rock! You Win!")
                numWins += 1
            if computerChoice == 2:
                print("Your opponent chose Paper! Tie, again!")
            if computerChoice == 3:
                print("Your opponent chose Scissors! You Lose!")
                numLoss += 1
        else:
            print("\nYou chose Scissors!\n")
            if computerChoice == 1:
                print("Your opponent chose Rock! You lose!")
                numLoss += 1
            if computerChoice == 2:
                print("Your opponent chose Paper! You Win!")
                numWins += 1
            if computerChoice == 3:
                print("Your opponent chose Scissors! Tie, again!")

        print("\nWins: ", numWins, "\nLoss: ", numLoss)
                      
        #if there is a final winner, congradulate and print, then check for replay
        if numWins > winNeeded:
            print("\n\nCongratualtions, you Won with ", numWins, " win and ", numLoss, " losses!")
            quit = "y"
        elif numLoss > winNeeded:
            print("\n\nYou lost with ", numWins, " win and ", numLoss, " losses.")
            quit = "y"
                      
    #Check if user wishes to play again, then validate
    playAgain = input("Do you want to play again? y or n: ")
    while playAgain != "y" and playAgain != "n":
        playAgain = input("Invalid, please enter y or n: ")
    
                

  




