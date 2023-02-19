import random
import time

chess_board = {
    1: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
    2: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
    3: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
    4: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
    5: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
    6: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
    7: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
    8: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
}

reset = chess_board

up_down = random.randint(1,8)
left_right = random.randint(1,7)
recorded_moves = []
n = -1

while n < 64 :
    recorded_moves.append([up_down, left_right])
    time.sleep(0)
    for key in chess_board:
        if key == up_down :
            chess_board[up_down][left_right] = "[H]"
        print(''.join(chess_board[key]))
    next_move = []    
    chess_board[up_down][left_right] = f"[{n}]"
    print('''new
move
    ''')
    
    if up_down + 2 <= 8:
        if left_right +1 <= 7 :
            if chess_board[up_down + 2][left_right + 1] == "[ ]" :
                next_move.append([up_down+2,left_right +1])
        if left_right - 1 >= 0 :
            if chess_board[up_down + 2][left_right - 1] == "[ ]" :
                next_move.append([up_down+2, left_right -1])
    if up_down -2 >= 1:
        if left_right +1 <= 7 :
            if chess_board[up_down - 2][left_right + 1] == "[ ]" :
                next_move.append([up_down-2, left_right+1])
        if left_right - 1 >= 0 :
            if chess_board[up_down - 2][left_right - 1] == "[ ]" :
                next_move.append([up_down-2, left_right-1])
    if left_right +2 <= 7 :
        if up_down + 1 <= 8 :
            if chess_board[up_down + 1][left_right + 2] == "[ ]" :
                next_move.append([up_down+1, left_right+2])
        if up_down -1 >= 1 :
            if chess_board[up_down - 1][left_right + 2] == "[ ]" :
                 next_move.append([up_down - 1, left_right+2])
    if left_right -2 >= 0:
        if up_down + 1 <= 8 :
            if chess_board[up_down + 1][left_right - 2] == "[ ]":
                next_move.append([up_down+1,left_right-2])
        if up_down -1 >= 1 :
            if chess_board[up_down - 1][left_right - 2] == "[ ]" :
                next_move.append([up_down-1, left_right-2])
    if next_move == [] :
        up_down = recorded_moves[0][0]
        left_right = recorded_moves[0][1]
        #print(f"GOING BACK {go_back} MOVES")
        time.sleep(0)
        recorded_moves = []
        n = 0
        chess_board = {
    1: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
    2: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
    3: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
    4: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
    5: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
    6: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
    7: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
    8: ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
}
 
    elif next_move != []:
        n += 1
        move = random.choice(next_move)
        up_down = move[0]
        left_right = move[1]
   # print(str(n))
for key in chess_board:
    print("".join(chess_board[key]))    
print("You win")

    