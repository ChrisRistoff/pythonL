binary_numbers = [128, 64, 32, 16, 8, 4, 2, 1]


def convert_to_binary(number):
    binary = ""
    for num in binary_numbers:
        if number >= num:
            binary += "1"
            number -= num
        else:
            binary += "0"
    return binary


def get_number():
    try:
        number = int(input("Enter a number:"))
        if number < 0 or number > 255:
            raise ValueError
    except ValueError or TypeError:
        print("Please enter a number between 0 and 255.")
        get_number()
    return number


def main():
    number = get_number()
    print(convert_to_binary(number))


if __name__ == "__main__":
    main()
