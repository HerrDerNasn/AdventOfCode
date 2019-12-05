def read_file():
    f = open("input.txt", "r")
    if f.mode == 'r':
        nums = f.read()
        nums = parse_input(nums)
        return nums


def parse_input(input):
    int_list = []
    split = input.split(',')
    for num in split:
        int_list.append(int(num))
    return int_list


def get_command(num):
    command_codes = {'E': num % 10}
    num = int(num / 10)
    command_codes['D'] = num % 10
    num = int(num / 10)
    command_codes['C'] = num % 10
    num = int(num / 10)
    command_codes['B'] = num % 10
    num = int(num / 10)
    command_codes['A'] = num % 10
    return command_codes


def process_two_length_instruction(nums, op_code, index):
    if op_code == 3:
        correct_input = False
        while not correct_input:
            try:
                user_input = int(input("Enter integer"))
                correct_input = True
            except ValueError:
                print("Not an integer! Try again.")
                continue
        nums[nums[index+1]] = user_input
    if op_code == 4:
        print(nums[nums[index+1]])
    return index + 2


def process_three_length_instruction(nums, op_code, index, param_one_mode, param_two_mode):
    value_one = bool(nums[index + 1] if param_one_mode == 1 else nums[nums[index + 1]])
    value_two = nums[index + 2] if param_two_mode == 1 else nums[nums[index + 2]]
    if op_code == 5 and value_one:
        return value_two
    elif op_code == 6 and not value_one:
        return value_two
    else:
        return index + 3


def process_four_length_instruction(nums, op_code, index, param_one_mode, param_two_mode, param_three_mode):
    value_one = nums[index + 1] if param_one_mode == 1 else nums[nums[index + 1]]
    value_two = nums[index + 2] if param_two_mode == 1 else nums[nums[index + 2]]
    if op_code == 1:
        nums[nums[index+3]] = value_one + value_two
    elif op_code == 2:
        nums[nums[index+3]] = value_one * value_two
    elif op_code == 7:
        nums[nums[index+3]] = 1 if value_one < value_two else 0
    elif op_code == 8:
        nums[nums[index+3]] = 1 if value_one == value_two else 0
    return index + 4


def run_over_input(orig_nums):
    nums = orig_nums.copy()
    curr_pos = 0
    while len(nums) > curr_pos and nums[curr_pos] != 99:
        comm_code = get_command(nums[curr_pos])
        op_code = comm_code['E']
        if op_code == 1 or op_code == 2 or op_code == 7 or op_code == 8:
            curr_pos = process_four_length_instruction(nums, comm_code['E'], curr_pos, comm_code['C'], comm_code['B'], comm_code['A'])
        elif op_code == 3 or op_code == 4:
            curr_pos = process_two_length_instruction(nums, comm_code['E'], curr_pos)
        elif op_code == 5 or op_code == 6:
            curr_pos = process_three_length_instruction(nums, comm_code['E'], curr_pos, comm_code['C'], comm_code['B'])
    return nums


def main():
    nums = read_file()
    run_over_input(nums)


if __name__ == "__main__":
    main()