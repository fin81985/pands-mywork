# Write a program that allows a user to add students to a list of students. Each student will have a name and a list of modules. The user can keep adding modules to the list until they enter a blank module name. The program should then print out the list of students and their modules.
# Author : Finian Doonan

students = [] # create an empty list called students

def readModules(): # define a function called readModules
    return [] # return an empty list

def doAdd(students): # define a function called doAdd that takes a parameter students
    currentStudent = {} # create an empty dictionary called currentStudent
    currentStudent["name"] = input("enter name : ") # get the user input and assign it to the key "name" in the dictionary currentStudent
    currentStudent["modules"] = readModules() # assign the result of calling the function readModules to the key "modules" in the dictionary currentStudent
    
    students.append(currentStudent) # append the dictionary currentStudent to the list students
    
# test

doAdd(students)
doAdd(students)
print(students) # print the list students