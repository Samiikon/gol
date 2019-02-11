"""All Game of Life rendering actions live here."""


def render_terminal(state, stats=False):
    """Draws given state to terminal.

    Args:
        state(list): State to render to terminal.
        stats(bool): Print additional data with the render.
    """

    width = len(state[0])
    height = len(state)

    # Print additional stats
    if stats:
        print("W: " + str(width) + "\tH: " + str(height))

    print('\n+' + (width * '-') + '+')

    for y in range(height):
        print('|', end='')
        for x in range(width):
            if state[y][x]:
                print('O', end='')
            else:
                print('.', end='')
        print('|')

    print('+' + (width * '-') + '+\n')
