import csv
from get_weather import get_weather

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    new_data = []
    for row in data:
        new_data.append(row)

index = get_weather()

print(
    f"The temperature on {new_data[index][0]} was {new_data[index][1]} degrees.\nIt was {new_data[index][2]}."
)
