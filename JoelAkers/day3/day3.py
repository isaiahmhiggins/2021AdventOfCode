import os


def convert_binary_to_decimal(binary_list):
    return int("".join(str(i) for i in binary_list), 2)

def get_file_name():
    cur_dir = os.getcwd()
    advent_folder = "2021AdventOfCode"
    joel_folder = "JoelAkers"
    day_folder = "day3"
    test_file = "input.txt"
    full_folder = os.path.join(cur_dir, advent_folder, joel_folder, day_folder)
    full_path = os.path.join(full_folder, test_file)
    return full_path

def get_input_binary():
    input_binary = [[]]
    full_path = get_file_name()
    with open(full_path) as open_file:
        for line in open_file:
            for bin_num in line:
                if bin_num.isdigit():
                    input_binary[-1].append(int(bin_num))
            input_binary.append([])
    return input_binary[0:-1]

def get_oxygen():
    input_binary = get_input_binary()

    for bit in range(len(input_binary)):
        if len(input_binary) == 1:
            return convert_binary_to_decimal(input_binary[0])
        column = [input_binary[x][bit] for x in range(len(input_binary))]
        most_common = 1
        if column.count(0) > column.count(1):
            most_common = 0
        for line_num in reversed(range(len(input_binary))):
            if input_binary[line_num][bit] != most_common:
                input_binary.pop(line_num)
    return convert_binary_to_decimal(input_binary[0])
def get_CO2():
    input_binary = get_input_binary()

    for bit in range(len(input_binary)):
        if len(input_binary) == 1:
            return convert_binary_to_decimal(input_binary[0])
        column = [input_binary[x][bit] for x in range(len(input_binary))]
        least_common = 0
        if column.count(0) > column.count(1):
            least_common = 1
        for line_num in reversed(range(len(input_binary))):
            if input_binary[line_num][bit] != least_common:
                input_binary.pop(line_num)
    return convert_binary_to_decimal(input_binary[0])

def get_Ox_CO2():
    ox = get_oxygen()
    co2 = get_CO2()
    print("oxygen: ", str(ox))
    print("CO2: ", str(co2))
    print("result: ", str(ox*co2))

def get_gamma_binary():
    input_binary = get_input_binary()
    gamma_bits = []
    epsilon_bits = []
    for bit in range(len(input_binary[0])):
        column = [input_binary[x][bit] for x in range(len(input_binary)-1)]
        if column.count(0) > column.count(1):
            gamma_bits.append(0)
            epsilon_bits.append(1)
        else:
            gamma_bits.append(1)
            epsilon_bits.append(0)

    print("gamme binary: ", str(gamma_bits))
    gamma_decimal = convert_binary_to_decimal(gamma_bits)
    print("gamme decimal: ", str(gamma_decimal))
    print("epsilon binary: ", str(epsilon_bits))
    epsilon_decimal = convert_binary_to_decimal(epsilon_bits)
    print("epsilon decimal: ", str(epsilon_decimal))
    print("power: ", str(epsilon_decimal * gamma_decimal))

    

if __name__ == "__main__":
    get_Ox_CO2()