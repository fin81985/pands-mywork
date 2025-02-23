# this program prompts the user to guess a number between 1 and 100
# Author: Finian Doonan

number_to_guess = 30

guess = int(input("Please guess the number: "))
while guess != number_to_guess:
        print ("Wrong")
        guess = int(input("Please guess again: "))
    
print ("Well done! Yes the number was", number_to_guess)