import math


def calc_angle(orig_coord, target_coord):
    return math.atan2(target_coord[1] - orig_coord[1], target_coord[0] - orig_coord[0])


def sort_by_dist(val):
    return math.sqrt(val[0]*val[0]+val[1]*val[1])


def sort_angles(val):
    return val if val >= calc_angle((0, 0), (0, -1)) else val + 2 * math.pi


with open('input.txt', 'r') as file:
    asteroids = file.readlines()
    angle_mapping = {}
    station = (20, 19)
    # print("(1, 0) || 90", calc_angle((0, 0), (1, 0)))
    # print("(0, 1) || 180", calc_angle((0, 0), (0, 1)))
    # print("(-1, 0) || 270", calc_angle((0, 0), (-1, 0)))
    # print("(0, -1) || 0", calc_angle((0, 0), (0, -1)))
    for x in range(0, 26):
        for y in range(0, 26):
            if not station == (x, y):
                angle = calc_angle(station, (x, y))
                if asteroids[y][x] == "#":
                    if angle not in angle_mapping.keys():
                        angle_mapping[angle] = []
                    angle_mapping[angle].append((x-station[0], y-station[1]))
                    angle_mapping[angle].sort(key=sort_by_dist)
    angles = list(angle_mapping.keys())
    angles.sort(key=sort_angles)
    curr_ast = 0
    curr_angle_ind = 0
    while any(len(targets) > 0 for targets in angle_mapping.values()):
        targets = angle_mapping[angles[curr_angle_ind]]
        if len(targets) > 0:
            curr_ast += 1
            print(str(curr_ast) + ": Deleting " + str((station[0]+targets[0][0], station[1]+targets[0][1])))
            targets = targets[1:]
            angle_mapping[angles[curr_angle_ind]] = targets
        curr_angle_ind = curr_angle_ind + 1 if curr_angle_ind + 1 in range(0, len(angles)) else 0