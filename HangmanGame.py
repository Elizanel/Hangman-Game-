#Final Project
#Elizanel Martinez Moquete  
#Resoures: 
#https://www.geeksforgeeks.org/time-functions-in-python-set-1-time-ctime-sleep/
#https://www.w3schools.com/python/python_for_loops.asp
#https://www.w3schools.com/python/python_conditions.asp
#https://www.youtube.com/watch?v=UEO1B_llDnc
#https://inventwithpython.com/invent4thed/chapter8.html

import random
import time

# asking user for name, personalized welcome:
print("\nWelcome to The UALBANY THEMED Hangman Game\n")
username = input("Enter your name: ")
print("Hello " + username + "! Have Fun & Good Luck!")
time.sleep(1)
print("Remember all words are UALBANY THEMED")
print("Are You Ready?!\n Let's play!")
time.sleep(2)
 #what is needed to play hangman 
def foundation():
    global count
    global display
    global theword
    global user_guesses
    global lengthofword
    global play_game
    words_in_game = ["campuscenter","damien","greatdane","jamalschicken","acadamiens","lecturecenter","books","homework","bus","collinscircle"
                   ,"sefcu"]
    theword = random.choice(words_in_game)
    lengthofword = len(theword)
    count = 0
    display = '_' * lengthofword
    user_guesses = []
    play_game = ""
#Ask user to play again, if not- quit 
def replay_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        foundation()
    elif play_game == "n":
        print("I hope you had fun playing Hangman.")
        exit()
#how the actual game works 
def hangmangame():
    global count
    global display
    global theword
    global user_guesses
    global play_game
    limit = 7
    theguess = input("The Hangman Word: " + display + " Enter your first letter guess: \n")
    theguess = theguess.strip()
    if len(theguess.strip()) == 0 or len(theguess.strip()) >= 2 or theguess <= "9":
        #doesnt let user input number 
        print("Invalid Input, Try a letter\n")
        hangmangame()
#if the letter being inputed is correct fond it in the line and place it there
    elif theguess in theword:
        user_guesses.extend([theguess])
        index = theword.find(theguess)
        theword = theword[:index] + "_" + theword[index + 1:]
        display = display[:index] + theguess + display[index + 1:]
        print(display + "\n")
        
    elif theguess in user_guesses:
        print("Not Quite! Try another letter!.\n")
#shows the user where they are in the game and how many tries they have 
    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Nope! " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |       \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Sorry!. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     |\n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Think a Little Harder " + str(limit - count) + " guesses remaining\n")

        elif count == 5:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     |\n"
                 "  |     O\n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("C'mon you can do this! " + str(limit - count) + " guesses remaining\n")

        elif count == 6:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     |\n"
                 "  |     O\n"
                 "  |    /|\ \n"
                 "  |      \n"
                 "__|__\n")
           print("Oh No! " + str(limit - count) + " guesses remaining\n")

        elif count == 7:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     |\n"
                 "  |     O\n"
                 "  |    /|\ \n"
                 "  |    / \ \n"
                 "__|__\n")
                 #shows the user the letters tehy were missing 
           print("Wrong!!! You lost! Maybe Next Time! \n")
           print("The word Correct letters were:",theword)
           print("Together: ", user_guesses, theword)
  
           
#winning message,compares the line with the input 
           replay_loop()           
    if theword == '_' * lengthofword:
        print("YOU DID IT GREATDANE! YOU GUESS THE WORD")
        replay_loop()
    elif count != limit:
        hangmangame()

foundation()

hangmangame()

                   
