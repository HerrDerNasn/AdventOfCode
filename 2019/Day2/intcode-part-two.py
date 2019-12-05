def calc_result(num_one, num_two):
    return 100 * num_one + num_two


def parse_input(input_string):
    int_list = []
    split = input_string.split(',')
    for num in split:
        int_list.append(int(num))
    return int_list


def run_over_nums(orig_nums):
    nums = orig_nums.copy()
    curr_pos = 0
    while len(nums) > curr_pos and nums[curr_pos] != 99:
        code = nums[curr_pos]
        first_num = nums[curr_pos + 1]
        second_num = nums[curr_pos + 2]
        target_pos = nums[curr_pos + 3]
        if code == 1:
            nums[target_pos] = nums[first_num] + nums[second_num]
        elif code == 2:
            nums[target_pos] = nums[first_num] * nums[second_num]
        curr_pos += 4
    return nums


def main():
    f = open("input.txt", "r")
    if f.mode == 'r':
        nums = f.read()
        nums = parse_input(nums)
        index_one = -1
        index_two = -1
        result = 0
        while result != 19690720 and index_one < 100:
            index_one += 1
            index_two = -1
            nums[1] = index_one
            while result != 19690720 and index_two < 100:
                index_two += 1
                nums[2] = index_two
                new_nums = run_over_nums(nums)
                result = new_nums[0]
        print(calc_result(new_nums[1], new_nums[2]))


if __name__ == "__main__":
    main()
