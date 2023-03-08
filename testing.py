import pandas

data = pandas.read_csv("weather_check_csv/weather_data.csv")

data_dict = data.to_dict()


monday = data[data.day == "Monday"]

mon_far = monday.temp * 9 / 5 + 32

print(float(mon_far))

# create a dataframe from scratch

data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}

data = pandas.DataFrame(data_dict)

print(data)
