def parse(lines):
    sensors = []
    for line in lines:
        line = line.strip()
        i = line.split()
        s_x = int(i[2][2:-1])
        s_y = int(i[3][2:-1])
        b_x = int(i[8][2:-1])
        b_y = int(i[9][2:])
        sensors.append([(s_x, s_y), (b_x, b_y)])
    return sensors

def manhattan(v1, v2):
    return abs(v1[0] - v2[0]) + abs(v1[1] - v2[1])

def run(lines, row):
    parsed_data = parse(lines)
    beacons = []
    not_beacons = 0
    bounds = [None, None]
    for i in parsed_data:
        dist = manhattan(i[0], i[1])
        if i[1][1] == row:
            beacons.append(i[1][0])
        if (bounds[0] == None) or (i[0][0] - dist < bounds[0]):
            bounds[0] = i[0][0] - dist
        if (bounds[1] == None) or (i[0][0] + dist > bounds[1]):
            bounds[1] = i[0][0] + dist
    for x in range(bounds[0], bounds[1] + 1):
        if x in beacons:
            continue
        else:
            for i in parsed_data:
                if manhattan(i[0], (x, row)) <= manhattan(i[0], i[1]):
                    not_beacons += 1
                    break
    return not_beacons

def checkPoint(parsed_data, point):
    result = True
    for j in parsed_data:
        if manhattan(j[0], point) <= manhattan(j[0], j[1]):
            result = False
            break
    return result

def run2(lines, upper):
    parsed_data = parse(lines)
    for sensor in parsed_data:
        dist = manhattan(sensor[0], sensor[1])
        x,y = sensor[0]
        for i in range(dist + 2):
            if (x-i >= 0) and (y-dist-1+i >= 0):
                if checkPoint(parsed_data, (x-i, y-dist-1+i)):
                    return (x-i) * 4000000 + (y-dist-1+i)
            elif (x-i >= 0) and (y+dist+1-i <= upper):
                if checkPoint(parsed_data, (x-i, y+dist+1-i)):
                    return (x-i) * 4000000 + (y+dist+1-i)
            elif (x+i <= upper) and (y-dist-1+i >= 0):
                if checkPoint(parsed_data, (x+i, y-dist-1+i)):
                    return (x+i) * 4000000 + (y-dist-1+i)
            elif (x+i <= upper) and (y+dist+1-i <= upper):
                if checkPoint(parsed_data, (x+i, y+dist+1-i)):
                    return (x+i) * 4000000 + (y+dist+1-i)

with open('./input.txt') as f:
    lines = f.readlines()

#print(run(lines, 2000000))

print(run2(lines, 4000000))