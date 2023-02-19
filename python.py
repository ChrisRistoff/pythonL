import random
import time

chess_board = {
    0: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
    1: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
    2: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
    3: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
    4: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
    5: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
    6: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
    7: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
}

up_down = random.randint(0,7)
left_right = random.randint(0,7)
recorded_moves = [[up_down,left_right]]
number_moves = 1
old_number_moves = 20

while number_moves < 64 :
    possible_moves= [(up_down+2, left_right +1), (up_down+2, left_right -1), (up_down-2, left_right+1),
                    (up_down-2, left_right-1), (up_down+1, left_right+2), (up_down - 1, left_right+2),
                    (up_down+1,left_right-2), (up_down-1, left_right-2),
                    ]
    time.sleep(0)
    for key in chess_board:
        if key == up_down :
            chess_board[up_down][left_right] = "[H]"
        print(''.join(chess_board[key]))
    next_move = []    
    chess_board[up_down][left_right] = f"[{number_moves}]"
    chess_board[recorded_moves[-1][0]][recorded_moves[-1][1]] = "[P]"
    print('''new
move
    ''')
    
    for key in possible_moves:
        if key[0]>=0 and key[1] >= 0 and key[0]<=7 and key[1] <= 7 :
            if chess_board[key[0]][key[1]] == "[ ]":
                next_move.append([key[0], key[1]])
    #move = random.choice((next_move))

    if next_move == [] or next_move == recorded_moves[-1]:
        go_back = 1
        up_down = recorded_moves[-go_back][0]
        left_right = recorded_moves[-go_back][1]
        number_moves -= go_back
        chess_board[recorded_moves[-1][0]][recorded_moves[-1][1]] = "[ ]"
        del recorded_moves[-1]
    elif next_move != [] and next_move != recorded_moves[-1]:
        move = next_move[0]
        number_moves += 1
        up_down = move[0]
        left_right = move[1]
        recorded_moves.append((move))
        print(recorded_moves)
    print(str(number_moves))
for key in chess_board:
    print("".join(chess_board[key]))    
print("You win")