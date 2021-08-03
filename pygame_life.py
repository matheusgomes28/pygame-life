import sys
import time

from collections import defaultdict
from copy import deepcopy
from example_grids import gosper_glider
import pygame


def get_alive_neighbours(grid, x, y):
    adjacent_dirs = [(-1, -1), (0, -1), (1, -1), (-1, 0),
                     (1, 0), (-1, 1), (0, 1), (1, 1)]
    positions = [(x + xAdd, y + yAdd) for xAdd, yAdd in adjacent_dirs]
    return {(pos[0], pos[1]) for pos in positions if pos in grid.cells}


def get_dead_neighbours(grid, x, y):
    adjacent_dirs = [(-1, -1), (0, -1), (1, -1), (-1, 0),
                     (1, 0), (-1, 1), (0, 1), (1, 1)]
    positions = [(x + xAdd, y + yAdd) for xAdd, yAdd in adjacent_dirs]
    return {(pos[0], pos[1]) for pos in positions if pos not in grid.cells}


def update_grid(grid):
    new_grid = deepcopy(grid)
    undead = defaultdict(int)

    for (x, y) in grid.cells:
        alive_neighbours = get_alive_neighbours(grid, x, y)
        if len(alive_neighbours) < 2 or len(alive_neighbours) > 3:
            new_grid.cells.remove((x, y))

        for pos in get_dead_neighbours(grid, x, y):
            undead[pos] += 1

    for pos, neighbours in undead.items():
        if neighbours == 3:
            new_grid.cells.add((pos[0], pos[1]))

    return new_grid


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

        time.sleep(0.2)


if __name__ == "__main__":
    main()
