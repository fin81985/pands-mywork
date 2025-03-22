# usaing os.path to check if file exists
# if file does not exist create it
# Author: Finian Doonan
import os.path
FILENAME = "count.txt"

if not os.path.isfile(FILENAME):
    print ("File does not exist")
 
 #initialise file here
    def writeNumber(number):
        with open(FILENAME, 'w') as f:
            f.write(int(number))
    writeNumber(0)
    
def readNumber():
    try:
        with open(FILENAME) as f:
            number = int(f.read())
            return number  
    except IOError:
        # this file will be created when we write back.
        # no file assumes first time running
        # ie 0 previous runs
        return 0