
def sum3(cur_list):
    cur_sum = 0
    for num in cur_list:
        cur_sum += num
    return cur_sum

def slide_3(nums, num_list, next_index):
    if len(num_list) >= 3:
        num_list.pop(0)
    num_list.append(nums[next_index])

def get_increases(nums):
    prev_index = 0
    cur_index = 1
    num_increases = 0
    while cur_index < len(nums):
        if nums[cur_index] > nums[prev_index]:
            num_increases += 1
        prev_index += 1
        cur_index += 1
    return num_increases

def getFileOutput_1():
    with open('./input.txt') as open_file:
        data = []
        for line in open_file:
            data.append(int(line))
        increases = get_increases(data)
        print(increases)

def getFileOutput_3():
    with open('./input.txt') as open_file:
        input_data = []
        for line in open_file:
            input_data.append(int(line))
        list_vals = []
        sums_data = []
        for index_num in range(0, len(input_data)):
            slide_3(input_data, list_vals, index_num)
            if index_num > 1:
                sums_data.append(sum3(list_vals))
        
        
        increases = get_increases(sums_data)
        print(increases)

getFileOutput_3()