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

up_down = random.randint(1,8)
left_right = random.randint(1,7)
recorded_moves = []

x = True
for key in chess_board:
    if "[ ]" in chess_board[key]:
        x = True
    else :
        x = False
    while x == True :
        recorded_moves.append([up_down, left_right])
        time.sleep(1)
        for key in chess_board:
            if key == up_down :
                chess_board[up_down][left_right] = "[H]"
            print(''.join(chess_board[key]))
        next_move = []    
        chess_board[up_down][left_right] = "[X]"
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
            n = int(input("How many moves would you like to go back? \n"))
            up_down = recorded_moves[-n][0]
            left_right = recorded_moves[-n - 1][1]
            print(f"GOING BACK {n} MOVES")
            time.sleep(1)
            for key in range(1, n) :
                chess_board[recorded_moves[-key][0]][recorded_moves[-key][1]] = "[ ]"
                del recorded_moves[-key]
        elif next_move != []:
            move = random.choice(next_move)
            up_down = move[0]
            left_right = move[1]

        
print("You win")

    