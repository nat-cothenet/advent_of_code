import pandas as pd
import numpy as np


def count_trees(tmap, slope_x, slope_y):
    width = len(tmap.iloc[0, 0])
    count_trees = 0
    x = 0
    y = 0
    while y != (len(tmap) - 1):
        x += slope_x
        if x >= width:
            x -= width
        y += slope_y
        if tmap.iloc[y, 0][x] == "#":
            count_trees += 1

    return count_trees


tmap = pd.read_csv("input_day3.csv", header=None)
slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

num_trees_list = []
for slope in slopes:
    num_trees = count_trees(tmap, slope[0], slope[1])
    print(f"Slope:\t{slope}\tTrees:\t{num_trees}")
    num_trees_list.append(num_trees)

product = np.prod(num_trees_list)
print(f"Product:\t{product}")
