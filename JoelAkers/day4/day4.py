import os
import numpy as np

def get_file_name():
    cur_dir = os.getcwd()
    advent_folder = "2021AdventOfCode"
    joel_folder = "JoelAkers"
    day_folder = "day4"
    test_file = "input.txt"
    full_folder = os.path.join(cur_dir, advent_folder, joel_folder, day_folder)
    full_path = os.path.join(full_folder, test_file)
    return full_path

def check_winner(board):
    for column in range(len(board[0])):
        col = [board[x][column] for x in range(len(board))]
        if all(col):
            return True, False, column
    for row in range(len(board)):
        if all(board[row]):
            return True, True, row
    return False, False, 0

def get_drawn_numbers(full_path):
    with open(full_path) as open_file:
        for line in open_file:
            numbers = line.split(",")
            return [int(x) for x in numbers]

def get_boards(full_path):
    boards = []
    with open(full_path) as open_file:
        for line in open_file:
            if len(line) > 2 and len(line) < 20:
                boards[-1].append([int(x) for x in line.split()])
            elif len(line) < 20:
                boards.append([])
    boards = list(filter(None, boards))
    return boards
    
def sum_unmarked(board, marked_board):
    sum = 0
    for row in range(len(board)):
        for column in range(len(board[0])):
            if marked_board[row][column] == False:
                sum += board[row][column]
    return sum
def play_num_on_board(boards, marked_boards, number, board_num):
    for row in range(len(boards[0])):
        for column in range(len(boards[0][0])):
            if boards[board_num][row][column] == number:
                marked_boards[board_num][row][column] = True
                winner, row_or_col, num = check_winner(marked_boards[board_num])
                if winner:
                    if row_or_col:
                        print("row: ", str(num))
                        row_values = boards[board_num][row]
                        print("row values: ", str(row_values))
                        print("number: ", str(number))
                        sum = sum_unmarked(boards[board_num], marked_boards[board_num])
                        print("sum: "+ str(sum))
                        print("answer: ", str(number * sum))
                        return True
                    else:
                        print("column: ", str(num))
                        column_values = [boards[board_num][x][column] for x in range(len(boards[board_num]))]
                        print("column values: ", str(column_values))
                        print("number: ", str(number))
                        sum = sum_unmarked(boards[board_num], marked_boards[board_num])
                        print("sum: "+ str(sum))
                        print("answer: ", str(number * sum))
                        return True
    return False

def play_game_1():
    full_path = get_file_name()
    number_draws = get_drawn_numbers(full_path)
    boards = get_boards(full_path)
    marked_boards = np.zeros(np.array(boards).shape).tolist()
    total_boards = len(boards)
    boards_to_pop = []
    for number in number_draws:
        for board_num in range(len(boards)):
            if play_num_on_board(boards, marked_boards, number, board_num):
                print("total boards: ", str(total_boards))
                print("current board number: ", str(len(boards)))
                boards_to_pop.append(board_num)
        if len(boards_to_pop) > 0:
            for board_num in reversed(boards_to_pop):
                boards.pop(board_num)
                marked_boards.pop(board_num)
        boards_to_pop = []

                            
    
if __name__ == "__main__":
    play_game_1()