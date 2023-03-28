dict1 = {
        'a': 1,
        'b': 2,
        }

dict2 = dict1

print("before value is updated:")
print("dict1: ", dict1)
print("dict2: ", dict2)



print ("dict 1 points to: ", id(dict1))
print ("dict 2 points to: ", id(dict2))

dict2['a'] = 3

print("after value is updated:")
print("dict1: ", dict1)
print("dict2: ", dict2)

print ("dict 1 points to: ", id(dict1))
print ("dict 2 points to: ", id(dict2))
