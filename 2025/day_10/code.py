from functools import lru_cache
import numpy as np
import scipy.optimize as spo
import heapq
from multiprocessing import Process, Queue

def parse(lines):
    machines = []
    for line in lines:
        line_frags = line.strip().split()
        lights = []
        for light in line_frags[0][1:-1]:
            if light == '#':
                lights.append(True)
            elif light == '.':
                lights.append(False)
        joltage = []
        for i in line_frags[-1][1:-1].split(','):
            joltage.append(int(i))
        wires = []
        for wiring in line_frags[1:-1]:
            wires.append(tuple([int(i) for i in wiring[1:-1].split(',')]))
        machines.append((tuple(lights), tuple(wires), tuple(joltage)))
    return machines

@lru_cache(maxsize=None)
def test_button(lights, desired, buttons, button_idx):
    if lights == desired:
        return 0
    button = buttons[button_idx]
    new_lights = list(lights)
    for i in button:
        new_lights[i] = not new_lights[i]
    new_lights = tuple(new_lights)
    if new_lights == desired:
        return 1
    new_buttons = buttons[:button_idx] + buttons[button_idx + 1:]
    min_val = len(buttons)
    for i in range(len(new_buttons)):
        val = test_button(new_lights, desired, new_buttons, i)
        if val < min_val:
            min_val = val
    return 1 + min_val

def run(inp):
    data = parse(inp)
    button_counts = []
    for lights, wires, joltages in data:
        min_val = len(wires)
        for i in range(len(wires)):
            val = test_button(tuple([False] * len(lights)), lights, wires, i)
            if val < min_val:
                min_val = val
        button_counts.append(min_val)
    print(f"{button_counts}\n{sum(button_counts)}")


def run2(inp):
    data = parse(inp)
    button_counts = []
    for lights, wires, joltages in data:
        b = np.array(joltages)
        mat_coeff = []
        for i in range(len(wires)):
            row = [0] * len(joltages)
            for j in wires[i]:
                row[j] = 1
            mat_coeff.append(row)
        A = np.linalg.matrix_transpose(np.array(mat_coeff))
        constraints = spo.LinearConstraint(A, b, b)
        c = np.array([1 for _ in range(len(wires))])
        integrality = np.array([1 for _ in range(len(wires))])
        result = spo.milp(c=c, constraints=constraints, integrality=integrality)
        buttons = [int(round(i)) for i in result.x]
        button_counts.append(sum(buttons))
    print(f"{button_counts}\n{sum(button_counts)}")


with open('./input.txt') as f:
    lines = f.readlines()

run2(lines)

##
# I'd usually delete failed (/ probably works but not used) attempts, but I'm proud of this
##
def heuristic(point, destination, max_step_size):
    diff = list(destination)
    for i in range(len(diff)):
        diff[i] -= point[i]
    for i in diff:
        if i < 0:
            return 100000
    return sum(diff) // max_step_size

def a_star(start, end, moves, queue, id):
    frontier = []
    explored = []
    max_step = max([len(i) for i in moves])
    heapq.heappush(frontier, (heuristic(start, end, max_step), start, tuple()))
    while True:
        weight, coord, path = heapq.heappop(frontier)
        if coord == end:
            queue.put((id, path))
            return
        elif coord in explored:
            continue
        explored.append(coord)
        for i in range(len(moves)):
            move = moves[i]
            new_pos = list(coord)
            for j in move:
                new_pos[j] += 1
            new_pos = tuple(new_pos)
            if new_pos in explored:
                continue
            new_path = path + (i,)
            heapq.heappush(frontier, (len(new_path) + heuristic(new_pos, end, max_step), new_pos, new_path))

def run2a(inp):
    data = parse(inp)
    button_counts = []
    q = Queue()
    p = []
    for lights, wires, joltages in data:
        p.append(Process(target=a_star, args=(tuple([0] * len(joltages)), joltages, wires, q, len(p))))
        p[-1].start()
    for i in range(len(p)):
        id, path = q.get()
        print(f"{id}: {len(path)} | {path}")
        button_counts.append(len(path))
        p[id].join()
    print(f"{button_counts}\n{sum(button_counts)}")
