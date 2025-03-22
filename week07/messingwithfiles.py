# Messing with files
# Autror : Finian Doonan


FILENAME = "count.txt" #create a file called count.txt
# Write a function that reads a number from a file and returns it
def readNumber():
 with open(FILENAME) as f:
        number = int(f.read())
 return number
# test it
num = readNumber()# read the number from the file
print (num)
...

def writeNumber(number):
    with open(FILENAME, "wt") as f:
 # write takes a string so we need to convert
        f.write(str(number))
        
# test it
writeNumber(3)
