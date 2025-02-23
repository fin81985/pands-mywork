# This program ask the user to entry a number and then it will tell the user if the number is even or odd.
# Author: Finian Doonan

number = int (input (" enter an integer: "))
if (number % 2) == 0:
    print (" f{number} is an even number")
else:
    print (f"{number} is an odd number")