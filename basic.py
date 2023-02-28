import random
import time

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_hand():
    the_hand = []
    while len(the_hand) < 2:
        the_hand.append(cards[random.randint(0, 12)])
    if sum(the_hand) > 21:
        the_hand[1] = 1
    return the_hand


def play_player_hand():
    p_hand = deal_hand()
    print(f"{p_hand} score : {sum(p_hand)}")
    if sum(p_hand) == 21:
        time.sleep(1)
        print("Blackjack! YOU WIN!")
        return True
    while sum(p_hand) <= 21:
        hit_pass = ""
        while hit_pass.lower() != "hit" and hit_pass.lower() != "pass":
            hit_pass = input("Hit or Pass\n")
        if hit_pass == "pass":
            return p_hand
        elif hit_pass == "hit":
            time.sleep(1)
            p_hand.append(cards[random.randint(0, 12)])
            print(f"{p_hand} score : {sum(p_hand)}")
            if p_hand[-1] == 11:
                choose_ace_value = 0
                while choose_ace_value != 1 and choose_ace_value != 11:
                    try:
                        choose_ace_value = int(input("Choose 1 or 11 for ace value\n"))
                    except ValueError or TypeError:
                        continue
                p_hand[-1] = choose_ace_value
                print(f"{p_hand} score : {sum(p_hand)}")
    if sum(p_hand) > 21:
        time.sleep(1)
        print(f"score : {sum(p_hand)} BUST! YOU LOSE")
        return p_hand


def play_computer_hand(pl_hand, c_hand):
    if sum(pl_hand) > 21:
        return
    while sum(c_hand) < sum(pl_hand):
        time.sleep(1)
        c_hand.append(cards[random.randint(0, 12)])
        print(f"{c_hand} score : {sum(c_hand)}")
        if c_hand[-1] == 11:
            if sum(c_hand) > 21:
                c_hand[-1] = 1
                time.sleep(1)
                print(f"{c_hand} score : {sum(c_hand)}")
    if sum(c_hand) > 21:
        time.sleep(1)
        print(f"Computer is BUST with {sum(c_hand)} score, YOU WON!")
        return c_hand
    return c_hand


def play_again_prompt():
    a = ""
    while a != "yes" and a != "no":
        a = input("Would you like to play again?\n")
    if a == "no":
        return a
    else:
        return a


play = ""
while play != "no":
    comp_hand = deal_hand()
    print(f"[{comp_hand[0]}][[]]")
    if comp_hand == 21:
        print(f"{comp_hand} BLACKJACK! Computer wins")
        play = play_again_prompt()
        continue
    time.sleep(1)
    your_hand = play_player_hand()
    if your_hand is True:
        play = play_again_prompt()
        continue
    print(f"Computer hand\n {comp_hand}")
    time.sleep(1)
    comp_hand = play_computer_hand(your_hand, comp_hand)

    if sum(your_hand) > 21 or sum(comp_hand) > 21:
        """"""
    else:
        if sum(your_hand) > sum(comp_hand):
            print(f"YOU WIN with score : {sum(your_hand)}")
        elif sum(your_hand) < sum(comp_hand):
            print(f"Computer WINs with score : {sum(comp_hand)}")
        else:
            print("DRAW!!!")
    play = play_again_prompt()
