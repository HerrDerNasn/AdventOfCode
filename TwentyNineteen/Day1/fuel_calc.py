def read_input():
    f = open("input.txt", "r")
    if f.mode == 'r':
        nums = f.readlines()
        new_nums = []
        for num in nums:
            num = int(num.rstrip())
            new_nums.append(num)
        return new_nums


def calc_fuel(mass):
    return int(mass / 3) - 2


def extra_fuel(fuel):
    extra = fuel
    while extra > 0:
        extra_mass = calc_fuel(extra)
        if extra_mass > 0:
            extra = extra_mass
            fuel += extra
        else:
            extra = 0
    return fuel


def main():
    nums = read_input()
    p1_count = 0
    p2_count = 0
    for num in nums:
        base_fuel = calc_fuel(num)
        bonus_fuel = extra_fuel(base_fuel)
        p1_count = p1_count + base_fuel
        p2_count = p2_count + bonus_fuel
    print("Part 1: " + str(p1_count))
    print("Part 2: " + str(p2_count))


if __name__ == "__main__":
    main()
