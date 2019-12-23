class Input:
    direction = ''
    distance = 0

    def parse(self, input_str):
        self.direction = input_str[0:1]
        self.distance = int(input_str[1:])


dir_map = {
    'R': (1, 0),
    'U': (0, -1),
    'L': (-1, 0),
    'D': (0, 1)
}


def step(pos, direction):
    return pos[0] + dir_map[direction][0], pos[1] + dir_map[direction][1]


def parse_input():
    f = open("input.txt", "r")
    if f.mode == 'r':
        lines = f.readlines()
        wires = []
        for line in lines:
            split = line.split(",")
            wire = []
            for string in split:
                input = Input()
                input.parse(string)
                wire.append(input)
            wires.append(wire)
        return wires


def build_pos_map(wire):
    pos = (0, 0)
    total_steps = 0
    pos_map = {}
    for line in wire:
        steps = 0
        while steps < line.distance:
            pos = step(pos, line.direction)
            steps += 1
            total_steps += 1
            if pos not in pos_map:
                pos_map[pos] = total_steps
    return pos_map


def find_crossings(pos_map, wire):
    pos = (0, 0)
    crossings = []
    for line in wire:
        steps = 0
        while steps < line.distance:
            pos = step(pos, line.direction)
            steps += 1
            if pos in pos_map:
                crossings.append(pos)
    return crossings


def count_combined_steps(pos_map, wire):
    pos = (0, 0)
    total_steps = 0
    crossings = {}
    for line in wire:
        steps = 0
        while steps < line.distance:
            pos = step(pos, line.direction)
            steps += 1
            total_steps += 1
            if pos in pos_map and pos not in crossings:
                crossings[pos] = pos_map[pos] + total_steps
    return crossings


def main():
    wires = parse_input()
    pos_map = build_pos_map(wires[0])
    crossings = count_combined_steps(pos_map, wires[1])
    print(min(crossings.values()))


if __name__ == "__main__":
    main()
