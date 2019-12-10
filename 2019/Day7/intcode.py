from itertools import permutations

curr_input = 0
last_output = 0
phases = []
use_phase = True


def read_file():
    f = open("input.txt", "r")
    if f.mode == 'r':
        nums = f.read()
        nums = parse_input(nums)
        return nums


def parse_input(intcode):
    int_list = []
    split = intcode.split(',')
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
    global use_phase, last_output
    if op_code == 3:
        nums[nums[index+1]] = phases[0] if use_phase else curr_input
        use_phase = False
    if op_code == 4:
        last_output = nums[nums[index+1]]
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
    global curr_input, phases, last_output, use_phase
    nums = read_file()
    highest = 0
    for x in list(permutations([0,1,2,3,4])):
        for i in range(0,5):
            if i == 0:
                curr_input = 0
                phases = list(x)
            else:
                curr_input = last_output
            run_over_input(nums.copy())
            phases = phases[1:]
            use_phase = True
        highest = last_output if last_output > highest else highest
    print(highest)


if __name__ == "__main__":
    main()