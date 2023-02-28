import random
import time

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]


def get_score(hand):
    n = 0
    for key in hand:
        if key == "Q" or key == "K" or key == "J":
            n += 10
        elif key == "A":
            if n + 11 <= 21:
                n += 11
            else:
                n += 1
        else:
            n += int(key)
    return n


def deal_hand():
    the_hand = []
    while len(the_hand) < 2:
        the_hand.append(cards[random.randint(0, 12)])
    return the_hand


def play_player_hand(score_list):
    p_hand = deal_hand()
    score = get_score(p_hand)
    print(f"{p_hand} score : {score}")
    if score == 21:
        time.sleep(1)
        print("Blackjack! YOU WIN!")
        return True
    while score <= 21:
        hit_pass = ""
        while hit_pass.lower() != "hit" and hit_pass.lower() != "pass":
            hit_pass = input("Hit or Pass\n")
        if hit_pass == "pass":
            return p_hand
        elif hit_pass == "hit":
            time.sleep(1)
            p_hand.append(cards[random.randint(0, 12)])
            score = get_score(p_hand)
            print(f"{p_hand} score : {score}")
    if score > 21:
        time.sleep(1)
        print(f"score : {score} BUST! YOU LOSE")
        return p_hand and score_list


def play_computer_hand(pl_hand_score, c_hand, score_list):
    score = get_score(c_hand)
    if pl_hand_score > 21:
        return c_hand
    while score <= pl_hand_score:
        time.sleep(1)
        c_hand.append(cards[random.randint(0, 12)])
        score = get_score(c_hand)
        print(f"{c_hand} score : {score}")
    if score > 21:
        time.sleep(1)
        print(f"Computer is BUST with {score} score, YOU WON!")
        return c_hand and score_list
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
score = [0, 0]

while play != "no":
    comp_hand = deal_hand()
    print(f"[{comp_hand[0]}][[]]")
    comp_score = get_score(comp_hand)

    # computer blackjack
    if comp_score == 21:
        score[1] += 1
        print(f"{comp_hand} BLACKJACK! Computer wins")
        print(f"Computer wins : {score[1]}\nPlayer wins : {score[0]}")
        play = play_again_prompt()
        continue
    # computer blackjack end

    time.sleep(1)
    your_hand = play_player_hand(score)

    # player blackjack
    if your_hand is True:
        score[0] += 1
        print(f"Computer wins : {score[1]}\nPlayer wins : {score[0]}")
        play = play_again_prompt()
        continue
    # player blackjack end

    your_score = get_score(your_hand)
    print(f"Computer hand\n {comp_hand}")
    time.sleep(1)
    comp_hand = play_computer_hand(your_score, comp_hand, score)
    comp_score = get_score(comp_hand)

    if your_score <= 21 and comp_score <= 21:
        if your_score > comp_score:
            print(f"YOU WIN with score : {your_score}")
            score[0] += 1
        elif your_score < comp_score:
            print(f"Computer WINs with score : {comp_score}")
            score[1] += 1
        elif your_score == comp_score:
            print("DRAW!!!")

    print(f"Computer wins : {score[1]}\nPlayer wins : {score[0]}")

    play = play_again_prompt()
