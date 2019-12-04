def calcFuel(mass):
    return int(mass/3)-2

def extraFuel(fuel):
    extra = fuel
    while extra > 0:
        extraFuel = calcFuel(extra)
        if extraFuel > 0:
            extra = extraFuel
            fuel += extra
        else:
            extra = 0
    return fuel

def main():
    f=open("input.txt", "r")
    if f.mode == 'r':
        nums = f.readlines()
        newNums = []
        for num in nums:
            num = int(num.rstrip())
            newNums.append(num)
        count = 0
        for num in newNums:
            fuel = calcFuel(num)
            fuel = extraFuel(fuel)
            count = count + fuel
        print(count)

if __name__== "__main__":
    main()