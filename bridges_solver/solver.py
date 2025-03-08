from bridges_solver.grid import Grid, NumberTile, Direction

def start(grid):
    numbers = get_and_populate_numbers(grid.grid)

    numbers.sort(key=sort)

    make_connections(numbers, grid)

def sort(number):
    return number._num_pos_connections-number._numConnectionsLeft

def get_and_populate_numbers(grid):
    numbers = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if isinstance(grid[i][j], NumberTile):
                set_possible_connections(grid, grid[i][j])

                numbers.append(grid[i][j])

    return numbers

def set_possible_connections(grid, number_tile):
    """
        Populates the possible connection fields of a number tile in the grid.

        Args:
            grid (list[list[NumberTile]]): A 2D list representing the grid containing NumberTiles.
            number_tile (NumberTile): The number tile to populate its possible connections.

        Direction (Direction): Enum representing the direction of the connection.

        The function checks the grid in all four directions (left, right, up, down) from the position of the given
        number tile. It sets possible connections between the given number tile and any adjacent number tiles found
        in those directions.
    """

    def set_connection(new_x, new_y, new_direction):
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and isinstance(grid[new_x][new_y], NumberTile):
            num_cons = min(2, grid[new_x][new_y].number, number_tile.number)

            number_tile.set_possible_connection(new_direction, num_cons, grid[new_x][new_y])

            return True

        return False

    x, y = number_tile.x, number_tile.y

    directions = {
        "LEFT": (0, -1),
        "RIGHT": (0, 1),
        "UP": (-1, 0),
        "DOWN": (1, 0)
    }

    for direction, (dx, dy) in directions.items():
        nx, ny = x + dx, y + dy
        while 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if set_connection(nx, ny, Direction[direction]):
                break
            nx += dx
            ny += dy


def make_connections(numbers, grid):
    if len(numbers) == 0:
        return

    number = numbers[0]
    # if number._numConnectionsLeft < number._numPosConnections:
    #    return

    posCons = number.get_possible_connections()
    for conNumber in list(posCons.keys()):
        if len(posCons) == 0:
            break

        if posCons[conNumber].numPossible == 2:
            grid.connect_numbers(number, conNumber)

        grid.connect_numbers(number, conNumber)

    numbers.remove(number)

    numbers.sort(key=sort)

    return make_connections(numbers, grid)