from .tile import ConnectionTile

class Board:
    def __init__(self, rows: int, cols: int):
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

    def set_connection(self, connection_tile, is_horizontal):
        connection_tile.add_connection(self.grid, is_horizontal)

    def connect_numbers(self, num1, num2):
        if num1.is_complete() or num2.is_complete():
            return

        num1.add_connection(num2)
        num2.add_connection(num1)

        if num1.y == num2.y:
            handle_vertical_connection(self, num1, num2)

            return

        handle_horizontal_connection(self, num1, num2)


def handle_vertical_connection(board, num1, num2):
    start, end = sorted([num1.x, num2.x])

    for i in range(start + 1, end):
        board.set_connection(board.grid[i][num1.y], False)

    return board


def handle_horizontal_connection(board, num1, num2):
    start, end = sorted([num1.y, num2.y])

    for i in range(start + 1, end):
        board.set_connection(board.grid[num1.x][i], True)

    return board