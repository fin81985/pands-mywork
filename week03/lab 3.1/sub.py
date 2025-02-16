# program to subtract  one number from another

# input reads a string so we need to convert to an integer
# so we can perform mathematical operations

x = int(input("Enter first number: ")) # read first number
y = int(input("Enter second number: ")) # read second number

answer = x - y # subtract the two numbers

print("{} minus {} is {}" .format(x, y, answer)) # output the answer