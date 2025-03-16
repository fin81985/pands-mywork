

def readModules (): # define a function called readModules
    modules = [] # create an empty list called modules
    moduleName = input("\tEnter the first module name (blank to quit): ") # get the user input and assign it to the variable moduleName

    
    while moduleName != "": # while the variable moduleName is not equal to an empty string
        module = {} # create an empty dictionary called module
        module["name"] = moduleName # assign the value of the variable moduleName to the key "name" in the dictionary module
        module["grade"] = int(input("\tEnter grade: ")) # get the user input and assign it to the key "grade" in the dictionary module
        modules.append(module) # append the dictionary module to the list modules
        moduleName = input("\tEnter the next module name (blank to quit): ") # get the user input and assign it to the variable moduleName
    
    return modules # return the list modules