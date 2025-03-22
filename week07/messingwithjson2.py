# This program reads a dictionary from a file
# Author: Finian Doonan

import json
FILENAME ="testdict.json"

def readDict():
 # this will throw an error if the file does
# not exist
 # it should readly just return an empty dict
 # we can do this later
     with open(FILENAME) as f:
        return json.load(f)

# test the function
somedict = readDict()
print(somedict)