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
        new_nums = run_over_nums(nums)
        print(new_nums[0])


if __name__ == "__main__":
    main()
