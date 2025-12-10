def parse(lines):
    vals = []
    for line in lines:
        vals.append(tuple([int(i) for i in line.strip().split(',')]))
    return vals

def run(inp):
    data = parse(inp)
    max_area = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            area = (abs(data[i][0] - data[j][0]) + 1) * (abs(data[i][1] - data[j][1]) + 1)
            if area > max_area:
                max_area = area
    print(max_area)

def in_shape(corners, edges, point):
    if point in edges:
        return True
    intersects = 0
    on_edge = False
    left = False
    for x in range(-1, point[0]):
        if on_edge:
            if (x, point[1]) in corners:
                on_edge = False
                if (left and (x, point[1] + 1) in edges) or \
                        not (left or (x, point[1] + 1) in edges):
                    intersects += 1
        elif (x, point[1]) in corners:
            on_edge = True
            if (x, point[1] + 1) in edges:
                left = False
            else:
                left = True
        elif (x, point[1]) in edges:
            intersects += 1
    return True if intersects % 2 == 1 else False

def run2(inp):
    data = parse(inp)
    max_area = 0
    edges = set()
    for i in range(len(data)):
        x_vals = [data[i][0], data[(i+1) % len(data)][0]]
        x_vals.sort()
        y_vals = [data[i][1], data[(i+1) % len(data)][1]]
        y_vals.sort()
        if x_vals[0] == x_vals[1]:
            for y in range(y_vals[0], y_vals[1] + 1):
                edges.add((x_vals[0], y))
        else:
            for x in range(x_vals[0], x_vals[1] + 1):
                edges.add((x, y_vals[0]))
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            x_vals = [data[i][0], data[j][0]]
            x_vals.sort()
            y_vals = [data[i][1], data[j][1]]
            y_vals.sort()
            area = (x_vals[1] - x_vals[0] + 1) * (y_vals[1] - y_vals[0] + 1)
            if area > max_area:
                for k in range(len(data)):
                    if k == i or k == j:
                        continue
                    x, y = data[k]
                    if x_vals[0] < x < x_vals[1] and y_vals[0] < y < y_vals[1]:
                        break
                    nx, ny = data[(k + 1) % len(data)]
                    if x_vals[0] < x < x_vals[1]:
                        if x == nx:
                            if y <= y_vals[0] and y_vals[0] < ny:
                                break
                            if y >= y_vals[1] and y_vals[1] > ny:
                                break
                    if y_vals[0] < y < y_vals[1]:
                        if y == ny:
                            if x <= x_vals[0] and x_vals[0] < nx:
                                break
                            if x >= x_vals[1] and x_vals[1] > nx:
                                break
                else:
                    midpoint = (sum(x_vals) // 2, sum(y_vals) // 2)
                    if not in_shape(data, edges, midpoint):
                        continue
                    print(f"New max area: {area}. Currently at {i * len(data) + j} of {len(data) ** 2}")
                    max_area = area
    print(max_area)

with open('./input.txt') as f:
    lines = f.readlines()

run2(lines)
