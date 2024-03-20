import numpy as np
import math

DIM = 512

def read_points(filename):
    points = []
    with open(filename, 'r') as file:
        for line in file:
            x, y, z, p = map(float, line.split())
            point = (x, y, z, int(p))
            points.append(point)
    return points

def read_end_points(filename):
    with open(filename, 'r') as file:
        start_line = file.readline()
        end_line = file.readline()

        start = tuple(map(float, start_line.split()))
        finish = tuple(map(float, end_line.split()))

    return start, finish

def get_end_points(start, finish, antmap):
    start_p = next((point for point in antmap if point[:2] == start), None)
    finish_p = next((point for point in antmap if point[:2] == finish), None)

    return start_p, finish_p

def heuristic(point1, point2):
    return np.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[2]) ** 2)

def get_neighbors(point, points_set):
    neighbors = []
    x, y = point[:2]
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            neighbor = (x + dx, y + dy)
            if neighbor != point[:2] and neighbor in points_set:
                neighbors.append(points_set[neighbor])
    return neighbors

def choose_probability():
    pass

def ant_solution_build(points_set, start_p, finish_p, alpha, beta):
    energy = 0

    current_point = start_p
    while current_point != finish_p:
        neighbor_p = []
        for neighbor in get_neighbors(current_point, points_set):
            neighbor_p.append(choose_probability(neighbor, alpha, beta)) #TODO: finish argument list
    
    return energy

def daemon_step():
    pass

def feromon_update():
    pass

def aco_algorithm(antmap, start, finish, ant_nr):
    start_p, finish_p = get_end_points(start, finish, antmap)
    points_set = {point[:2]: point for point in antmap}
    alpha = 1.0
    beta = 1.0
    
    max_left_energy = 0
    i = 0
    while i < ant_nr:
        current_energy = ant_solution_build(points_set, start_p, finish_p, alpha, beta)
        daemon_step()
        feromon_update()
        if current_energy > max_left_energy:
            max_left_energy = current_energy
        i += 1

    return max_left_energy


def main():
    antmap = read_points('aco_points_512x512.txt')
    start, finish = read_end_points('aco_start_end_512x512.txt')
    aco_algorithm(antmap, start, finish, 100)

if __name__ == '__main__':
    main()
