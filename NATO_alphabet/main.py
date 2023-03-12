import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def main():
    user_input = input("Enter a word: ").upper()
    try:
        result = [data_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        main()
    else:
        print(result)


if __name__ == "__main__":
    while True:
        another_word = ""
        main()
        while another_word != "y" and another_word != "n":
            another_word = input("Another word? (y/n): ").lower()
        if another_word == "n":
            break
