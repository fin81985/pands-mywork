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

def doAdd(): # define a function called doAdd
    print ("in adding") # print the string "in adding"
    
def doView(): # define a function called doView
    print ("in viewing") # print the string "in viewing"
    
# main program
choice = displayMenu() # call the function displayMenu and assign the result to the variable choice
while (choice != 'q'): # while the value of choice is not equal to 'q'
    if choice == 'a': # if the value of choice is equal to 'a'
        doAdd() # call the function doAdd
    elif choice == 'v': # if the value of choice is equal to 'v'
        doView() # call the function doView
    elif choice != 'q': # if the value of choice is not equal to 'q'
        print ("\n\nplease select either a,v or q") # print the string "please select either a,v or q"
    choice = displayMenu() # call the function displayMenu and assign the result to the variable choice
    
print ("bye bye !!!") # print the string "bye bye !!!"

