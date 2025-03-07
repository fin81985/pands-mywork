

import datetime

# Define a dictionary to map day numbers to names and types
days = {
    0: ("Monday", "Weekday"),
    1: ("Tuesday", "Weekday"),
    2: ("Wednesday", "Weekday"),
    3: ("Thursday", "Weekday"),
    4: ("Friday", "Weekday"),
    5: ("Saturday", "Weekend"),
    6: ("Sunday", "Weekend"),
}

# Get today's day number (0 = Monday, 6 = Sunday)
today_num = datetime.datetime.today().weekday()

# Get the day's name and type (Weekday/Weekend)
day_name, day_type = days[today_num]

# Output the result based on the day type
if day_type == "Weekday":
    print(f"Yes, unfortunately today is {day_name}, a weekday.")
else:
    print(f"It is {day_name}, the weekend, yay!")
