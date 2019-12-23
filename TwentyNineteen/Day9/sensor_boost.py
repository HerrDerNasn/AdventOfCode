from TwentyNineteen import intcode

with open('input.txt', 'r') as file:
    nums = [int(x) for x in file.read().rstrip().split(',')]
    result = intcode.run(nums.copy(), [1], 0, 0)
    print("Part One: " + str(result[-1][-1]))
    result = intcode.run(nums.copy(), [2], 0, 0)
    print("Part Two: " + str(result[-1][-1]))
