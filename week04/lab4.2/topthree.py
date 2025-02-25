# This program generates 10 ramdom  numbers
# prints them out
# then prints out the top 3
# Author: Finian Doonan

import random

howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100

numbers = []

for i in range(0,howMany):
    numbers.append(random.randint(rangeFrom, rangeTo))
    print(f"{howMany} random numbers\t{numbers}") #print the list of random numbers
    
topOnes = numbers.copy()

topOnes.sort(reverse = True)
print(f"Top {topHowMany} numbers are {topOnes[0:topHowMany]}") #print the top 3 numbers