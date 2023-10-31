def vecSize(vec):
    return (vec[0] ** 2 + vec[1] ** 2) ** 0.5

def vecAdd(vec1, vec2):
    return (vec1[0] + vec2[0], vec1[1] + vec2[1])

def relVec(vec1, vec2):
    return (vec2[0] - vec1[0], vec2[1] - vec1[1])

def move(rel_vec, mov_vec):
    move_x = 0
    move_y = 0
    new_h_x = vecAdd(rel_vec, mov_vec)[0]
    new_h_y = vecAdd(rel_vec, mov_vec)[1]
    if abs(new_h_x) == 2:
        move_x = int(new_h_x / abs(new_h_x))
    elif abs(new_h_x) > 0 and abs(new_h_y) == 2:
        move_x = int(new_h_x / abs(new_h_x))
    if abs(new_h_y) == 2:
        move_y = int(new_h_y / abs(new_h_y))
    elif abs(new_h_y) > 0 and abs(new_h_x) == 2:
        move_y = int(new_h_y / abs(new_h_y))
    return (move_x, move_y)

def dirToVec(dir):
    match(dir):
        case "U":
            return (0, 1)
        case "R":
            return (1, 0)
        case "D":
            return (0, -1)
        case "L":
            return (-1, 0)

def parse(lines):
    moves = []
    for line in lines:
        if line[-1] == "\n":
            line = line[:-1]
        com = line.split()
        for i in range(int(com[1])):
            moves.append(com[0])
    vecs = []
    for move in moves:
        vecs.append(dirToVec(move))
    return vecs

def run(lines):
    moves = parse(lines)
    current_h = (0,0)
    current_t = (0,0)
    t_spaces = [(0,0)]
    for i in moves:
        rel_vec = relVec(current_t, current_h)
        current_h = vecAdd(current_h, i)
        current_t = vecAdd(current_t, move(rel_vec, i))
        if not current_t in t_spaces:
            t_spaces.append(current_t)
    return len(t_spaces)

def multiMove(this_move, pos):
    new_pos = []
    lead_move = ()
    for i in range(len(pos)):
        if i == 0:
            new_pos.append(vecAdd(pos[i], this_move))
            lead_move = this_move
        else:
            rel_vec = relVec(pos[i], pos[i-1])
            lead_move = move(rel_vec, lead_move)
            new_pos.append(vecAdd(pos[i], lead_move))
    return new_pos

def run2(lines):
    moves = parse(lines)
    current_pos = [(0,0)] * 10
    spaces = [(0,0)]
    for i in moves:
        current_pos = multiMove(i, current_pos)
        if not current_pos[-1] in spaces:
            spaces.append(current_pos[-1])
    return len(spaces)

with open('./input.txt') as f:
    lines = f.readlines()

#print(run(lines))

print(run2(lines))