dicto = {
    "Jack": 10,
    "Romy": 20,
    "Adam": 30,
    "Bongo": 40,
    "Bingo": 50,
    "Candy": 60,
    "Dandy": 70,
    "Dingo": 80,
    "Eagle": 90,
    "Fancy": 100,
    "Gandy": 110,
    "Honey": 120,
    "Igloo": 130,
    "Jolly": 140,
    "Kandy": 150,
    "Lucky": 160,
    "Mandy": 170,
    "Nancy": 180,
    "Oggy": 190,
    "Pandy": 200,
    "Qandy": 210,
    "Randy": 220,
    "Sandy": 230,
    "Tandy": 240,
    "Uggy": 250,
    "Vandy": 260,
    "Wandy": 270,
    "Xandy": 280,
    "Yandy": 290,
    "Zandy": 300,
}

dataset = [key for key in dicto.keys()]

# Sort the list
dataset.sort()


def binary_search(dataset, target):
    low = 0
    high = len(dataset) - 1

    # this will keep dividing the list in half until the target is found
    while low <= high:
        # Find the middle of the list
        mid = (low + high) // 2

        # Check if target is in mid
        if dataset[mid] == target:
            return True
        elif target < dataset[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False


def main(dic):
    target = input("Enter the name to search for: \n").title()
    result = binary_search(dataset, target)
    if result == "exit":
        quit()
    if result:
        print(f"{target} found and has a value of {dicto[target]}")
    else:
        print(f"{target} returned no results")


if __name__ == "__main__":
    while True:
        main(dicto)
