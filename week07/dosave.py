students= []

def displayMenu():

    print("what would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(q) Quit")
    choice = input("type one letter (a/v/s/q):").strip()
    return choice

def doAdd(students):
 # you have code here to add
    print("in adding")
def doView(students):
 # you have code here to view
    print("in viewing")
def writeDict(students):
    with open('students.txt', 'w') as f:
        for student in students:
            f.write(f"{student}\n")

def doSave(students):
#you will put the call to save dict here
    writeDict(students)
    print("students saved")
#main program
choice = displayMenu()
while(choice != 'q'):
 # we could do this with lamda functions
 # I am keeping this basic for the moment
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)

    elif choice !='q':
        print("\n\nPlease select either a,v,s or q")
    choice=displayMenu()
    
    writeDict(students)
    print("students saved")
    
def doLoad():

    return readDict()

# in the menu
students = doLoad()