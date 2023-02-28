import random
import time

chess_board = {
    0: ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    1: ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    2: ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    3: ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    4: ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    5: ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    6: ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    7: ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
}
restart = chess_board

up_down = random.randint(0, 7)
left_right = random.randint(0, 7)
recorded_moves = [[up_down, left_right]]
number_moves = 0
backtrack_index = -1
moves_last_turn = [[]]

while len(recorded_moves) < 64:
    new_move = []
    possible_moves = [
        (up_down + 2, left_right + 1),
        (up_down + 2, left_right - 1),
        (up_down - 2, left_right + 1),
        (up_down - 2, left_right - 1),
        (up_down + 1, left_right + 2),
        (up_down - 1, left_right + 2),
        (up_down + 1, left_right - 2),
        (up_down - 1, left_right - 2),
    ]
    time.sleep(0.7)
    for key in chess_board:
        if key == up_down:
            chess_board[up_down][left_right] = "[H]"
        print("".join(chess_board[key]))
    next_move = []
    chess_board[up_down][left_right] = f"[{len(recorded_moves)}]"
    print("New Move\n")
    # print(empty_space)

    for key in possible_moves:
        if key[0] >= 0 and key[1] >= 0 and key[0] <= 7 and key[1] <= 7:
            if chess_board[key[0]][key[1]] == "[ ]":
                next_move.append([key[0], key[1]])
    if len(moves_last_turn) > 9:
        moves_last_turn.remove(moves_last_turn[0])

    for move in moves_last_turn:
        if move in next_move:
            next_move.remove(move)

    if next_move:
        up_down = next_move[0][0]
        left_right = next_move[0][1]
        if next_move[0] not in recorded_moves:
            recorded_moves.append(next_move[0])
        backtrack_index = -1
        moves_last_turn.append(next_move[0])
    else:
        chess_board[up_down][left_right] = "[ ]"
        backtrack_index -= 1
        up_down = recorded_moves[backtrack_index][0]
        left_right = recorded_moves[backtrack_index][1]
        moves_last_turn.append([up_down, left_right])

for key in chess_board:
    print("".join(chess_board[key]))
print("You win")
