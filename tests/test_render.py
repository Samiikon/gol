from io import StringIO
from unittest.mock import patch

from src.render import render_terminal


def test_render_without_stats():
    test_state = [[1,0,0],[0,1,0],[0,0,1],[1,1,1]]
    expected = """+---+
|O..|
|.O.|
|..O|
|OOO|
+---+"""

    with patch('sys.stdout', new=StringIO()) as fake_output:
        render_terminal(test_state, stats=False)
        output = fake_output.getvalue().strip()

        assert output == expected


def test_render_with_stats():
    test_state = [[1,0,0],[0,1,0],[0,0,1],[1,1,1]]
    expected = """W: 3	H: 4

+---+
|O..|
|.O.|
|..O|
|OOO|
+---+"""

    with patch('sys.stdout', new=StringIO()) as fake_output:
        render_terminal(test_state, stats=True)
        output = fake_output.getvalue().strip()

        assert output == expected
