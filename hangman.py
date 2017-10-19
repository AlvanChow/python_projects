from random import *


#Create a hangman game

#Input "Start" to play, "Exit" to quit
#start_or_exit = input("Type 'Start' to begin, or 'Exit' to quit: ")

#List of words to choose from
list_of_words = ['apple', 'orange', 'grapes', 'banana', 'rice', 'fruit', 'mom', 'dad', 'seaweed']

#Define the game
def hangman(start_or_exit = "Start"):
    if start_or_exit == "Start":

        print("\n")
        lives = 10
        print("You have {} lives".format(lives))


        #Choose random word from list
        word = list_of_words[randint(0,len(list_of_words)-1)]

        #How many Blanks
        blanks = ''
        i = 0
        while i < len(word):
            blanks += '_'
            i += 1
        print(" ".join(list(blanks)))
        print("\n")

        #Let player guess letters




        while lives > 0:
            letter = input("Guess your letter: ")
            print("\n")
            blanks_list = list(blanks)
            if letter in word:
                print(border_msg("Good guess!"))
                i = 0
                while i < len(blanks_list):
                    if letter == word[i]:
                        blanks_list[i] = letter
                    i += 1
                print(' '.join(blanks_list))
                blanks = ''.join(blanks_list)

                if '_' not in blanks:
                    print("Winner!")
                    break
                print("\n")


            else:
                print("\n")
                print(border_msg("Wrong"))
                lives -= 1
                print("You have {} lives".format(lives))
                if lives == 0:
                    print("You lose...")
                    break
                print(' '.join(blanks_list))
                print("\n")

def border_msg(msg):

    count = len(msg) + 2 # dash will need +2 too

    dash = "-"*count

    return "+{dash}+\n| {msg} |\n+{dash}+".format(dash=dash,msg=msg)




#Execute game
hangman()
