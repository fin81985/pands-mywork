# Write a program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line.
# Author: Finian Doonan


import sys# import the sys module
if len(sys.argv) != 2:# check if the number of arguments is not equal to 2
    print("Usage: python es.py <filename>")
    sys.exit(1)

filename = sys.argv[1]  # get the filename from the command line
count = 0  # set the count to 0

try:  # try to open the file
    with open(filename, 'r') as f:  # open the file
        for line in f:
            count += line.count('e')  # count the number of 'e' in the line

except FileNotFoundError:  # deals with the error if the file is not found
    print(f"Error: The file '{filename}' was not found.")
    sys.exit(1)

print(f"The text '{filename}' contains {count} occurrences of the letter 'e'.")


