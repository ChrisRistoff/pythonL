# 107W per square meter


class Room:
    def __init__(self, length, width, wattage_per_m):
        self.length = length
        self.width = width
        self.wattage_per_m = wattage_per_m


    def calculate_square_meter(self):
        return self.length * self.width


    def calculate_heater_wattage(self):
        return self.calculate_square_meter() * self.wattage_per_m


def type_value_debug(a):
    while True:
        try:
            a = float(input(f"Enter the {a} of the room: "))
        except ValueError or TypeError:
            continue
        return a


while True:
    lenght = type_value_debug("lenght")
    width = type_value_debug("width")

    room = Room(lenght, width, 107)
    room_size = room.calculate_square_meter()
    square_meter_wattage = room.calculate_heater_wattage()

    print(
        f"The room is {room_size} square meters and needs {square_meter_wattage} Watts of heating"
    )

    again = ""
    while again != "y" and again != "n":
        again = input("Do you want to calculate another room? (y/n): ")

    if again == "y":
        continue
    else:
        break
