# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    letter_text = letter.read()


for name in names_list:
    name = name.strip()
    new_letter = letter_text.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
        file.write(new_letter)
