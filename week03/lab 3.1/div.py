# program that reads in two numbers 
# outputs the integer answer and remainder

x = int(input("Enter first number: ")) # read first number
y = int(input("Enter second number: ")) # read second number

answer = int(x / y) # divide the two numbers and convert to an integer
remainder = x % y # calculate the remainder

print("{} divided by {} is {} with remainder {}" .format(x, y, answer, remainder)) # output the answer and remainder