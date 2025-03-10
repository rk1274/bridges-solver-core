from operator import truediv
import copy

from nltk.sem.chat80 import continent

from bridges_solver.board import Board, NumberTile, Direction

def start(grid):
    numbers = get_and_populate_numbers(grid.grid)

    numbers.sort(key=sort)

    return make_connections(numbers, grid)

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

            if number_tile.number == 2 and grid[new_x][new_y].number == 2:
                num_cons = 1
            elif number_tile.number == 1 and grid[new_x][new_y].number == 1:
                return

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


def sort(number):
    return number.get_num_possible_connections()-number._num_connections_left

def make_connections(numbers, grid):
    i = 0
    while i < len(numbers):
        number = numbers[i]
        connections_before = number._num_connections_left  # Store the number of connections before making any move

        # If no possible moves, handle and remove the number
        if number.get_num_possible_connections() - number._num_connections_left == 0:
            if number._num_connections_left == 0:
                number.set_complete()
            else:
                handle_when_1(grid, number)

            numbers.pop(i)  # Remove completed number

            numbers.sort(key=sort)  # Re-sort after removal
            i = 0  # Restart to ensure best move is picked

            continue

        # If only one connection is left to make
        if number.get_num_possible_connections() - number._num_connections_left == 1 and number._num_connections_left != 1:
            handle_when_2(grid, number)

            if number._num_connections_left == 0:
                numbers.pop(i)  # Remove fully connected number

            # Only restart if a new connection was made
            if number._num_connections_left < connections_before:
                numbers.sort(key=sort)
                i = 0
            else:
                i += 1

            continue

        # .. new thing!

        pos_cons = number.get_possible_connections()
        for number_to_connect in list(pos_cons.keys()):
            if len(pos_cons) == 0:
                break

            index_number = numbers.index(number)
            index_to_connect = numbers.index(number_to_connect)

            copied_numbers = copy.deepcopy(numbers)
            copied_grid = copy.deepcopy(grid)

            copied_num = copied_numbers[index_number]
            copied_to_connect = copied_numbers[index_to_connect]

            copied_grid.connect_numbers(copied_num, copied_to_connect)

            complete, copied_grid = make_connections(copied_numbers, copied_grid)
            if complete:
                return True, copied_grid

        i += 1  # Move to the next number if no action was taken

    if len(numbers) == 0:
        return True, grid

    return False, grid


def handle_when_1(grid, number):
    pos_cons = number.get_possible_connections()

    for number_to_connect in list(pos_cons.keys()):
        if len(pos_cons) == 0:
            break

        if pos_cons[number_to_connect].num_possible == 2:
            grid.connect_numbers(number, number_to_connect)

        grid.connect_numbers(number, number_to_connect)

def handle_when_2(grid, number):
    pos_cons = number.get_possible_connections()
    for number_to_connect in list(pos_cons.keys()):
        if len(pos_cons) == 0:
            break

        if pos_cons[number_to_connect].num_possible == 2:
            grid.connect_numbers(number, number_to_connect)