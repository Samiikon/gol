import pytest

from src.state import dead_state


@pytest.mark.parametrize('test_input, expected',[
    (0,0),
    (1,1),
    (2,2),
    (100,100),
])
def test_state_width(test_input, expected):
    test_state = dead_state(test_input, 1)
    assert len(test_state[0]) == expected


@pytest.mark.parametrize('test_input, expected',[
    (0,0),
    (1,1),
    (2,2),
    (100,100),
])
def test_state_height(test_input, expected):
    test_state = dead_state(1,test_input)
    assert len(test_state) == expected


def test_state_content():
    expected_state = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    test_state = dead_state(3,4)
    assert test_state == expected_state
