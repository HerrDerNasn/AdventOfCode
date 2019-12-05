def read_input():
    f=open("input.txt", "r")
    if f.mode == 'r':
        nums = f.readlines()
        new_nums = []
        for num in nums:
            num = int(num.rstrip())
            new_nums.append(num)
        return new_nums


def calc_fuel(mass):
    return int(mass/3)-2


def main():
    nums = read_input()
    count = 0
    for num in nums:
        fuel = calc_fuel(num)
        count = count + fuel
    print(count)


if __name__ == "__main__":
    main()
