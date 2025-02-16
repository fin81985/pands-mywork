# rounds a number
# be careful of rounding , it rounds to the nearest even number
# eg round(4.5) gives 4, round(5.5) gives 6
# so do not use it where accuracy is important
# Author: Finian Doonan

numberToRound = float(input("Enter a float number: ")) # read a float number
roundedNumber = round(numberToRound) # round the number
print('{} rounded is {}'.format(numberToRound, roundedNumber)) # output the answer  