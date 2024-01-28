# """
#     Pygame of life module. Contains the short engine
#     to simluate the grid of life.
# """

# import sys
# import time
# from collections import defaultdict
# from copy import deepcopy

# import pygame

# from example_grids import GOSPER_GLIDER
# from grid_defs import Grid, Neighbours


# def get_neighbours(grid: Grid, x: int, y: int) -> Neighbours:
#     """
#         Gets the neighbour states for a particular cell in
#         (x, y) on the grid.
#     """
#     offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
#     possible_neighbours = {(x + x_add, y + y_add) for x_add, y_add in offsets}
#     alive = {(pos[0], pos[1]) for pos in possible_neighbours if pos in grid.cells}
#     return Neighbours(alive, possible_neighbours - alive)


# def update_grid(grid: Grid) -> Grid:
#     """
#         Given a grid, this function returns the next iteration
#         of the game of life.
#     """
#     new_cells = deepcopy(grid.cells)
#     undead = defaultdict(int)

#     for x, y in grid.cells:
#         alive_neighbours, dead_neighbours = get_neighbours(grid, x, y)
#         if len(alive_neighbours) not in [2, 3]:
#             new_cells.remove((x, y))

#         for pos in dead_neighbours:
#             undead[pos] += 1

#     for pos, _ in filter(lambda elem: elem[1] == 3, undead.items()):
#         new_cells.add((pos[0], pos[1]))

#     return Grid(grid.dim, new_cells)


# def draw_grid(screen: pygame.Surface, grid: Grid) -> None:
#     """
#         This function draws the game of life on the given
#         pygame.Surface object.
#     """
#     cell_width = screen.get_width() / grid.dim.width
#     cell_height = screen.get_height() / grid.dim.height
#     border_size = 2

#     for x, y in grid.cells:
#         pygame.draw.rect(
#             screen,
#             (255, 0, 0),
#             (
#                 x * cell_width + border_size,
#                 y * cell_height + border_size,
#                 cell_width - border_size,
#                 cell_height - border_size,
#             ),
#         )


# def main():
#     """
#         Main entry point
#     """
#     grid = GOSPER_GLIDER

#     pygame.init()
#     screen = pygame.display.set_mode((600, 400))

#     while True:
#         if pygame.QUIT in [e.type for e in pygame.event.get()]:
#             sys.exit(0)

#         screen.fill((0, 0, 0))
#         draw_grid(screen, grid)
#         grid = update_grid(grid)
#         pygame.display.flip()
#         time.sleep(0.1)


# if __name__ == "__main__":
#     main()



import sys
import time
from collections import defaultdict
from copy import deepcopy

import pygame

from example_grids import GOSPER_GLIDER
from grid_defs import Grid, Neighbours


def get_neighbours(grid: Grid, x: int, y: int) -> Neighbours:
    offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    possible_neighbours = {(x + x_add, y + y_add) for x_add, y_add in offsets}
    alive = {(pos[0], pos[1]) for pos in possible_neighbours if pos in grid.cells}
    return Neighbours(alive, possible_neighbours - alive)
    


def update_grid(grid: Grid) -> Grid:
    new_cells = deepcopy(grid.cells)
    """
        Given a grid, this function returns the next iteration
        of the game of life.    
    """
    
    undead = defaultdict(int)

    for x, y in grid.cells:
        alive_neighbours, dead_neighbours = get_neighbours(grid, x, y)
        if len(alive_neighbours) not in [2, 3]:
            new_cells.remove((x, y))

        for pos in dead_neighbours:
            undead[pos] += 1

    for pos, _ in filter(lambda elem: elem[1] == 3, undead.items()):
        new_cells.add((pos[0], pos[1]))

    return Grid(grid.dim, new_cells)
    


def draw_grid(screen: pygame.Surface, grid: Grid, color: tuple) -> None:
    cell_width = screen.get_width() / grid.dim.width
    cell_height = screen.get_height() / grid.dim.height
    border_size = 2

    for x, y in grid.cells:
        pygame.draw.rect(
            screen,
            color,
            (
                x * cell_width + border_size,
                y * cell_height + border_size,
                cell_width - border_size,
                cell_height - border_size,
            ),
        )


def main():
    grid = GOSPER_GLIDER

    pygame.init()
    screen = pygame.display.set_mode((600, 400))

    color = (255, 0, 0)  # Initial color

    while True:
        if pygame.QUIT in [e.type for e in pygame.event.get()]:
            sys.exit(0)

        screen.fill((0, 0, 0))
        draw_grid(screen, grid, color)
        grid = update_grid(grid)
        pygame.display.flip()

        # Change color (you can modify this logic based on your requirements)
        color = (color[2], color[0], color[1])  # Simple color rotation
        time.sleep(0.1)


if __name__ == "__main__":
    main()
