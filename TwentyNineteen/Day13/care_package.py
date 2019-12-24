from TwentyNineteen import intcode
import sys


symbols = {
    0: " ",
    1: "#",
    2: "O",
    3: "_",
    4: "+"
}


def print_play_field(play_field):
    score = list(filter(lambda x: x[0] == -1 and x[1] == 0, play_field))
    # lines = []
    # for block in blocks:
    #     if block[0] >= 0 and block[1] >= 0:
    #         while block[1] >= len(lines):
    #             lines.append([])
    #         while block[0] >= len(lines[block[1]]):
    #             lines[block[1]].append([])
    #         lines[block[1]][block[0]] = symbols[block[2]]
    # for line in lines:
    #     sys.stdout.write("".join(line) + '\n')
    sys.stdout.write("\rPlayer Score: " + str(score[0][2]))
    sys.stdout.flush()


with open('input.txt', 'r') as file:
    nums = [int(x) for x in file.read().rstrip().split(',')]
    state = intcode.run(nums, [0], 0, 0)
    blocks = [state[4][x:x+3] for x in range(0, len(state[4]), 3)]
    print("Part one: " + str(len(list(filter(lambda y: y == 2, map(lambda x: x[2], blocks))))))
    nums[0] = 2
    intcode.init(nums, [], 0, 0)
    finished = False
    while not finished:
        state = intcode.run_code()
        blocks = [state[4][x:x+3] for x in range(0, len(state[4]), 3)]
        ball_blocks = list(filter(lambda x: x[2] == 4, blocks))
        paddle_blocks = list(filter(lambda x: x[2] == 3, blocks))
        joystick = 0
        if paddle_blocks[-1][0] < ball_blocks[-1][0]:
            joystick = 1
        elif paddle_blocks[-1][0] > ball_blocks[-1][0]:
            joystick = -1
        intcode.update([joystick], 0, 0)
        finished = not any(block[2] == 2 for block in blocks)
        print_play_field(blocks)
    # print("Part two: " + str(list(filter(lambda x: x[0] == -1 and x[1] == 0, blocks))[0][2]))
