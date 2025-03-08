# create a program that tells the user whether it is a weekday or weekend

# Autror : Finian Doonan



from datetime import datetime   # import the datetime module

dt = datetime.now() # get the current date and time
day_name = dt.strftime("%A") #  the strftime() method formats the date and time into a readable string

weekday = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
weekend = {"Saturday", "Sunday"}    # create a list of weekdays and weekends

if day_name in weekday: 
    print("Yes, unfortunately, it is a weekday.")
else: 
    print("Yay, it is the weekend!")

