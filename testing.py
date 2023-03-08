with open("weather_data.csv") as data_file:
    data = data_file.readlines()

updated_data = []
days_in_week = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]

for line in data:
    line = [line.strip()]
    updated_data.append(line)

day_choose = input("Which day of the week would you like to see the temperature for? ")
while day_choose.lower() not in days_in_week:
    day_choose = input("Please enter a valid day of the week: ")

chosen_day = updated_data[days_in_week.index(day_choose) + 1]

print(chosen_day)
