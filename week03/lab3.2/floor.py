# Take in a float and output an int rounded down.
# Author: finian Doonan

import math

numberToFloor = float(input("Enter a float number: ")) # read a float number
flooredNumber = math.floor(numberToFloor) # floor the number
print('{} floored is {}'.format(numberToFloor, flooredNumber)) # output the answer