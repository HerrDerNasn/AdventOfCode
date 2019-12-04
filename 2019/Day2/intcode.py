def calcResult(numOne, numTwo):
    return 100 * numOne + numTwo

def parseInput(input):
    intList = []
    split = input.split(',')
    for num in split:
        intList.append(int(num))
    return intList

def runOverInput(input):
    nums = input.copy()
    currPos = 0
    while len(nums) > currPos and nums[currPos] != 99:
        code = nums[currPos]
        firstNum = nums[currPos + 1]
        secondNum = nums[currPos + 2]
        targetPos = nums[currPos + 3]
        if code == 1:
            nums[targetPos] = nums[firstNum] + nums[secondNum]
        elif code == 2:
            nums[targetPos] = nums[firstNum] * nums[secondNum]
        currPos += 4
    return nums

def main():
    f=open("input.txt", "r")
    if f.mode == 'r':
        nums = f.read()
        nums = parseInput(nums)
        indexOne = -1
        indexTwo = -1
        result = 0
        while result != 19690720 and indexOne < 100:
            indexOne += 1
            indexTwo = -1
            nums[1] = indexOne
            while result != 19690720 and indexTwo < 100:
                indexTwo += 1
                nums[2] = indexTwo
                newnums = runOverInput(nums)
                result = newnums[0]
        print(calcResult(newnums[1], newnums[2]))


if __name__== "__main__":
    main()