from TwentyNineteen import intcode

dir_mods = {
    0: [0, -1],
    1: [1, 0],
    2: [0, 1],
    3: [-1, 0]
}


def to_key(pos):
    return str(pos[0]) + "," + str(pos[1])


def get_next_pos(pos, value, curr_direction):
    curr_direction = (curr_direction + (-1 if value == 0 else 1)) % 4
    return [pos[0] + dir_mods[curr_direction][0], pos[1] + dir_mods[curr_direction][1]], curr_direction


def from_key(key):
    return [int(key.split(",")[0]), int(key.split(",")[1])]


def print_colors(colors):
    x_vals = set(map(lambda x: from_key(x)[0], colors.keys()))
    y_vals = set(map(lambda y: from_key(y)[1], colors.keys()))
    widths = [min(x_vals), max(x_vals)]
    heights = [min(y_vals), max(y_vals)]
    rows = []
    index = -1
    for y in range(heights[0], heights[1]+1):
        index += 1
        rows.append("")
        for x in range(widths[0], widths[1]+1):
            value = 0 if to_key([x, y]) not in colors.keys() else colors[to_key([x, y])]
            rows[index] += " " if value == 0 else "#"
    for row in rows:
        print(row)


with open('input.txt', 'r') as file:
    nums = [int(x) for x in file.read().rstrip().split(',')]
    intcode.init(nums.copy(), [], 0, 0)
    curr_pos = [0, 0]
    direction = 0
    colors = {}
    finished = False
    while not finished:
        intcode.add_inputs([0 if to_key(curr_pos) not in colors.keys() else colors[to_key(curr_pos)]])
        state = intcode.run_code()
        colors[to_key(curr_pos)] = state[4][-2]
        curr_pos, direction = get_next_pos(curr_pos, state[4][-1], direction)
        finished = state[0][state[2]] == 99
    print("Part one: " + str(len(colors.keys())))
    intcode.init(nums.copy(), [], 0, 0)
    curr_pos = [0, 0]
    direction = 0
    colors = {"0,0": 1}
    finished = False
    while not finished:
        intcode.add_inputs([0 if to_key(curr_pos) not in colors.keys() else colors[to_key(curr_pos)]])
        state = intcode.run_code()
        colors[to_key(curr_pos)] = state[4][-2]
        curr_pos, direction = get_next_pos(curr_pos, state[4][-1], direction)
        finished = state[0][state[2]] == 99
    print("Part Two:")
    print_colors(colors)
