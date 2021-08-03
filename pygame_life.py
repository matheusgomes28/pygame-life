import sys
import time
from collections import defaultdict
from copy import deepcopy

import pygame

from example_grids import gosper_glider
from grid_defs import Grid

adjacent_dirs = [(-1, -1), (0, -1), (1, -1), (-1, 0),
                 (1, 0), (-1, 1), (0, 1), (1, 1)]


def get_alive_neighbours(grid, x, y):
    positions = [(x + xAdd, y + yAdd) for xAdd, yAdd in adjacent_dirs]
    return {(pos[0], pos[1]) for pos in positions if pos in grid.cells}


def get_dead_neighbours(grid, x, y):
    positions = [(x + xAdd, y + yAdd) for xAdd, yAdd in adjacent_dirs]
    return {(pos[0], pos[1]) for pos in positions if pos not in grid.cells}


def update_grid(grid):
    new_cells = deepcopy(grid.cells)
    undead = defaultdict(int)

    for (x, y) in grid.cells:
        if len(get_alive_neighbours(grid, x, y)) not in [2, 3]:
            new_cells.remove((x, y))

        for pos in get_dead_neighbours(grid, x, y):
            undead[pos] += 1

    for pos, _ in filter(lambda elem: elem[1] == 3, undead.items()):
        new_cells.add((pos[0], pos[1]))

    return Grid(grid.dim, new_cells)


def draw_grid(screen, grid):
    cell_width = screen.get_width()/grid.dim.width
    cell_height = screen.get_height()/grid.dim.height

    for (x, y) in grid.cells:
        rect = pygame.Rect(x*cell_width+2, y*cell_height +
                           2, cell_width-2, cell_height-2)
        pygame.draw.rect(screen, (255, 0, 0), rect)


def main():

    grid = gosper_glider

    pygame.init()
    screen = pygame.display.set_mode((600, 400))

    while True:
        if pygame.QUIT in [e.type for e in pygame.event.get()]:
            sys.exit(0)

        screen.fill((0, 0, 0))
        draw_grid(screen, grid)
        grid = update_grid(grid)
        pygame.display.flip()
        time.sleep(0.1)


if __name__ == "__main__":
    main()
