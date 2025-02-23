# This program reads in 
# astudents percentage mark and prints out the corresponding grade.
# Author: Finian Doonan

while True:
    percentage = float(input("Enter the percentage: ")) 
    #print (percentage)
    if percentage == -1:
        print ("Exiting program")
        break

    if percentage < 0 or percentage > 100:
        print ("Please enter a number between 0 and 100")
    elif percentage < 40: # if the percentage is less than 40, the student fails
        print ("Fail")
    elif percentage < 50:# if the percentage is less than 50, the student passes
        print ("Pass")
    elif percentage < 60:# if the percentage is less than 60, the student gets a merit 2
        print ("Merit 2")
    elif percentage < 70:# if the percentage is less than 70, the student gets a merit 1
        print ("Merit 1")
    else:
        print ("Distinction")# if the percentage is greater than 70, the student gets a distinction