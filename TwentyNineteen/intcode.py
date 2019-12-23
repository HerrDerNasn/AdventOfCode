class IntcodeException(Exception):
    pass


gNumbers = []
gCurrPos = 0
gInputs = []
gCurrInput = 0
gOutputs = []
gRelativeBase = 0


def get_index(num, mod):
    return num if mod == 0 else gRelativeBase + num


def get_num(num, mod):
    global gNumbers, gRelativeBase
    return num if mod == 1 else get_num_at(get_index(num, mod)) if mod == 0 else get_num_at(get_index(num, mod))


def get_num_at(index):
    global gNumbers
    if index >= len(gNumbers):
        return 0
    return gNumbers[index]


def set_num_at(index, value):
    global gNumbers
    if index >= len(gNumbers):
        for i in range(index - len(gNumbers) + 1):
            gNumbers.append(0)
    gNumbers[index] = value


def op_code_one(block, modifier):
    global gNumbers, gCurrPos
    num_one = get_num(block[0], modifier[0])
    num_two = get_num(block[1], modifier[1])
    set_num_at(get_index(block[2], modifier[2]), num_one + num_two)
    return gCurrPos + 4


def op_code_two(block, modifier):
    global gNumbers, gCurrPos
    num_one = get_num(block[0], modifier[0])
    num_two = get_num(block[1], modifier[1])
    set_num_at(get_index(block[2], modifier[2]), num_one * num_two)
    return gCurrPos + 4


def op_code_three(block, modifier):
    global gNumbers, gInputs, gCurrInput, gCurrPos
    if gCurrInput >= len(gInputs):
        raise IntcodeException("inputs")
    set_num_at(get_index(block[0], modifier[0]), gInputs[gCurrInput])
    gCurrInput = gCurrInput + 1
    return gCurrPos + 2


def op_code_four(block, modifier):
    global gNumbers, gCurrPos, gOutputs
    gOutputs.append(get_num(block[0], modifier[0]))
    return gCurrPos + 2


def op_code_five(block, modifier):
    global gCurrPos
    num_one = get_num(block[0], modifier[0])
    num_two = get_num(block[1], modifier[1])
    if num_one != 0:
        return num_two
    return gCurrPos + 3


def op_code_six(block, modifier):
    global gCurrPos
    num_one = get_num(block[0], modifier[0])
    num_two = get_num(block[1], modifier[1])
    if num_one == 0:
        return num_two
    return gCurrPos + 3


def op_code_seven(block, modifier):
    global gNumbers, gCurrPos
    num_one = get_num(block[0], modifier[0])
    num_two = get_num(block[1], modifier[1])
    set_num_at(get_index(block[2], modifier[2]), 1 if num_one < num_two else 0)
    return gCurrPos + 4


def op_code_eight(block, modifier):
    global gNumbers, gCurrPos
    num_one = get_num(block[0], modifier[0])
    num_two = get_num(block[1], modifier[1])
    set_num_at(get_index(block[2], modifier[2]), 1 if num_one == num_two else 0)
    return gCurrPos + 4


def op_code_nine(block, modifier):
    global gRelativeBase
    gRelativeBase += get_num(block[0], modifier[0])
    return gCurrPos + 2


split_length = {
    1: 4,
    2: 4,
    3: 2,
    4: 2,
    5: 3,
    6: 3,
    7: 4,
    8: 4,
    9: 2
}

op_fn = {
    1: op_code_one,
    2: op_code_two,
    3: op_code_three,
    4: op_code_four,
    5: op_code_five,
    6: op_code_six,
    7: op_code_seven,
    8: op_code_eight,
    9: op_code_nine
}


def run(numbers, inputs, position, input_position):
    global gNumbers, gInputs, gCurrPos, gCurrInput, gRelativeBase
    gNumbers = numbers.copy()
    gInputs = inputs.copy()
    gCurrPos = position
    gCurrInput = input_position
    gRelativeBase = 0
    return run_internal()


def run_internal():
    global gCurrPos, gNumbers, gCurrInput, gInputs
    op_code, modifier = get_op_code()
    while op_code != 99:
        if op_code in split_length.keys():
            try:
                curr_block = gNumbers[gCurrPos + 1: gCurrPos + split_length[op_code]]
                gCurrPos = op_fn[op_code](curr_block, modifier)
            except IntcodeException as error:
                return gNumbers, gInputs, gCurrPos, gCurrInput, gOutputs
        op_code, modifier = get_op_code()
    return gNumbers, gInputs, gCurrPos, gCurrInput, gOutputs


def get_op_code():
    global gCurrPos, gNumbers
    num = gNumbers[gCurrPos]
    op_code = num % 100
    num = int(num / 100)
    modifier = []
    for i in range(3):
        modifier.append(num % 10)
        num = int(num / 10)
    return op_code, modifier
