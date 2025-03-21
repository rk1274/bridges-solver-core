import unittest
from solver.solver import set_possible_connections,make_connections, start, sort, get_and_populate_numbers, handle_mandatory_connections, handle_reducible_connections
from board.board import Board
from board.tile import NumberTile
import json

def load_boards():
    with open("tests/boards.json", "r") as file:
        return json.load(file)

class TestBridgesSolver(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.boards = load_boards()

    def setUp(self):
        """
        This method is run before each test to set up any state.
        It could be used to initialize grids or other required variables.
        """

    def create_board(self, board_name):
        """Creates a Board instance from JSON data"""
        data = self.boards[board_name]
        board = Board(data["height"], data["width"])

        for i, row in enumerate(data["grid"]):
            for j, cell in enumerate(row):
                if data["grid"][i][j].isnumeric():
                    board.set_number(NumberTile(int(data["grid"][i][j]), i, j, ))

        return board

    def test_game_complex(self):
        grid = self.create_board("grid_complex")
        (complete, final_grid), process = start(grid)
        print("-----------------------------------------------\n")
        print(final_grid)
        print("\n-----------------------------------------------")
        print(" - > is complete? [", complete, "] < - ")

        assert complete

        # display_process(process)

    def test_game_normal_big(self):
        grid = self.create_board("grid_normal_big")
        (complete, final_grid), process = start(grid)
        print("-----------------------------------------------\n")
        print(final_grid)
        print("\n-----------------------------------------------")
        print(" - > is complete? [",complete,"] < - ")

        assert complete

        # display_process(process)

    def test_game_hard_small(self):
        grid = self.create_board("grid_hard_small")
        (complete, final_grid), process = start(grid)
        print("-----------------------------------------------\n")
        print(final_grid)
        print("\n-----------------------------------------------")
        print(" - > is complete? [", complete, "] < - ")

        assert complete

    def test_game_normal_small(self):
        grid = self.create_board("grid_normal_small")
        (complete, final_grid), process = start(grid)
        print("-----------------------------------------------\n")
        print(final_grid)
        print("\n-----------------------------------------------")
        print(" - > is complete? [",complete,"] < - ")

        assert complete

    def test_game_hard_big(self):
        grid = self.create_board("grid_hard_big")
        (complete, final_grid), process = start(grid)
        print("-----------------------------------------------\n")
        print(final_grid)
        print("\n-----------------------------------------------")
        print(" - > is complete? [", complete, "] < - ")

        assert complete

        # display_process(process)

    def test_populate_number_tile_fields(self):
        grid = Board(3, 3)

        numbers = [
            NumberTile(4, 0, 0),
            NumberTile(2, 2, 0),
            NumberTile(3, 0, 2),
            NumberTile(1, 2, 2),
        ]

        for number in numbers:
            grid.set_number(number)

        set_possible_connections(grid.grid, numbers[0])
        self.assertEqual(numbers[0].get_num_possible_connections(), 4)
        self.assertIn(numbers[1], numbers[0]._pos_connections)
        self.assertIn(numbers[2], numbers[0]._pos_connections)
        self.assertNotIn(numbers[3], numbers[0]._pos_connections)

        set_possible_connections(grid.grid, numbers[1])
        self.assertEqual(numbers[1].get_num_possible_connections(), 3)

        set_possible_connections(grid.grid, numbers[2])
        self.assertEqual(numbers[1].get_num_possible_connections(), 3)

        set_possible_connections(grid.grid, numbers[3])
        self.assertEqual(numbers[3].get_num_possible_connections(), 2)

        # sort test
        numbers_sorted = [
            NumberTile(4, 0, 0),
            NumberTile(2, 2, 0),
            NumberTile(3, 0, 2),
            NumberTile(1, 2, 2),
        ]

        self.assertNotEqual(numbers,numbers_sorted)
        self.assertNotEqual(numbers.sort(key=sort),numbers_sorted)

        # make connections test

        make_connections([numbers[0]], grid)
        self.assertEqual(numbers[0].get_num_possible_connections(), 0)

        make_connections([numbers[1]], grid)
        self.assertEqual(numbers[1].get_num_possible_connections(), 0)

        make_connections([numbers[2]], grid)
        self.assertEqual(numbers[2].get_num_possible_connections(), 0)

        make_connections([numbers[3]], grid)
        self.assertEqual(numbers[3].get_num_possible_connections(), 0)

    def test_2(self):
        grid = Board(5, 5)

        numbers = [
            NumberTile(1, 0, 2),
            NumberTile(3, 4, 2),
            NumberTile(2, 4, 0),
            NumberTile(1, 2, 0),
            NumberTile(2, 4, 4),
            NumberTile(1, 2, 4),
        ]

        for number in numbers:
            grid.set_number(number)

        get_and_populate_numbers(grid.grid)

        handle_mandatory_connections(grid, numbers[0])
        self.assertEqual(numbers[0].get_num_possible_connections(), 0)

        handle_mandatory_connections(grid, numbers[3])
        self.assertEqual(numbers[3].get_num_possible_connections(), 0)

        self.assertEqual(numbers[4].get_num_possible_connections(), 3)
        handle_reducible_connections(grid, numbers[4])
        self.assertEqual(numbers[4].get_num_possible_connections(), 2)

    def test_3(self):
        grid = Board(5, 5)

        numbers = [
            NumberTile(3, 0, 0),
            NumberTile(2, 0, 2),
            NumberTile(3, 2, 0),
        ]

        for number in numbers:
            grid.set_number(number)

        get_and_populate_numbers(grid.grid)

        make_connections([numbers[1]],grid)
        self.assertEqual(numbers[1].get_num_possible_connections(), 0)

        make_connections([numbers[0]],grid)
        self.assertEqual(numbers[0].get_num_possible_connections(), 0)

    def test_4(self):
        grid = Board(5, 3)

        numbers = [
            NumberTile(2, 0, 0),
            NumberTile(2, 2, 0),
            NumberTile(1, 0, 2),
            NumberTile(3, 2, 2),
            NumberTile(2, 4, 2),
        ]

        for number in numbers:
            grid.set_number(number)

        get_and_populate_numbers(grid.grid)

        make_connections([numbers[4]], grid)
        numbers.remove(numbers[4])
        make_connections([numbers[0]], grid)
        numbers.sort(key=sort)

if __name__ == '__main__':
    unittest.main()

    # python -m unittest discover tests/

    # python -m unittest tests.test_solver.TestBridgesSolver.test_3


