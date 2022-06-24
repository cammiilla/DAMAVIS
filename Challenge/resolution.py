import numpy as np 


def board_maker(board_dimentions,snake_position):

    rows = board_dimentions[0]
    colunms = board_dimentions[1]

    snake_lenth = len(snake_position)

    board = np.zeros((rows, colunms))

    for i in range(snake_lenth):
        if i == 0:
            row = snake_position[i][0]
            colunm = snake_position[i][1]
            board[row][colunm] = 2
        else:
            row = snake_position[i][0]
            colunm = snake_position[i][1]
            board[row][colunm] = 1
    return board 

def new_snake_position(snake_position,movement):
    
    copy_snake_position = snake_position.copy()
    copy_snake_position.insert(0, movement)
    del copy_snake_position[-1]
    return copy_snake_position

def movement_test(snake_head,board_dimentions,board):

    # Board limit coordnates
    row_limit = board_dimentions[0] - 1
    colunm_limit = board_dimentions[1] - 1

    movements = {"R": [0, 1], "D": [1, 0], "L": [0, -1], "U": [-1, 0]}
    candidates_movements = []
    for move in movements.items():
        value = move[1]
        key = move[0]

        # Sum the snake_head coordinate with the movements coordinates
        new_position = list(map(lambda v1, v2: v1 + v2, value, snake_head))
        # Test for the board limits
        if new_position[0] <= row_limit and new_position[1] <= colunm_limit and new_position[0] >= 0 and new_position[1] >= 0:

            new_position_row = new_position[0]
            new_position_colunm = new_position[1]
            
            # Test for the snake body limits
            if board[new_position_row,new_position_colunm] == 0:
                candidates_movements.append(new_position)

    return candidates_movements

def nexts_movements(board_dimentions,snake_position,depth):
    if depth == 0:
        return "End of Sequence"
    else: 

        board = board_maker(board_dimentions,snake_position)
        head = snake_position[0]
        possibles_movements = movement_test(head, board_dimentions, board)
        number_of_possibles_movements = len(possibles_movements)
        dicio = {}
        for n in range(number_of_possibles_movements):
            change_snake_position = new_snake_position(snake_position,possibles_movements[n])
            possible_movement = possibles_movements[n]
            dicio[str(possible_movement)] = nexts_movements(board_dimentions,change_snake_position,depth-1)
        return dicio

board_dimentions = [4, 3]
snake_position = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
depth = 3

result = nexts_movements(board_dimentions,snake_position,depth)
result = str(result)
result.count('End of Sequence')
