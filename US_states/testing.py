sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
each_word = [word for word in sentence.split(" ")]

dicto = {key: len(key) for key in each_word}

print(dicto)
