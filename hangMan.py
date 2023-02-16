import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
question = ["_"] * len(chosen_word)
mistakesGG = 6
listOfUsedLetters = [""]
print(question)
while chosen_word != (''.join(question)) and mistakesGG > 0 :
    mistakesMade = 0    
    questionIndex = 0
    guess = input('choose a letter: \n')
    if guess in listOfUsedLetters :

        print('stop using that stupid')
        continue
    listOfUsedLetters.extend(guess)
     
    for letter in chosen_word :
        if letter == guess:
            question[questionIndex] = guess
            questionIndex += 1            
        elif letter != guess : 
            questionIndex += 1
            mistakesMade += 1
        if mistakesMade == len(chosen_word) :
                    mistakesGG -= 1
                    print(stages[mistakesGG + 1])


    print(' '.join(question))

if mistakesGG == 0 :
    print(f'get rekt loser\n{stages[0]}')
else :
    print('you win')