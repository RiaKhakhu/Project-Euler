# author: Khakhu Ria
# version: 14/12/2024

from queue import Queue


# problem statement: given a 20 by 20 grid, in how many ways can you travel from the top-left corner
# to the bottom-left corner, if you can only move horizontally right or vertically down?

def find_paths(grid):
    """
    finds the total paths from the top-left corner to any point on the grid by moving
    horizontally right or vertically down in the given grid ( this is a digraph). The logic behind this is that
    if X1,X2,...,Xn is the in-neighbourhood of a point X, then p(X) =  p(X1)+p(X2)+...+p(Xn), where p(y) is
    the number of paths from the top-left corner to a point y.
    """
    grid_dimensions = dimensions(grid)
    points_queue = Queue()
    start = (0, 0)
    discovered = {}
    points_queue.put(start)
    grid[0][0] = 1

    while not points_queue.empty():
        position = points_queue.get()
        position_neighbours = out_neighbourhood(position, grid_dimensions[0], grid_dimensions[1])
        for neighbour in position_neighbours:
            if neighbour not in discovered:  # wouldn't want to add twice
                points_queue.put(neighbour)
                discovered[neighbour] = "yay"
            grid[neighbour[0]][neighbour[1]] += grid[position[0]][position[1]]

    return grid


def out_neighbourhood(point, height, width):
    """
    find the out-neighbourhood of the given point
    """
    neighbour_1 = (point[0], point[1] + 1)
    neighbour_2 = (point[0] + 1, point[1])
    neighbours = []
    if neighbour_1[0] < height and neighbour_1[1] < width:
        neighbours.append(neighbour_1)

    if neighbour_2[0] < height and neighbour_2[1] < width:
        neighbours.append(neighbour_2)

    return neighbours


def dimensions(grid):
    """
    find the dimensions of the given grid
    """
    width = len(grid[0])
    height = 0

    for row in grid:
        height += 1

    return height, width


if __name__ == "__main__":
    grid = [[0 for i in range(21)] for j in range(21)]
    path_grid = find_paths(grid)
    print(path_grid[20][20])
