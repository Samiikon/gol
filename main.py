"""Main python file for game of life."""

from src.state import (
    load_board_state,
    run_game,
)
from src.render import render_terminal

from pathlib import Path

project_root = Path.cwd()

LOADED_STATE = load_board_state(project_root, 'states/80x40multiple.txt')
run_game(LOADED_STATE, iterations=120, sleep_time=0.2)
