from TwentyNineteen import intcode


def read_file():
    f = open("input.txt", "r")
    if f.mode == 'r':
        nums = f.read()
        nums = parse_input(nums)
        return nums


def parse_input(input_str):
    int_list = []
    split = input_str.split(',')
    for num in split:
        int_list.append(int(num))
    return int_list


def main():
    nums = read_file()
    print(intcode.run(nums, [5], 0, 0))


if __name__ == "__main__":
    main()
