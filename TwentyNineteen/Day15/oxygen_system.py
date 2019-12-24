from TwentyNineteen import intcode
import sys


class Position:
    x_coord = 0
    y_coord = 0
    result = 3
    neighbors = {}
    state = {}

    def __init__(self):
        self.neighbors = dict({
            1: {},
            2: {},
            3: {},
            4: {}
        })
        self.state = []

    def __repr__(self):
        return 'X=' + str(self.x_coord) + ', Y=' + str(self.y_coord) + 'N=' + str(
            list(map(lambda x: x.result, self.neighbors.values())))

    def __str__(self):
        return 'X=' + str(self.x_coord) + ', Y=' + str(self.y_coord) + 'N=' + str(
            list(map(lambda x: x.result, self.neighbors.values())))


movements = {
    1: [0, -1],
    2: [0, 1],
    3: [-1, 0],
    4: [1, 0]
}

opposites = {
    1: 2,
    2: 1,
    3: 4,
    4: 3
}


def find_target_position(x_coordinate, y_coordinate, list_of_positions):
    filtered = list(filter(lambda x: x.x_coord == x_coordinate and x.y_coord == y_coordinate, list_of_positions))
    if len(filtered) == 1:
        return filtered[0]
    return {}


def print_result(list_of_positions, list_of_visited):
    symbols = {
        0: "#",
        1: ".",
        2: "O",
        3: "S",
        4: "="
    }
    x_offset = min(list(map(lambda x: x.x_coord, list_of_positions))) - 1
    y_offset = min(list(map(lambda x: x.y_coord, list_of_positions))) - 1
    lines = []
    for position in list_of_positions:
        x, y = position.x_coord - x_offset, position.y_coord - y_offset
        while y >= len(lines):
            lines.append([])
        while x >= len(lines[y]):
            lines[y].append(' ')
        if any(position in visited for visited in list_of_visited):
            lines[y][x] = symbols[4]
        else:
            lines[y][x] = symbols[position.result]
    for line in lines:
        print("".join(line))


def next_positions(route):
    return list(filter(lambda x: (x.result == 1 or x.result == 2 or x.result == 3) and x not in route,
                       list(route[-1].neighbors.values())))


def has_next(route):
    return len(next_positions(route)) > 0


def find_shortest_route(initital_position):
    routes = [[initital_position]]
    hits = []
    while any(has_next(route) for route in routes):
        new_routes = []
        for route in routes:
            first = True
            for unvisited in next_positions(route):
                if unvisited.result == 2:
                    route.append(unvisited)
                    hits.append(route)
                    del routes[routes.index(route)]
                else:
                    if first:
                        route.append(unvisited)
                        first = False
                    else:
                        n_route = route[:-1].copy()
                        n_route.append(unvisited)
                        new_routes.append(n_route)
        routes += new_routes
    return min(list(map(lambda x: len(x) - 1, hits)))


def find_longest_route(initital_position):
    routes = [[initital_position]]
    while any(has_next(route) for route in routes):
        new_routes = []
        for route in routes:
            first = True
            for unvisited in next_positions(route):
                if first:
                    route.append(unvisited)
                    first = False
                else:
                    n_route = route[:-1].copy()
                    n_route.append(unvisited)
                    new_routes.append(n_route)
        routes += new_routes
    return max(list(map(lambda x: len(x) - 1, routes)))


with open('input.txt', 'r') as file:
    nums = [int(x) for x in file.read().rstrip().split(',')]
    init_pos = Position()
    init_pos.state = [nums, [1], 0, 0, [], 0]
    all_positions = [init_pos]
    while any(any(neighbor == {} for neighbor in position.neighbors.values()) for position in all_positions):
        new_positions = []
        for curr_position in all_positions:
            for direction in list(filter(lambda x: curr_position.neighbors[x] == {}, curr_position.neighbors.keys())):
                result = intcode.run(curr_position.state[0], [direction], curr_position.state[2], 0,
                                     curr_position.state[5])
                status_code = result[4][-1]
                x_coord = curr_position.x_coord + movements[direction][0]
                y_coord = curr_position.y_coord + movements[direction][1]
                next_pos = find_target_position(x_coord, y_coord, all_positions)
                if next_pos == {}:
                    next_pos = Position()
                    next_pos.x_coord = x_coord
                    next_pos.y_coord = y_coord
                    next_pos.state = result
                    next_pos.result = status_code
                    if status_code == 0:
                        next_pos.neighbors = dict({
                            1: -1,
                            2: -1,
                            3: -1,
                            4: -1
                        })
                    new_positions.append(next_pos)
                next_pos.neighbors[opposites[direction]] = curr_position
                curr_position.neighbors[direction] = next_pos
        all_positions = all_positions + new_positions
    print_result(all_positions, [])
    print("Part One: " + str(find_shortest_route(init_pos)))
    print("Part Two: " + str(find_longest_route(list(filter(lambda x: x.result == 2, all_positions))[-1])))
