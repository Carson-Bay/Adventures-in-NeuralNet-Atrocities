from PIL import Image
import random
import sys
import numpy as np
import time
import pickle
import matplotlib.pyplot as plt

#TODO Variable renaming
#TODO Python recursion limits

MAX_DEPTH = 20000

def maze_template():
    size = int(input("Size of Mazes: "))
    if size % 2 == 0:
        size += 1
    
    mazeTemplate = np.zeros((size, size), dtype=np.uint8)
    openTemplate = np.zeros((size, size), dtype=np.uint8)

    for i in range(1, size - 1, 2):
        for j in range(1, size - 1, 2):
            mazeTemplate[i, j] = 1
            openTemplate[i, j] = 1

    return mazeTemplate, openTemplate, size


def get_neighbours(coord, openTemplate, size):
    '''
    Returns: list of coordinates of neighboring unvisited nodes
    '''
    n = []
    x, y = coord

    for i in range(-2, 3, 4):
        if 0 < (x + i) < size and openTemplate[x+i, y]:
            n.append((x + i, y))

    for j in range(-2, 3, 4):

        if 0 < (y + j) < size and openTemplate[x, y+j]:
            n.append((x, y + j))
    return n

def evaluate_node(node, maze, open_map, size, depth):

    current_x, current_y = node
    open_map[current_x, current_y] = 0

    depth += 1

    if depth >= MAX_DEPTH:
        return maze, open_map

    while(len(get_neighbours(node, open_map, size)) > 0):
        next = random.choice(get_neighbours(node, open_map, size))
        next_x, next_y = next
        
        # Remove the wall
        wall_X = int((current_x + next_x) / 2)
        wall_Y = int((current_y + next_y) / 2)
        maze[wall_X, wall_Y] = 1

        maze, open_map = evaluate_node(next, maze, open_map, size, depth)
    
    return maze, open_map

def gen_maze(size, mazeT, open_mapT):
    initial_x = random.randrange(1, size, 2)
    initial_y = random.randrange(1, size, 2)

    maze, open_map = evaluate_node((initial_x, initial_y), mazeT, open_mapT, size, 0)

    # Create entrance and exit
    start = random.randrange(1, size - 1, 2)
    end = random.randrange(1, size - 1, 2)

    maze[0, start] = 1
    maze[size - 1, end] = 1

    return maze.flatten()

def main():
    sys.setrecursionlimit(40000)
    mazeTemplate, openTemplate, size = maze_template()

    numberOfMazes = int(input("Number of Mazes to Gen: "))

    startTime = time.perf_counter()

    mazes = np.zeros((numberOfMazes, size ** 2))

    for i in range(numberOfMazes):
        mazeT = np.copy(mazeTemplate)
        openT = np.copy(openTemplate)

        mazes[i] = gen_maze(size, mazeT, openT)
    

    runTime = time.perf_counter() - startTime
    print(runTime)


    if numberOfMazes == 1:
        reshaped_maze = mazes[0].reshape(size, size) * 255

        maze_img = Image.fromarray(reshaped_maze)

        maze_img.show()

    else:
        with open("NewMazeDataset11.pickle", "wb") as fout:
            pickle.dump(mazes, fout)


if __name__ == "__main__":
    main()
