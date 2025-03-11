import unittest
from bridges_solver.solver import set_possible_connections,make_connections, start, sort, get_and_populate_numbers, handle_when_1, handle_when_2
from bridges_solver.board import Board, NumberTile
import time

class TestBridgesSolver(unittest.TestCase):
    
    def setUp(self):
        """
        This method is run before each test to set up any state.
        It could be used to initialize grids or other required variables.
        """
        self.sample_grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.invalid_move = (1, 1)  # Example of an invalid move (placeholder)
        self.valid_move = (0, 1)    # Example of a valid move (placeholder)




        
        #print(grid)

        #print("---------------------------")

        #grid.connect_numbers(NumberTile(1, 6, 6), NumberTile(1, 6, 0))
        #grid.connect_numbers(NumberTile(4, 0, 0), NumberTile(3, 0, 3))
        #grid.connect_numbers(NumberTile(3, 5, 3), NumberTile(5, 2, 3))

        #print(grid)

        #print("---------------------------")

        #grid.connect_numbers(NumberTile(1, 6, 6), NumberTile(1, 6, 0))
        #grid.connect_numbers(NumberTile(3, 5, 3), NumberTile(5, 2, 3))

        self.grid = grid_2()
        #print(grid)

    def test_game_normal_big(self):
        grid = grid_1()
        (complete, final_grid), process = start(grid)
        print("-----------------------------------------------\n")
        print(final_grid)
        print("\n-----------------------------------------------")
        print(" - > is complete? [",complete,"] < - ")

        for frame in process:
            print("\033c", end="")  # Clears the screen for a smoother transition
            print(frame)
            time.sleep(0.1)

    def test_game_hard_small(self):
        grid = grid_2()
        complete, final_grid = start(grid)
        print("-----------------------------------------------\n")
        print(final_grid)
        print("\n-----------------------------------------------")
        print(" - > is complete? [",complete,"] < - ")

    def test_game_normal_small(self):
        grid = grid_3()
        complete, final_grid = start(grid)
        print("-----------------------------------------------\n")
        print(final_grid)
        print("\n-----------------------------------------------")
        print(" - > is complete? [",complete,"] < - ")

    def test_game_hard_big(self):
        grid = grid_4()
        (complete, final_grid), process = start(grid)
        print("-----------------------------------------------\n")
        print(final_grid)
        print("\n-----------------------------------------------")
        print(" - > is complete? [", complete, "] < - ")

        for frame in process:
            print("\033c", end="")  # Clears the screen for a smoother transition
            print(frame)
            time.sleep(0.1)

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

        handle_when_1(grid, numbers[0])
        self.assertEqual(numbers[0].get_num_possible_connections(), 0)

        handle_when_1(grid, numbers[3])
        self.assertEqual(numbers[3].get_num_possible_connections(), 0)

        self.assertEqual(numbers[4].get_num_possible_connections(), 3)
        handle_when_2(grid, numbers[4])
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

