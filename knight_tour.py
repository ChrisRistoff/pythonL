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
past_move = [[0,1],[1,0]]

while number_moves <= 64 :
    possible_moves= [(up_down+2, left_right +1), (up_down+2, left_right -1), (up_down-2, left_right+1),
                    (up_down-2, left_right-1), (up_down+1, left_right+2), (up_down - 1, left_right+2),
                    (up_down+1,left_right-2), (up_down-1, left_right-2),
                    ]
    time.sleep(0)
    for key in chess_board:
        if key == up_down :
            chess_board[up_down][left_right] = "[H]"
      #  print(''.join(chess_board[key]))
    next_move = []    
    chess_board[up_down][left_right] = f"[{number_moves}]"
    #print("New Move\n")
    
    for key in possible_moves:
        if key[0]>=0 and key[1] >= 0 and key[0]<=7 and key[1] <= 7 :
            if chess_board[key[0]][key[1]] == "[ ]":
                next_move.append([key[0], key[1]])
    #move = random.choice((next_move))

    if next_move and next_move[0] != recorded_moves[-1] :
        recorded_moves.append(next_move[0])
        up_down = next_move[0][0]
        left_right = next_move[0][1]
        number_moves += 1
        previous_move = next_move[0]
    elif not next_move and previous_move[0] != recorded_moves[-2] :
        chess_board[up_down][left_right] = "[ ]"
        up_down = recorded_moves[-2][0]
        left_right = recorded_moves[-2][1]
        number_moves -= 1
    else :
        chess_board[up_down][left_right] = "[ ]"
        chess_board[recorded_moves[-1][0]][recorded_moves[-1][1]] = "[ ]"
        chess_board[recorded_moves[-2][0]][recorded_moves[-2][1]] = "[ ]"
        up_down = recorded_moves[-3][0]
        up_down = recorded_moves[-3][1]
        number_moves -= 1
    if number_moves < 0 :
        for key in chess_board:
            for square in chess_board[key] :
                if square != "[ ]" :
                    chess_board[key] = ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"]
        number_moves = 1
        recorded_moves = [[up_down,left_right]]
        past_move = [[0,1],[1,0]]


    #print(number_moves)
for key in chess_board:
    print("".join(chess_board[key]))    
print("You win")