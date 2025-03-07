# create a dictionary with student details and print them out

# Author: Finian Doonan

student = {
    "name": "Mary",
    "modules": [
        {
            "courseName": "Programming",
            "grade": 45
        },
        {
            "courseName": "History",
            "grade": 99
        }
    ]
} # Fixed indentation

print("Student: {}".format(student["name"]))

for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))  # print out the modules and grades using a loop