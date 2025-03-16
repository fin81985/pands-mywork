# create a function to display a menu
# create a function to display a menu
# create a function to display a menu
# Author : Finian Doonan

def displayMenu(): # define a function called displayMenu
    print (" What would you like to do?") # print the string "What would you like to do?"
    print ("\t(a) Add new student") # print the string "Add new student"
    print ("\t(v) View students")
    print ("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip() # get the user input and remove any whitespace
    
    return choice # return the value of choice

choice = displayMenu() # call the function displayMenu and assign the result to the variable choice
print (f"you chose {choice}")