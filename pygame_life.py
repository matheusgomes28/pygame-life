import pygame
import sys
import time

from collections import namedtuple
from copy import deepcopy

Point = namedtuple("Point", ["x", "y"])
Dim = namedtuple("Dimension", ["width", "height"])
Grid = namedtuple("Grid", ["dim", "cells"])

def make_grid(width, height):
    return Grid(Dim(width, height), set())

def init_graphics(settings):

    pygame.init()
    screen = pygame.display.set_mode((settings["window_width"], settings["window_height"]))
    return screen

def draw_grid(screen, grid):

    cell_width = screen.get_width()/grid.dim.width
    cell_height = screen.get_height()/grid.dim.height

    for (x, y) in grid.cells:
        rect = pygame.Rect(x*cell_width+2, y*cell_height+2, cell_width-2, cell_height-2)
        pygame.draw.rect(screen, (255, 0, 0), rect)

def in_range(grid, x, y):
    return x >= 0 and x < grid.dim.x and y >= 0 and y < grid.dim.y

def get_neighbours(grid, x, y):
    width = grid.dim.width
    height = grid.dim.height

    dirs = [(-1, -1), (0, -1), (1, -1), (-1,  0), (1,  0), (-1, 1), (0, 1), (1, 1)]
    positions = [(x + xAdd, y + yAdd) for xAdd, yAdd in dirs]
    return [(pos[0], pos[1]) for pos in positions if pos in grid.cells]

def check_dead(neighbours):
    num_neighbours = len(neighbours)
    return num_neighbours < 2 or num_neighbours > 3

def check_alive(neighbours):
    num_neighbours = len(neighbours)
    return num_neighbours == 3

def set_cell(grid, x, y):
    grid.cells.add((x, y))

def unset_cell(grid, x, y):
    grid.cells.remove((x, y))

def update_grid(grid):
    new_grid = deepcopy(grid)

    undead = {}

    # Check if alive cells need to die
    for (x, y) in grid.cells:
        neighbours = get_neighbours(grid, x, y)
        if len(neighbours) < 2 or len(neighbours) > 3:
            unset_cell(new_grid, x, y)

        for pos in neighbours:
            if pos in undead:
                undead[pos] += 1
            else:
                undead[pos] = 1
        print("!!!", undead)

    for k, v in undead.items():
        if v == 3:
            set_cell(new_grid, k[0], k[1])


    return new_grid


if __name__ == "__main__":

    settings = {
        "window_width": 600,
        "window_height": 400,
    }

    colours = {
        "black": (0, 0, 0)
    }

    grid = make_grid(10, 10)
    set_cell(grid, 3, 3)
    set_cell(grid, 4, 3)
    set_cell(grid, 5, 3)

    screen = init_graphics(settings)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        screen.fill(colours["black"])

        draw_grid(screen, grid)
        grid = update_grid(grid)
        pygame.display.flip()

        time.sleep(0.5)

    print("bye bye!")
