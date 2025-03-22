# Write a program that reads a number from a file and increments it by 1.
# Authtor: Finian Doonan

FILENAME = "count.txt"
def readNumber():
    with open(FILENAME) as f:
         number = int(f.read())
         return number
     
def writeNumber(number):# write a number to a file
    with open(FILENAME, "wt") as f:
 
 # write takes a string so we need to convert
        f.write(str(number))
        
# main
num = readNumber()
num += 1
print (f"we have run this program {num} times")
writeNumber(num)