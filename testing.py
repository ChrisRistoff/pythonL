arr = [":D", ":~)", ";-D", ":)"]


def count_smileys(arr):
    valid_faces = [":)", ":D", ";-D", ":~)"]
    n = 0
    for i in valid_faces:
        if i in arr:
            n += 1
    return n


print(count_smileys(arr))
