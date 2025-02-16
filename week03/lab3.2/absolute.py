# Give the absolute value of a number

# Author: Finian Doonan

# in the question, number is ambiguous but the
# output implies that it is a float number
# so I will use a float number in the input

number = float(input("Enter a number: ")) # read a float number
absoluteValue = abs(number) # get the absolute value
print('The absolute value of {} is {}'.format(number, absoluteValue)) # output the answer
