import math


def init_detectable_amounts(width, height):
    detectable_amount = []
    for y in range(0, height):
        detectable_amount.append([])
        for x in range(0, width):
            detectable_amount[y].append(0)
    return detectable_amount


def check_multiple(top, bottom):
    if bottom == 0:
        return True
    if top == 0 and not bottom == 0:
        return False
    return top % bottom == 0


def calc_angle(orig_coord, target_coord):
    return math.atan2(target_coord[1]-orig_coord[1], target_coord[0]-orig_coord[0])


with open('input.txt', 'r') as file:
    asteroids = file.readlines()
    nums = init_detectable_amounts(26, 26)
    for x in range(0, 26):
        for y in range(0, 26):
            if asteroids[y][x] == "#":
                blocked = []
                for x2 in range(x, 26):
                    for y2 in range(y + 1 if x == x2 else 0, 26):
                        angle = calc_angle((x,y),(x2,y2))
                        if asteroids[y2][x2] == "#" and angle not in blocked:
                            nums[y][x] = nums[y][x] + 1
                            nums[y2][x2] = nums[y2][x2] + 1
                            blocked.append(angle)
    merged_nums = []
    for num in nums:
        merged_nums = merged_nums + num
    max_num = max(merged_nums)
    index = merged_nums.index(max_num)
    print(str((index % 26, int(index / 26))), max(merged_nums))
