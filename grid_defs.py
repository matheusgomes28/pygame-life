"""
    Grid definitions for the game of life engine.
"""
from collections import namedtuple

Dim = namedtuple("Dimension", ["width", "height"])
Grid = namedtuple("Grid", ["dim", "cells"])
Neighbours = namedtuple("Neighbours", ["alive", "dead"])
