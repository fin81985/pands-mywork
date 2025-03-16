# Author: Finian Doonan

# Function to display the menu
def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip()
    return choice

# Function to read modules
def readModules():
    modules = []
    moduleName = input("\tEnter module name (blank to quit): ").strip()
    while moduleName != "":
        module = {"name": moduleName}
        modules.append(module)
        moduleName = input("\tEnter another module name (blank to quit): ").strip()
    return modules

# Function to add a student
def doAdd(students):
    studentName = input("Enter student name: ").strip()
    studentModules = readModules()
    student = {"name": studentName, "modules": studentModules}
    students.append(student)

# Function to view students
def doView(students):
    for student in students:
        print(f"Student: {student['name']}")
        for module in student["modules"]:
            print(f"\tModule: {module['name']}")

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
