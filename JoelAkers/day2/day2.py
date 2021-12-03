import os

def get_file_name():
    cur_dir = os.getcwd()
    advent_folder = "2021AdventOfCode"
    joel_folder = "JoelAkers"
    day_folder = "day2"
    test_file = "input.txt"
    full_folder = os.path.join(cur_dir, advent_folder, joel_folder, day_folder)
    full_path = os.path.join(full_folder, test_file)
    return full_path

def get_position_aim():
    horiz = 0
    depth = 0
    aim = 0
    full_path = get_file_name()
    with open(full_path) as open_file:
        for line in open_file:
            parsed_line = line.split(" ")
            command = parsed_line[0]
            number = int(parsed_line[1])
            if command.startswith("forward"):
                depth += number*aim
                horiz += number
            elif command.startswith("up"):
                aim -= number
            elif command.startswith("down"):
                aim += number
    print("horiz: ", horiz)
    print("depth: ", depth)
    print("result: ", horiz * depth)

def get_position_mult():
    horiz = 0
    depth = 0
    full_path = get_file_name()
    with open(full_path) as open_file:
        for line in open_file:
            parsed_line = line.split(" ")
            command = parsed_line[0]
            number = int(parsed_line[1])
            if command.startswith("for"):
                horiz += number
            elif command.startswith("up"):
                depth -= number
            elif command.startswith("down"):
                depth += number
    print("horiz: ", horiz)
    print("depth: ", depth)
    print("result: ", horiz * depth)

get_position_aim()