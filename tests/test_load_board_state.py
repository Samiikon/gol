import pytest

from pathlib import Path

from src.state import load_board_state


# Run pytest from project root to get right path!
project_root = Path.cwd()


@pytest.mark.parametrize('filename, expected',[
    ('tests/files/3x3_zeroes.txt',[[0,0,0],[0,0,0],[0,0,0]]),
    ('tests/files/3x4_zeroes.txt',[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]),
    ('tests/files/4x3_zeroes.txt',[[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
    ('tests/files/4x3_mixed.txt',[[1,0,0,1],[0,1,0,0],[0,1,0,1]]),
    ('tests/files/3x3_ones.txt',[[1,1,1],[1,1,1],[1,1,1]]),
])
def test_against_files(filename, expected):
    filepath = Path(filename)

    test_state = load_board_state(project_root, filepath)

    assert test_state == expected
