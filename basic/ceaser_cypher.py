alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def calculate():
    go_again = " "
    while go_again.lower() == "yes" or go_again == " ":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        while direction != "encode" and direction != "decode":
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        coded_word = []
    
        for letter in text:
            index_new_letter = 0
            new_letter = ""
            if letter == " ":
                coded_word += letter
            elif direction == "encode":
                index_new_letter = (alphabet.index(letter) - shift) % 26
            elif direction == "decode":
                index_new_letter = (alphabet.index(letter) + shift) % 26
            if letter != " ":
                new_letter = alphabet[index_new_letter]
                coded_word += new_letter
        print("".join(coded_word))
        go_again = input("would you like to go again Yes for Yes")


calculate()
print("Goodbye")