def grid_4():
    grid = Board(25, 25)

    grid.set_number(NumberTile(1, 0, 0))
    grid.set_number(NumberTile(1, 0, 3))
    grid.set_number(NumberTile(1, 0, 5))
    grid.set_number(NumberTile(2, 0, 7))
    grid.set_number(NumberTile(2, 0, 12))
    grid.set_number(NumberTile(2, 0, 24))

    grid.set_number(NumberTile(2, 1, 8))
    grid.set_number(NumberTile(3, 1, 15))
    grid.set_number(NumberTile(3, 1, 20))
    grid.set_number(NumberTile(1, 1, 23))

    grid.set_number(NumberTile(3, 2, 0))
    grid.set_number(NumberTile(6, 2, 3))
    grid.set_number(NumberTile(4, 2, 10))
    grid.set_number(NumberTile(2, 2, 12))
    grid.set_number(NumberTile(5, 2, 14))
    grid.set_number(NumberTile(2, 2, 19))

    # Third row
    grid.set_number(NumberTile(4, 4, 10))
    grid.set_number(NumberTile(2, 4, 22))

    # Fourth row
    grid.set_number(NumberTile(2, 5, 15))
    grid.set_number(NumberTile(5, 5, 17))
    grid.set_number(NumberTile(3, 5, 19))

    # Fifth row
    grid.set_number(NumberTile(2, 6, 10))

    grid.set_number(NumberTile(3, 7, 0))
    grid.set_number(NumberTile(6, 7, 3))
    grid.set_number(NumberTile(5, 7, 14))
    grid.set_number(NumberTile(6, 7, 17))
    grid.set_number(NumberTile(7, 7, 20))
    grid.set_number(NumberTile(5, 7, 22))

    grid.set_number(NumberTile(2, 8, 2))

    # Sixth row
    grid.set_number(NumberTile(2, 9, 17))

    grid.set_number(NumberTile(4, 10, 0))
    grid.set_number(NumberTile(5, 10, 2))


    # Seventh row
    grid.set_number(NumberTile(2, 11, 4))
    grid.set_number(NumberTile(3, 11, 14))
    grid.set_number(NumberTile(2, 11, 22))

    # Eighth row
    grid.set_number(NumberTile(1, 12, 2))
    grid.set_number(NumberTile(2, 12, 6))
    grid.set_number(NumberTile(3, 12, 9))
    grid.set_number(NumberTile(3, 12, 20))

    grid.set_number(NumberTile(5, 13, 0))
    grid.set_number(NumberTile(6, 13, 3))
    grid.set_number(NumberTile(5, 13, 23))

    # Ninth row
    grid.set_number(NumberTile(2, 15, 4))
    grid.set_number(NumberTile(3, 15, 9))
    grid.set_number(NumberTile(4, 15, 16))
    grid.set_number(NumberTile(1, 15, 20))

    grid.set_number(NumberTile(3, 16, 0))

    # Tenth row
    grid.set_number(NumberTile(2, 17, 23))

    grid.set_number(NumberTile(2, 18, 1))
    grid.set_number(NumberTile(5, 18, 3))
    grid.set_number(NumberTile(6, 18, 16))
    grid.set_number(NumberTile(4, 18, 24))


    # Twelfth row
    grid.set_number(NumberTile(3, 20, 0))
    grid.set_number(NumberTile(3, 20, 3))
    grid.set_number(NumberTile(2, 20, 11))
    grid.set_number(NumberTile(1, 20, 15))
    grid.set_number(NumberTile(2, 20, 17))
    grid.set_number(NumberTile(4, 20, 20))
    grid.set_number(NumberTile(2, 20, 22))

    grid.set_number(NumberTile(5, 22, 1))
    grid.set_number(NumberTile(3, 22, 15))
    grid.set_number(NumberTile(2, 22, 18))
    grid.set_number(NumberTile(3, 22, 20))

    grid.set_number(NumberTile(1, 23, 0))
    grid.set_number(NumberTile(2, 23, 24))

    # Thirteenth row
    grid.set_number(NumberTile(4, 24, 1))
    grid.set_number(NumberTile(3, 24, 4))
    grid.set_number(NumberTile(2, 24, 6))
    grid.set_number(NumberTile(3, 24, 16))
    grid.set_number(NumberTile(2, 24, 22))

    return grid

def grid_2():
    grid = Board(7, 7)

    grid.set_number(NumberTile(3, 0, 0))
    grid.set_number(NumberTile(4, 2, 0))
    grid.set_number(NumberTile(4, 6, 0))
    grid.set_number(NumberTile(3, 0, 2))
    grid.set_number(NumberTile(3, 3, 2))
    grid.set_number(NumberTile(4, 6, 2))
    grid.set_number(NumberTile(1, 0, 5))
    grid.set_number(NumberTile(3, 3, 5))
    grid.set_number(NumberTile(2, 5, 5))
    grid.set_number(NumberTile(2, 4, 6))
    grid.set_number(NumberTile(3, 6, 6))

    return grid

def grid_3():
    grid = Board(7, 7)

    grid.set_number(NumberTile(4, 0, 0))
    grid.set_number(NumberTile(6, 2, 0))
    grid.set_number(NumberTile(5, 4, 0))
    grid.set_number(NumberTile(1, 6, 0))
    grid.set_number(NumberTile(1, 5, 1))
    grid.set_number(NumberTile(2, 4, 2))
    grid.set_number(NumberTile(3, 0, 3))
    grid.set_number(NumberTile(5, 2, 3))
    grid.set_number(NumberTile(3, 5, 3))
    grid.set_number(NumberTile(1, 0, 5))
    grid.set_number(NumberTile(2, 3, 5))
    grid.set_number(NumberTile(3, 5, 5))
    grid.set_number(NumberTile(3, 2, 6))
    grid.set_number(NumberTile(1, 6, 6))

    return grid

