all_bids = {}


def new_bid(
    a,
    b,
):
    all_bids.update({a: [b]})


def highest_bid(dic, lis):
    for key in dic:
        lis.append(dic[key][0])
    for key in dic:
        if dic[key][0] == max(lis):
            return f"The highest bidder is {key} with £{dic[key][0]}"


def program(another_bid, bids):
    while another_bid != "no":
        new_bid(input("Add name\n"), int(input("add bid\n")), bids={})
        another_bid = ""

        while another_bid != "no" and another_bid != "yes":
            another_bid = input("Would you like to add another bid?\n").lower()


program("")

print(highest_bid(all_bids, []))
