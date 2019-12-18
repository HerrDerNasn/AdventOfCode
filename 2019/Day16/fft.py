base_pattern = [0, 1, 0, -1]


def get_digits():
    return {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}


def calc(number, idx):
    block_length = idx + 1
    mult = 1
    digits = get_digits()
    for i in range(idx, len(number), block_length * 2):
        for digit in number[i:i+block_length]:
            if digit != "0":
                digits[digit] += mult
        mult *= -1
    num = sum([int(x) * digits[x] for x in digits.keys()])
    return str(num)[-1:]


def calc_part_two(number, idx, last_num):
    num = last_num + int(number[idx])
    return str(num)[-1:], num


def part_one(number):
    nums = number
    for phase in range(100):
        new_nums = ""
        for index in range(len(nums)):
            new_nums = new_nums + calc(nums, index)
        nums = new_nums
    print("Part One: " + nums[:8])


def part_two(number):
    number *= 10000
    print(len(number))
    target_digits = int(number[:7])
    for phase in range(100):
        new_nums = ""
        last_num = 0
        for index in range(len(number)-1, target_digits-1, -1):
            digit, last_num = calc_part_two(number, index, last_num)
            new_nums = digit + new_nums
        number = number[:target_digits] + new_nums
        print("Phase " + str(phase + 1) + " finished")
    print(target_digits, number[target_digits:8])


with open('input.txt', 'r') as file:
    nums = file.read().rstrip()
    # part_one(nums)
    part_two(nums)
