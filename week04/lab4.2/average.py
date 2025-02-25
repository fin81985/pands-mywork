#This program reads in numbers until the user enters 0
# It will then print back out again all the numbers entered
#Author: Finian Doonan

numbers = []
number = int(input("Enter a number (0 to quit): ")) #prompt the user to enter a number

while number != 0:  #while the number entered is not 0
    numbers.append(number)      #add the number to the list
    number = int(input("Enter another (0 to quit): "))  #prompt the user to enter another number

for value in numbers:
    print (value)
    
average = float(sum(numbers)) / len(numbers) # calulate the average in float format
print (f"The average is {average}")