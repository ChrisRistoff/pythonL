import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    new_data = []
    for row in data:
        new_data.append(row)

days_of_week = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]

choose_day = input("Which day of the week would you like to see the temperature for? ")
while choose_day not in days_of_week:
    choose_day = input("Please choose a day of the week: ")

chosen_day = new_data[days_of_week.index(choose_day) + 1]

print(
    f"The temperature on {choose_day.title()} was {chosen_day[1]} degrees.\nIt was {chosen_day[2]}."
)
