# Description: A program that uses functions to add students and modules to a list and display them.
# The program uses a menu system to allow the user to choose whether to add a student, view students, or quit.
# Author: Finian Doonan

# Function to display the menu
def displayMenu(): 
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip().lower() # .strip() removes any whitespace from the beginning and end of the string
    return choice

# Function to read modules
def readModules():
    modules = []
    moduleName = input("\tEnter module name (blank to quit): ").strip()
    while moduleName != "":
        grade = input(f"\tEnter grade for {moduleName}: ").strip()  # Adding grade input
        module = {"name": moduleName, "grade": grade}
        modules.append(module)
        moduleName = input("\tEnter another module name (blank to quit): ").strip()
    return modules

# Function to add a student
def doAdd(students):
    studentName = input("Enter student name: ").strip()
    studentModules = readModules()
    student = {"name": studentName, "modules": studentModules}
    students.append(student)

# Function to display modules
def displayModules(modules): 
    print("\tName\tGrade") 
    for module in modules: 
        print(f"\t{module['name']}\t{module['grade']}") # ues single quotes for the string and double quotes for the f-string  

# Function to view students
def doView(students): 
    for currentStudent in students: 
        print(f"Student: {currentStudent['name']}") 
        displayModules(currentStudent["modules"])

# Main program
students = []
choice = displayMenu()

while choice != 'q':
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    else:
        print("\n\nPlease select either a, v, or q")
    
    choice = displayMenu()

print("Bye bye!!!")

