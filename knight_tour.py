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
restart = chess_board

up_down = random.randint(0,7)
left_right = random.randint(0,7)
recorded_moves = [[up_down,left_right]]
number_moves = 1
illegal_moves = []
empty_space = 64
backtrack_index = -1
chess_board_index = 0
moves_last_turn = []

while empty_space < 65 :
    last_turn_backtrack = False
    new_move = []
    empty_space = 0
    possible_moves= [(up_down+2, left_right +1), (up_down+2, left_right -1), (up_down-2, left_right+1),
                    (up_down-2, left_right-1), (up_down+1, left_right+2), (up_down - 1, left_right+2),
                    (up_down+1,left_right-2), (up_down-1, left_right-2),
                    ]
    time.sleep(0.2)
    for key in chess_board:
        if key == up_down :
            chess_board[up_down][left_right] = "[H]"
        print(''.join(chess_board[key]))
        for square in chess_board[key]:
            if square == "[ ]" :
                empty_space -= 1
    n = 64 - empty_space
    next_move = []    
    chess_board[up_down][left_right] = f"[{number_moves}]"
    print("New Move\n")
    #print(empty_space)

    for key in possible_moves:
        if key[0]>=0 and key[1] >= 0 and key[0]<=7 and key[1] <= 7 :
            if chess_board[key[0]][key[1]] == "[ ]":
                next_move.append([key[0], key[1]])
    #move = random.choice((next_move))
    for move in illegal_moves:
        if move in next_move or move in moves_last_turn:
            next_move.remove(move)
    

    if next_move:
        number_moves += 1
        up_down = next_move[0][0]
        left_right = next_move[0][1]
        recorded_moves.append(next_move[0])
        backtrack_index = -1
        illegal_moves = []
        moves_last_turn = []
        moves_last_turn.append(next_move)
    else :
        illegal_moves.append([up_down,left_right])
        chess_board_index -= 1
        chess_board[up_down][left_right] = "[ ]"
        chess_board[recorded_moves[chess_board_index][0]][recorded_moves[chess_board_index][1]] = "[ ]"
        number_moves -= 1
        backtrack_index -= 1
        up_down = recorded_moves[backtrack_index][0]
        left_right = recorded_moves[backtrack_index][1]
        illegal_moves.append([up_down,left_right])

    #print(number_moves)
for key in chess_board:
    print("".join(chess_board[key]))    
print("You win")