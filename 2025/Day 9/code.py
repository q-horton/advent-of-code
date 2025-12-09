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

def run2(inp):
    data = parse(inp)
    max_area = 0
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
                    # Shouldn't work yet as it doesn't account for shapes
                    # outside the loop with no edges running through them
                    # It did though...
                else:
                    print(f"New max area: {area}. Currently at {i * len(data) + j} of {len(data) ** 2}")
                    max_area = area
    print(max_area)

with open('./input.txt') as f:
    lines = f.readlines()

run2(lines)
