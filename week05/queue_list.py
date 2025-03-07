# create a queue using a list
# add 10 random numbers to the queue

# Author: Finian Doonan

import random

queue = []
numberOfNumbers = 10
rangeTo = 100

# Generate random numbers and add them to the queue
for n in range(0, numberOfNumbers):
    queue.append(random.randint(0, rangeTo))

print(f"queue is {queue}")

# Take numbers from the queue
while len(queue) != 0:
    
    currentNumber = queue.pop(0) 
    print(f"current Number is {currentNumber} and the queue is {queue}")

print("the queue is now empty")
