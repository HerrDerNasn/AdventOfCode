with open('input.txt', 'r') as file:
    for line in file.readlines():
        nums = [line[i:i + 25] for i in range(0, len(line), 25)]
        picture = [nums[i:i + 6] for i in range(0, len(nums), 6)]
    decoded = [list('2222222222222222222222222'),list('2222222222222222222222222'),list('2222222222222222222222222'),list('2222222222222222222222222'),list('2222222222222222222222222'),list('2222222222222222222222222')]
    for number in picture:
        for i in range(0, 6):
            for x in range(0, 25):
                decoded[i][x] = number[i][x] if decoded[i][x] == '2' else decoded[i][x]
    for number in decoded:
        print(''.join(number))