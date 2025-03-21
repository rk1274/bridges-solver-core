import copy

from bridges_solver.board import Board, NumberTile, Direction

process = [""]

lengthOfOrig  = 0

# badConnections = []

def start(grid):
    global lengthOfOrig
    numbers = get_and_populate_numbers(grid.grid)

    numbers.sort(key=sort)

    lengthOfOrig = len(numbers)

    return make_connections(numbers, grid), process

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
                return True

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

# This sort orders the list to put the 'easiest' numbers to deal with first.
def sort(number):
    return number.get_num_possible_connections() - number.num_connections_left, -number.num_connections_left

def make_connections(numbers, grid):
    i = 0
    while i < len(numbers):
        number = numbers[i]
        connections_before = number.num_connections_left

        # for num in numbers:
        if number.get_num_possible_connections() - number.num_connections_left < 0:
            return False, grid

        if number.get_num_possible_connections() - number.num_connections_left == 0:
            if number.num_connections_left == 0:
                number.set_complete()
            else:
                handle_when_1(grid, number)

            numbers.pop(i)

            numbers.sort(key=sort)
            i = 0

            continue

        if number.get_num_possible_connections() - number.num_connections_left == 1 and number.num_connections_left != 1:
            handle_when_2(grid, number)

            if number.num_connections_left == 0:
                numbers.pop(i)

            if number.num_connections_left < connections_before:
                numbers.sort(key=sort)
                i = 0
            else:
                i += 1

            continue

        complete, final_grid = handle_when_3(grid, number, numbers)
        if complete:
            return True, final_grid

        i += 1

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
            process.append(str(grid))

        grid.connect_numbers(number, number_to_connect)
        process.append(str(grid))

def handle_when_2(grid, number):
    pos_cons = number.get_possible_connections()
    for number_to_connect in list(pos_cons.keys()):
        if len(pos_cons) == 0:
            break

        if pos_cons[number_to_connect].num_possible == 2:
            grid.connect_numbers(number, number_to_connect)
            process.append(str(grid))


def handle_when_3(grid, number, numbers):
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

    return False, grid

# unused
def search(number):
    """Checks if the number is isolated (forms an island)."""
    visited = set()
    stack = [number]  # Start with the given number

    while stack:
        num = stack.pop()

        if num in visited:
            continue  # Skip already checked numbers

        visited.add(num)

        for connected in num._made_connections:
            if not connected.is_complete():
                return False

            if connected not in visited:
                stack.append(connected)

    if len(visited) == lengthOfOrig:
        return False

    # If all connected nodes form an isolated component, return True (it's an island)
    return True