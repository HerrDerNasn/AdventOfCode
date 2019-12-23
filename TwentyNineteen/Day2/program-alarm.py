from TwentyNineteen import intcode


def parse_input(input_string):
    int_list = []
    split = input_string.split(',')
    for num in split:
        int_list.append(int(num))
    return int_list


def main():
    f = open("input.txt", "r")
    if f.mode == 'r':
        nums = f.read()
        nums = parse_input(nums)
        new_nums = intcode.run(nums, [], 0, 0)
        print("Part One: " + str(new_nums[0][0]))
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
                new_nums = intcode.run(nums, [], 0, 0)
                result = new_nums[0][0]
        print("Part Two: " + str(100 * index_one + index_two))


if __name__ == "__main__":
    main()
