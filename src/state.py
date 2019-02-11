"""Creation and handling of gamestates in Game of Life project."""

import random
import time

from pathlib import Path

from .render import render_terminal

def dead_state(width, height):
    """Create new state with all cell dead.

    Returns list of lists containing only 0 values.

    Args:
        width(int): length of the x-axis
        height(int): length of the y-axis
    """

    full_state = []

    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(0)
        full_state.append(row)

    return full_state


def random_state(width, height, alive_threshold=0.8):
    """Create new state with randomized alive cells.

    Returns list of lists containing randomized 1 and 0 values.

    Args:
        width(int): Length of the x-axis
        height(int): Length of the y-axis
        alive_threshold(float): Value for amount of alive cells, values closer
            to 1.0 give less alive cells and values closer to 0.0 give more
            alive cells.
    """
    full_state = []

    for _ in range(height):
        row = []
        for _ in range(width):
            next_rand = random.random()
            if next_rand >= alive_threshold:
                row.append(1)
            else:
                row.append(0)
        full_state.append(row)

    return full_state


def load_board_state(project_root, filepath):
    """Open saved state from textfile in given location.

    Args:
        project_root(pathlib.Path): Path to project root.
        filepath(pathlib.Path): Path to textfile, relative to project root.

    """
    state_file = open(project_root / filepath, 'r')

    board_state = []
    for line in state_file:
        # List of integers for each line, strip whitespaces away.
        row = [int(x) for x in line.strip()]
        board_state.append(row)

    state_file.close()

    return board_state


def next_board_state(current_state):
    """Calculates and returns boards next state."""

    width = len(current_state[0])
    height = len(current_state)
    next_state = dead_state(width, height)

    for y in range(height):
        for x in range(width):

            # If x equals to width, some neighbors are on x=0 row. No need
            # to check the other side as Python can handle negative elements.
            if x == width - 1:
                xp = 0
            else:
                xp = x+1

            # If y equals to height, some neighbors are on y=0 row.
            if y == height - 1:
                yp = 0
            else:
                yp = y+1

            # As every alive-cell is integer 1 and dead-cell is 0, counting
            # neighbors is a simple sum.
            alive_count = current_state[y-1][x-1] + current_state[y-1][x] + \
                          current_state[y-1][xp] + current_state[y][x-1] + \
                          current_state[y][xp] + current_state[yp][x-1] + \
                          current_state[yp][x] + current_state[yp][xp]

            if current_state[y][x] and alive_count >= 2 and alive_count <= 3:
                next_state[y][x] = 1
            elif not current_state[y][x] and alive_count == 3:
                next_state[y][x] = 1

    return next_state


def run_game(state, iterations=10, sleep_time=1.0):
    """Run game for given state.

    Args:
        state(list): State to be used.
        iterations(int): How many iterations game goes through.
        sleep_time(float): Sleep time between iterations.
    """

    for _ in range(iterations):
        render_terminal(state, True)
        state = next_board_state(state)
        time.sleep(sleep_time)
