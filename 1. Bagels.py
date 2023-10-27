#A game about guessing a 3-digit number.
from random import shuffle

#Print rules.
print("This game consists of guessing the hidden three-digit number:")
print("Here are some clues:\n1. If I say 'Pico': One of the digits is correct but in the wrong place.")
print("2. If I say 'Fermi': One of the digits is correct and in the right position.")
print("3. If I say 'Bagels': None of the digits are correct.")
print("Also, you will only have 10 attempts available.")
print("There won't be two identical digits in the secret number.")

#Game function.
def play(num, lives):
    #Variable hidden is used to known if the player win.
    hidden = True
    attemps = 1
    #Game loop, only stopping if attemps == lives, so you lose or hidden come False what means that you won.
    while(attemps <= lives and hidden):
        #The player number must be a 3 digit integer.
        guess = input("\nGuess #" + str(attemps) + ":\n")
        acceptable_number = False
        while(not acceptable_number):
            try:
                guess = int(guess)
                if guess > 99 and guess < 1000:
                    acceptable_number = True
                else:
                    guess = input("I'm sorry, the entered number can only contain 3 digits, try again: ")
            except:
                guess = input("I'm sorry, the entered number can only contain 3 digits, try again: ")
        guess = str(guess)
        #If you guess correctly the number.
        if guess == num:
            hidden = False
        else:
            #Use brute force to know if you have any correct digit.
            printer = ['', '', '']
            for i in range(len(guess)):
                if guess[i] in num:
                    for x in range(len(num)):
                        if guess[i] == num[x]:
                            if x == i:
                                printer[i] = "Fermi"
                            elif printer[i] != "Fermi":
                                printer[i] = "Pico"
            if printer[0] == '' and printer[1] == '' and printer[2] == '':
                print("Bagels")
            else:
                for i in printer:
                    if i != '':
                        print(i, end= ' ')
            attemps += 1
    if hidden:
        print("Sorry you lose all your lives, try again.")
    else:
        print("You got it!")
                    
lives = 10
#Creating the hidden number.
all_numbers = list("0123456789")
shuffle(all_numbers)
secret_num = ''
for i in range(3):
    secret_num += all_numbers[i]
continue_playing = True
#Loop for multiple games.
while(continue_playing):
    play(secret_num, lives)
    response = input("Do you want to play again? (yes or no)\n").lower()
    while(response != "yes" and response != "no"):
        response = input("Do you want to play again? (yes or no)\n").lower()
    if response == "no":
        continue_playing = False
        print("Thanks for playing.")
    else:
        lives = 10
        all_numbers = list("0123456789")
        shuffle(all_numbers)
        secret_num = ''
        for i in range(3):
            secret_num += all_numbers[i]