def grid_1():
    grid = Board(25, 25)

    # First row
    grid.set_number(NumberTile(2, 0, 0))
    grid.set_number(NumberTile(2, 0, 3))
    grid.set_number(NumberTile(3, 0, 7))
    grid.set_number(NumberTile(5, 0, 22))
    grid.set_number(NumberTile(4, 0, 24))

    # Second row
    grid.set_number(NumberTile(4, 2, 0))
    grid.set_number(NumberTile(2, 2, 21))

    # Third row
    grid.set_number(NumberTile(1, 3, 6))
    grid.set_number(NumberTile(5, 3, 8))
    grid.set_number(NumberTile(3, 3, 22))

    # Fourth row
    grid.set_number(NumberTile(4, 5, 8))
    grid.set_number(NumberTile(4, 5, 21))
    grid.set_number(NumberTile(5, 5, 24))

    # Fifth row
    grid.set_number(NumberTile(4, 7, 0))
    grid.set_number(NumberTile(4, 7, 24))

    # Sixth row
    grid.set_number(NumberTile(2, 9, 0))
    grid.set_number(NumberTile(1, 9, 2))
    grid.set_number(NumberTile(2, 9, 6))
    grid.set_number(NumberTile(3, 9, 8))
    grid.set_number(NumberTile(3, 9, 22))

    # Seventh row
    grid.set_number(NumberTile(2, 11, 0))
    grid.set_number(NumberTile(3, 11, 19))
    grid.set_number(NumberTile(4, 11, 22))

    # Eighth row
    grid.set_number(NumberTile(4, 13, 1))
    grid.set_number(NumberTile(3, 13, 4))
    grid.set_number(NumberTile(1, 13, 6))
    grid.set_number(NumberTile(3, 13, 9))
    grid.set_number(NumberTile(1, 13, 11))
    grid.set_number(NumberTile(4, 13, 17))
    grid.set_number(NumberTile(4, 13, 24))

    # Ninth row
    grid.set_number(NumberTile(2, 15, 1))
    grid.set_number(NumberTile(2, 15, 5))
    grid.set_number(NumberTile(7, 15, 9))
    grid.set_number(NumberTile(4, 15, 17))
    grid.set_number(NumberTile(3, 15, 21))
    grid.set_number(NumberTile(3, 15, 23))

    # Tenth row
    grid.set_number(NumberTile(4, 17, 0))
    grid.set_number(NumberTile(5, 17, 4))
    grid.set_number(NumberTile(4, 17, 7))
    grid.set_number(NumberTile(3, 17, 12))
    grid.set_number(NumberTile(5, 17, 14))
    grid.set_number(NumberTile(4, 17, 16))
    grid.set_number(NumberTile(3, 17, 18))
    grid.set_number(NumberTile(1, 17, 20))

    grid.set_number(NumberTile(3, 18, 1))
    grid.set_number(NumberTile(1, 18, 3))
    grid.set_number(NumberTile(2, 18, 6))
    # Eleventh row

    grid.set_number(NumberTile(1, 19, 14))
    grid.set_number(NumberTile(2, 19, 16))
    grid.set_number(NumberTile(5, 19, 18))
    grid.set_number(NumberTile(4, 19, 21))
    grid.set_number(NumberTile(3, 19, 24))

    # Twelfth row
    grid.set_number(NumberTile(3, 20, 1))
    grid.set_number(NumberTile(2, 20, 3))
    grid.set_number(NumberTile(4, 20, 6))
    grid.set_number(NumberTile(2, 20, 10))
    grid.set_number(NumberTile(7, 20, 12))
    grid.set_number(NumberTile(5, 20, 17))
    grid.set_number(NumberTile(2, 20, 23))

    grid.set_number(NumberTile(2, 21, 18))
    grid.set_number(NumberTile(2, 21, 20))
    grid.set_number(NumberTile(3, 21, 22))
    grid.set_number(NumberTile(6, 21, 24))

    grid.set_number(NumberTile(3, 22, 4))
    grid.set_number(NumberTile(4, 22, 6))
    grid.set_number(NumberTile(2, 22, 14))
    grid.set_number(NumberTile(5, 22, 17))
    grid.set_number(NumberTile(1, 22, 19))

    grid.set_number(NumberTile(2, 23, 7))
    grid.set_number(NumberTile(3, 23, 12))
    grid.set_number(NumberTile(1, 23, 18))
    grid.set_number(NumberTile(1, 23, 20))
    grid.set_number(NumberTile(1, 23, 22))
    grid.set_number(NumberTile(2, 23, 24))

    # Thirteenth row
    grid.set_number(NumberTile(4, 24, 0))
    grid.set_number(NumberTile(4, 24, 3))
    grid.set_number(NumberTile(5, 24, 9))
    grid.set_number(NumberTile(4, 24, 21))
    grid.set_number(NumberTile(1, 24, 23))

    return grid

if __name__ == '__main__':
    unittest.main()

    # python -m unittest discover tests/

    # python -m unittest tests.test_solver.TestBridgesSolver.test_3
