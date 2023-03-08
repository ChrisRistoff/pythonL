with open("Input/Names/invited_names.txt", "r") as file:
    names = file.readlines()
    names = [name.strip() for name in names]

    print(names)
