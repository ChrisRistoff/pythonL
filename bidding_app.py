all_bids = {}
another_bid = ""
highest_bid_list = []

def new_bid (a, b) :
    all_bids.update({a:[b]})

def highest_bid (bid_dic) :
    for key in bid_dic:
        highest_bid_list.append(bid_dic[key][0])

def result(bid_dic) :
    for key in bid_dic:
        if bid_dic[key][0] == max(highest_bid_list) :
            print(f"The highest bidder is {key} with £{bid_dic[key][0]}")
        

while another_bid != "no" :
    new_bid(input("Add name\n"), int(input("add bid\n")))

    another_bid = " "
    while another_bid != "no" and another_bid != "yes" :
        another_bid = input("Would you like to add another bid?\n").lower()      

highest_bid(all_bids)

result(all_bids)