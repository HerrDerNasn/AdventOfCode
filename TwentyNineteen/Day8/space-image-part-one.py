with open('input.txt', 'r') as file:
    for line in file.readlines():
        nums = [line[i:i + 25] for i in range(0, len(line), 25)]
        picture = [nums[i:i + 6] for i in range(0, len(nums), 6)]
    lowest_zero_count = ''
    for number in picture:
        lowest_zero_count = number if sum([num.count('0') for num in number]) < \
                                      sum([num.count('0') for num in lowest_zero_count]) or lowest_zero_count == '' \
            else lowest_zero_count
    print(lowest_zero_count)
    print(sum([num.count('1') for num in lowest_zero_count]) * sum([num.count('2') for num in lowest_zero_count]))
