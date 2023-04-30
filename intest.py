import random

workers = [
        "Sally",
        "Bob",
        "Fiona",
        "Mary",
        "George",
        "Alice",
        ]
pairs = []


def shuffle_list(workers):
    random.shuffle(workers)
    return workers


def group_up_pairs(workers):
    for i in range(0, int((len(workers)/2))):
        pair_list=[]
        pair_list.append(workers[i])
        pair_list.append(workers[i+1])

        pairs.append(pair_list)

    return pairs

new_list=shuffle_list(workers)

pairs=group_up_pairs(new_list)

print(pairs)
