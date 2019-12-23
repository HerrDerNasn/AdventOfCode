from itertools import permutations
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
    highest = 0
    for x in list(permutations([0, 1, 2, 3, 4])):
        phases = list(x)
        amplification_signal = 0
        for i in range(0, 5):
            result = intcode.run(nums, [phases[i], amplification_signal], 0, 0)
            amplification_signal = result[4][-1]
        highest = amplification_signal if amplification_signal > highest else highest
    print("Part one: " + str(highest))
    highest = 0
    for x in list(permutations([5, 6, 7, 8, 9])):
        phases = list(x)
        amplification_signal = 0
        states = [
            [nums.copy(), [phases[0]], 0, 0, []],
            [nums.copy(), [phases[1]], 0, 0, []],
            [nums.copy(), [phases[2]], 0, 0, []],
            [nums.copy(), [phases[3]], 0, 0, []],
            [nums.copy(), [phases[4]], 0, 0, []]
        ]
        all_finished = False
        while not all_finished:
            for i in range(0, 5):
                states[i][1].append(amplification_signal)
                states[i] = list(intcode.run(states[i][0], states[i][1], states[i][2], states[i][3]))
                amplification_signal = states[i][4][-1]
            all_finished = all(state[0][state[2]] == 99 for state in states)
        highest = amplification_signal if amplification_signal > highest else highest
    print("Part two: " + str(highest))


if __name__ == "__main__":
    main()
