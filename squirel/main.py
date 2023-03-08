import pandas as pd

data = pd.read_csv("ny_squirels.csv")

g_sq = data[data["Primary Fur Color"] == "Gray"]
b_sq = data[data["Primary Fur Color"] == "Black"]
r_sq = data[data["Primary Fur Color"] == "Cinnamon"]

print(f"{len(g_sq)} grey squirels")
print(f"{len(b_sq)} black squirels")
print(f"{len(r_sq)} red squirels")

data_dict = {
    "Fur Color": ["Gray", "Black", "Red"],
    "Count": [len(g_sq), len(b_sq), len(r_sq)],
}

end_res = pd.DataFrame(data_dict).to_csv("squirel_count.csv")

print(end_res)
