# Write a function that writes a dictionary to a json file
# Author: Finian Doonan


import json
FILENAME="testdict.json"
sample= dict(name='fred', age=31, grades=[1,34,55])

def writeDict(obj):
    with open(FILENAME, 'wt') as f:
        json.dump(obj,f)
#test the function
writeDict(sample)