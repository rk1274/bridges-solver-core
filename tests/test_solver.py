import unittest
from bridges_solver.solver import solve_puzzle, is_valid_move, populateNumberTileFields,setNumPosConnections, Start
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

        
        print(grid)

        print("---------------------------")

        #grid.connect_numbers(NumberTile(1, 6, 6), NumberTile(1, 6, 0))
        #grid.connect_numbers(NumberTile(4, 0, 0), NumberTile(3, 0, 3))
        #grid.connect_numbers(NumberTile(3, 5, 3), NumberTile(5, 2, 3))

        #print(grid)

        print("---------------------------")

        #grid.connect_numbers(NumberTile(1, 6, 6), NumberTile(1, 6, 0))
        #grid.connect_numbers(NumberTile(3, 5, 3), NumberTile(5, 2, 3))

        self.grid = grid
        #print(grid)

    def test_populate_number_tile_fields(self):
        Start(self.grid)
        print(self.grid)
        #setNumPosConnections(self.grid.grid)
        #populateNumberTileFields(self.grid.grid,NumberTile(6, 2, 0))
        
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