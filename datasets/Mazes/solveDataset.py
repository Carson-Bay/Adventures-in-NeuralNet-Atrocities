from PIL import Image
import random
import sys
import numpy as np
import time
import pickle
import matplotlib.pyplot as plt


def get_neighbours(coord, openTemplate, size):
    '''
    Returns: list of coordinates of neighboring unvisited nodes
    '''
    n = []
    x, y = coord

    for i in range(-1, 2, 2):
        if 0 < (x + i) < size and openTemplate[x+i, y]:
            n.append((x + i, y))

    for j in range(-1, 2, 2):

        if 0 < (y + j) < size and openTemplate[x, y+j]:
            n.append((x, y + j))
    return n

def evaluate_node(node, maze, pathCheck, size, pathList, target):

    current_x, current_y = node
    pathCheck[current_x, current_y] = 0
    possiblePathList = pathList.copy()
    possiblePathList.append(node)
    
    while(len(get_neighbours(node, pathCheck, size)) > 0):
        next = random.choice(get_neighbours(node, pathCheck, size))
        next_x, next_y = next
        

        maze, pathCheck, possiblePathList = evaluate_node(next, maze, pathCheck, size, possiblePathList, target)
        if possiblePathList[-1] == target:
            pathList = possiblePathList
            return maze, pathCheck, pathList
    
    if node == target:
        pathList = possiblePathList
    
    return maze, pathCheck, pathList

# returns first white pixel in image
def find_start(mazeArray):
    for index, line in enumerate(mazeArray):
        for j, pixel in enumerate(line):
            if bool(pixel):
                return (index, j)

# TODO FIX THIS SHITTY FUNCTION JUST GO BACKWARDS DUMMY
def find_target(mazeArray):
    for index, line in enumerate(mazeArray):
        for j, pixel in enumerate(line):
            if bool(pixel):
                xCord = index
                yCord = j
    return (xCord, yCord)

def main():
    sys.setrecursionlimit(100000)

    with open("NewMazeDataset11.pickle", "rb") as fin:
        mazes = pickle.load(fin)

    solves = np.zeros((0, 121))

    startTime = time.perf_counter()

    # TODO write to automatically find length
    for i in range(50000):
        mazeArray = mazes[i].reshape(11,11)
        pathCheck = np.copy(mazeArray)
    
        pathList = []

        start = find_start(mazeArray)
        end = find_target(mazeArray)

        maze, pathCheck, pathList = evaluate_node(start, mazeArray, pathCheck, mazeArray.shape[0], pathList, end)

        solve = np.zeros(mazeArray.shape)

        for i in pathList:
            solve[i] = 1

        solve_reshaped = solve.reshape(1, 121)
    
        solves = np.append(solves, solve_reshaped, axis=0)


    with open("NewDataset11.pickle", "wb") as fout:
        pickle.dump(mazes, fout)
        pickle.dump(solves, fout)
    

    runTime = time.perf_counter() - startTime
    print(runTime)


if __name__ == "__main__":
    main()
