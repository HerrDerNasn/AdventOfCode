class Input:
    direction = ''
    distance = 0

    def parse(self, inputStr):
        self.direction = inputStr[0:1]
        self.distance = int(inputStr[1:])

def parseInput():
    f=open("input.txt", "r")
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

def buildPosMap(wire):
    x = 0
    y = 0
    totalsteps = 0
    posMap = {}
    for input in wire:
        steps = 0
        while steps < input.distance:
            if input.direction == "R":
                x += 1
            elif input.direction == "U":
                y -= 1
            elif input.direction == "L":
                x -= 1
            else:
                y += 1
            steps += 1
            totalsteps += 1
            if not (x,y) in posMap:
                posMap[(x,y)] = totalsteps
    return posMap

def findCrossings(posMap, wire):
    x = 0
    y = 0
    crossings = []
    for input in wire:
        steps = 0
        while steps < input.distance:
            if input.direction == "R":
                x += 1
            elif input.direction == "U":
                y -= 1
            elif input.direction == "L":
                x -= 1
            else:
                y += 1
            steps += 1
            if (x,y) in posMap:
                crossings.append((x,y))
    return crossings

def countCombinedSteps(posMap, wire):
    x = 0
    y = 0
    totalsteps = 0
    crossings = {}
    for input in wire:
        steps = 0
        while steps < input.distance:
            if input.direction == "R":
                x += 1
            elif input.direction == "U":
                y -= 1
            elif input.direction == "L":
                x -= 1
            else:
                y += 1
            steps += 1
            totalsteps += 1
            if (x,y) in posMap:
                if not (x,y) in crossings:
                    crossings[(x,y)] = posMap[(x,y)] + totalsteps
    return crossings

def main():
    wires = parseInput()
    posMap = buildPosMap(wires[0])
    crossings = countCombinedSteps(posMap, wires[1])
    distance = -1
    for crossing in crossings.values():
        if distance == -1 or crossing < distance:
            distance = crossing
    print(distance)

if __name__== "__main__":
    main()