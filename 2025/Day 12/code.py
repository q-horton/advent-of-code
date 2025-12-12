from functools import lru_cache
import math

def parse(lines):
    presents = []
    trees = []
    shapes_mode = True
    next_shape = []
    for line in lines:
        line = line.strip()
        if shapes_mode:
            if len(line) == 0:
                presents.append(tuple(next_shape))
            elif line[-1] == ':':
                next_shape = []
            elif '0' <= line[0] <= '9':
                shapes_mode = False
            else:
                next_row = 0
                for i in range(len(line)):
                    if line[i] == '#':
                        next_row |= (1 << i)
                next_shape.append(next_row)
        if not shapes_mode:
            breakdown = line.split(':')
            dims = tuple([int(i) for i in breakdown[0].split('x')])
            quants = tuple([int(i) for i in breakdown[1].split()])
            trees.append((dims, quants))
    return (tuple(presents), trees)

@lru_cache(maxsize=None)
def can_fit(space, space_dims, presents, shapes):
    space_x, space_y = space_dims
    first_needed = 0
    for i in range(len(presents)):
        if presents[i] > 0:
            first_needed = i
            break
    is_last_shape = (sum(presents) - 1 == 0)
    next_presents = list(presents)
    if not is_last_shape:
        next_presents[first_needed] -= 1
        next_presents = tuple(next_presents)
    pres_array = shapes[first_needed]
    pres_x = math.floor(math.log(max(pres_array), 2)) + 1
    pres_y = len(pres_array)
    pres = 0
    for i in range(pres_y):
        pres |= pres_array[i] << (i * space_x)
    past_pres = [pres]
    for rotation in range(8):
        for dy in range(space_y - pres_y + 1):
            for dx in range(space_x - pres_x + 1):
                shifted_pres = pres << (dx + dy * space_x)
                if shifted_pres & space > 0:
                    continue
                elif shifted_pres & ~(2 ** (space_x * space_y) - 1) > 0:
                    continue
                if is_last_shape:
                    return True
                else:
                    next_space = space | shifted_pres
                    fitting = can_fit(next_space, space_dims, next_presents, shapes)
                    if fitting:
                        return True
        rot_pres = 0
        for y in range(pres_y):
            for x in range(pres_x):
                cur_val = (pres >> (y * space_x + x)) & 1
                rot_pres |= cur_val << (x * space_x + (pres_y - 1) - y)
        # Despite highlighting 'rotated and flipped', it appears allowing
        # flipping breaks it
        # -----
        # if rotation % 4 == 3:
        #     vert_flip_pres = 0
        #     for y in range(pres_y):
        #         row = (rot_pres >> (y * space_x)) & (2 ** pres_x - 1)
        #         vert_flip_pres |= row << (((space_y - 1) - y) * space_x)
        #     rot_pres = vert_flip_pres
        # if rotation % 8 == 7:
        #     horiz_flip_pres = 0
        #     for y in range(pres_y):
        #         for x in range(pres_x):
        #             cur_val = (rot_pres >> (y * space_x + x)) & 1
        #             horiz_flip_pres |= cur_val << (y * space_x + (pres_x - 1) - x)
        #     rot_pres = horiz_flip_pres
        if rot_pres in past_pres:
            break
        past_pres.append(rot_pres)
        pres = rot_pres
    return False

def run(inp):
    presents, trees = parse(inp)
    present_bits = []
    for present in presents:
        pres_x = math.floor(math.log(max(present), 2)) + 1
        pres_y = len(present)
        count = 0
        for x in range(pres_x):
            for y in range(pres_y):
                if (present[y] >> x) & 1 == 1:
                    count += 1
        present_bits.append(count)
    fits = []
    for i in range(len(trees)):
        dims, quants = trees[i]
        bit_count = 0
        for j in range(len(quants)):
            bit_count += quants[j] * present_bits[j]
        if bit_count > dims[0] * dims[1]:
            fits.append(False)
            continue
        fits.append(can_fit(0, dims, quants, presents))
    print(sum([1 if i else 0 for i in fits]))

with open('./input.txt') as f:
    lines = f.readlines()

run(lines)
