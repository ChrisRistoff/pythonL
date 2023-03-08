import pandas as pd
from get_weather import get_weather

data = pd.read_csv("weather_data.csv")

index = get_weather() - 1

print(
    f"The temperature on {data['day'][index]} was {data['temp'][index]} degrees.\nIt was {data['condition'][index]}."
)
