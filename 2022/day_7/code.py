def upDir(dir):
    dir_arr = dir.split("/")
    new_dir = "/".join(dir_arr[:-2]) + "/"
    return new_dir

def downDir(dir, folder):
    if folder == "/":
        dir = "/"
    elif dir == "/":
        dir = folder + "/"
    else:
        dir += folder + "/"
    return dir

def getCurrentLevel(dir_map, current_dir):
    current_level = dir_map
    for i in current_dir.split("/"):
        if i != "":
            current_level = current_level[i]
    return current_level

def mapArray(lines):
    dir_map = {}
    current_dir = ""
    for line in lines:
        if line[-1] == "\n":
            line = line[:-1]
        if line[0] == "$":
            if line[2:4] == "cd":
                if line[5:7] == "..":
                    current_dir = upDir(current_dir)
                else:
                    current_dir = downDir(current_dir, line[5:])
        elif line[0:3] == "dir":
            current_level = getCurrentLevel(dir_map, current_dir)
            current_level[line[4:]] = {}
        else:
            file = line.split()
            current_level = getCurrentLevel(dir_map, current_dir)
            current_level[file[1]] = int(file[0])
    return dir_map

def getDirSize(dir_map):
    size = 0
    for i in dir_map.keys():
        if isinstance(dir_map[i], int):
            size += dir_map[i]
        else:
            size += getDirSize(dir_map[i])
    return size

def getDirs(dir_map, current_dir):
    dirs = {}
    for i in dir_map.keys():
        if not isinstance(dir_map[i], int):
            dirs[downDir(current_dir, i)] = 0
            dirs.update(getDirs(dir_map[i], downDir(current_dir, i)))
    return dirs

def getDirSizes(dir_map):
    dirs = getDirs(dir_map, "")
    for i in dirs.keys():
        current_dir = dir_map
        for j in i.split("/")[:-1]:
            current_dir = current_dir[j]
        dirs[i] = getDirSize(current_dir)
    result = {}
    for k in dirs.keys():
        result[k] = dirs[k]
    return result

def run(lines):
    dir_map = mapArray(lines)
    dir_sizes = getDirSizes(dir_map)
    total = 0
    for i in dir_sizes.keys():
        if dir_sizes[i] <= 100000:
            total += dir_sizes[i]
    return total

def findClosestOver(dir_map, size):
    del_contender = getDirSize(dir_map)
    sizes = list(getDirSizes(dir_map).values())
    for i in sizes:
        if i > size and i < del_contender:
            del_contender = i
    return del_contender

def run2(lines):
    dir_map = mapArray(lines)
    del_size = getDirSize(dir_map) - 40000000
    return findClosestOver(dir_map, del_size)

with open('./input.txt') as f:
    lines = f.readlines()

#print(run(lines))

print(run2(lines))