import unittest
from bridges_solver.solver import set_possible_connections,make_connections, start, sort, get_and_populate_numbers
from bridges_solver.grid import Grid, NumberTile

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


        grid = Grid(7,7)
        #grid.set_number(NumberTile(3, 0, 0))
        #grid.set_number(NumberTile(4, 2, 0))
        #grid.set_number(NumberTile(4, 6, 0))
        #grid.set_number(NumberTile(3, 0, 2))
        #grid.set_number(NumberTile(3, 3, 2))
        #grid.set_number(NumberTile(4, 6, 2))
        #grid.set_number(NumberTile(1, 0, 5))
        #grid.set_number(NumberTile(3, 3, 5))
        #grid.set_number(NumberTile(2, 5, 5))
        #grid.set_number(NumberTile(2, 4, 6))
        #grid.set_number(NumberTile(3, 6, 6))

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
        
        #print(grid)

        #print("---------------------------")

        #grid.connect_numbers(NumberTile(1, 6, 6), NumberTile(1, 6, 0))
        #grid.connect_numbers(NumberTile(4, 0, 0), NumberTile(3, 0, 3))
        #grid.connect_numbers(NumberTile(3, 5, 3), NumberTile(5, 2, 3))

        #print(grid)

        #print("---------------------------")

        #grid.connect_numbers(NumberTile(1, 6, 6), NumberTile(1, 6, 0))
        #grid.connect_numbers(NumberTile(3, 5, 3), NumberTile(5, 2, 3))

        self.grid = grid
        #print(grid)

    def test_game(self):
        start(self.grid)
        print(self.grid)

    def test_populate_number_tile_fields(self):
        grid = Grid(3, 3)

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
        grid = Grid(5, 5)

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

        numbersUpdated = get_and_populate_numbers(grid.grid)

        make_connections([numbers[0]], grid)
        self.assertEqual(numbers[0].get_num_possible_connections(), 0)

        make_connections([numbers[3]], grid)
        self.assertEqual(numbers[3].get_num_possible_connections(), 0)

        print(grid)

    #def test_solve_puzzle(self):
        """
        Test the solve_puzzle function.
        Here, you would check if the puzzle is being solved correctly.
        """
       # result = solve_puzzle(self.sample_grid)
       # self.assertEqual(result, self.sample_grid)  # Since the placeholder just returns the input grid

    

if __name__ == '__main__':
    unittest.main()

    # python -m unittest discover tests/