
from enum import Enum

class Direction(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"

class PosConnection:
    def __init__(self, direction, num_possible, number):
        self.number = number
        self.direction = direction
        self.num_possible = num_possible

    def __str__(self):
        return self.number + ":" + self.direction + ":" + self.num_possible

class NumberTile:
    def __init__(self, num: int, x: int, y: int):
        self.number = num
        self.x = x
        self.y = y
        self._pos_connections = {}
        self._num_connections_left = num
        self._num_connections = 0
        self._complete = False

    def __str__(self):
        return str(self.number)

    def display(self):
        return str(self.number)+ " "

    def set_possible_connection(self, direction, num_possible, number):
        self._pos_connections[number]= PosConnection(direction, num_possible, number)

    def remove_possible_connection(self, number):
        self._pos_connections.pop(number)

    def get_possible_connections(self):
        return self._pos_connections

    def get_num_possible_connections(self):
        num_pos_connections = 0

        for number, pos_connection in self._pos_connections.items():
            num_pos_connections += pos_connection.num_possible

        return num_pos_connections

    def reduce_possible_direction(self, direction):
        connection_to_remove = None

        for number, pos_con in self._pos_connections.items():
            if pos_con.direction == direction:
                connection_to_remove = pos_con

                break

        if connection_to_remove is not None:
            self.remove_possible_connection(connection_to_remove.number)

    def add_connection(self, number):
        if self._complete:
            return

        pos_con = self._pos_connections[number]

        pos_con.num_possible -= 1
        if pos_con.num_possible == 0:
            self.remove_possible_connection(number)

        self._num_connections_left -= 1
        self._num_connections += 1

        if self._num_connections_left == 0 or self._num_connections == self.number:
            self._pos_connections.clear()
            self._complete = True

class ConnectionTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._connections = 0
        self._direction = ""

    def display(self):
        if self._connections == 0:
            return "  "
        
        if self._connections == 1:
            if self._direction in (Direction.LEFT, Direction.RIGHT):
                return "--"
            
            return "| "

        if self._direction in (Direction.LEFT, Direction.RIGHT):
            return "=="
            
        return "||"
    
    def add_connection(self, grid, direction):
        if self._connections == 2:
            return
            
        self._connections += 1
        self._direction = direction

        if self._direction in (Direction.UP, Direction.DOWN) : # vertical
            for j in range(self.y - 1, -1, -1):
                if isinstance(grid[self.x][j], NumberTile):
                    grid[self.x][j].reduce_possible_direction(Direction.RIGHT)
                    break  # Stop checking further left after first number

            # Check right
            for j in range(self.y + 1, len(grid[0])):
                if isinstance(grid[self.x][j], NumberTile):
                    grid[self.x][j].reduce_possible_direction(Direction.LEFT)
                    break  # Stop checking further right after

            return
        
        # Check UP
        for i in range(self.x - 1, -1, -1):  # Move upwards
            if isinstance(grid[i][self.y], NumberTile):
                grid[i][self.y].reduce_possible_direction(Direction.DOWN)  # Remove downward connection
                break  # Stop after the first number

        # Check DOWN
        for i in range(self.x + 1, len(grid)):  # Move downwards
            if isinstance(grid[i][self.y], NumberTile):
                grid[i][self.y].reduce_possible_direction(Direction.UP)  # Remove upward connection
                break  # Stop after the first number

        


class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.grid = [[ConnectionTile(row, col) for col in range(cols)] for row in range(rows)]

    def __repr__(self):
        """
        Returns a string representation of the grid, primarily for printing.
        """
        return '\n'.join([' '.join([cell.display() for cell in row]) for row in self.grid])
    
    def set_number(self, number):
        if 0 <= number.x < self.rows and 0 <= number.y < self.cols:
            self.grid[number.x][number.y] = number
        else:
            raise IndexError("Cell index out of bounds")

    def set_connection(self, row, col, direction):
        self.grid[row][col].add_connection(self.grid, direction)

    def connect_numbers(self, num1, num2):
        if num1._complete or num2._complete:
            return

        num1.add_connection(num2)
        num2.add_connection(num1)

        if num1.y == num2.y:
            self = handle_vertical_connection(self, num1, num2)

            return
        
        self = handle_horizontal_connection(self, num1, num2)

def handle_vertical_connection(grid, num1, num2):
    start = min(num1.x, num2.x)
    end = max(num1.x, num2.x)

    direction = Direction.UP
    if start < end:
        direction = Direction.DOWN

    for i in range(start+1, end):
        grid.set_connection(i, num1.y, direction)

    return grid    

def handle_horizontal_connection(grid, num1, num2):
    start = min(num1.y, num2.y)
    end = max(num1.y, num2.y)

    direction = Direction.RIGHT
    if start < end:
        direction = Direction.LEFT

    for i in range(start+1, end):
        grid.set_connection(num1.x, i, direction)

    return grid    


# TODO bottom middle 4.