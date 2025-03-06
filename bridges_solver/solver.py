from bridges_solver.grid import Grid, NumberTile, Direction

def solve_puzzle(grid):
    """
    Function to solve the 'Bridges' puzzle. (Placeholder function)
    This should be replaced with your actual puzzle-solving algorithm.
    
    :param grid: A 2D list representing the puzzle grid
    :return: A 2D list representing the solved puzzle grid
    """
    # Placeholder implementation (just returns the input grid for now)
    return grid

def is_valid_move(grid, move):
    """
    Function to check if a move is valid in the 'Bridges' puzzle.
    
    :param grid: A 2D list representing the puzzle grid
    :param move: A tuple representing the move
    :return: True if the move is valid, False otherwise
    """
    # Placeholder validation (currently, it always returns True)
    return True



def Start(grid):
    numbers = setNumPosConnections(grid.grid)

    numbers.sort(key=sort)

    makeConnections(numbers, grid)

def makeConnections(numbers, grid):
    if len(numbers) == 0:
        return
    
    for num in numbers:
        print(num._number, num._numConnectionsLeft, num._numPosConnections)

    number = numbers[0]
    if number._numConnectionsLeft != number._numPosConnections:
        return

    posCons = number.get_possible_connections()
    for conNumber in list(posCons.keys()):
        if len(posCons) == 0:
            break

        if posCons[conNumber].numPossible == 2:
            grid.connect_numbers(number, conNumber)

        grid.connect_numbers(number, conNumber)

    numbers.remove(number)

    numbers.sort(key=sort)  

    print(grid,"\n") 
    
    return makeConnections(numbers, grid)
    



def sort(number):
    return number._numPosConnections-number._numConnectionsLeft


def setNumPosConnections(grid):
    numbers = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if isinstance(grid[i][j], NumberTile):
                populateNumberTileFields(grid, grid[i][j])

                numbers.append(grid[i][j])

    return numbers

def populateNumberTileFields(grid, numberTile):
    x, y = numberTile.x, numberTile.y
    rows, cols = len(grid), len(grid[0])

    for j in range(y - 1, -1, -1):  # Move left
        if isinstance(grid[x][j], NumberTile):
            numCons = min(2, grid[x][j]._number, numberTile._number)

            numberTile.set_possible_connection(Direction.LEFT, numCons, grid[x][j])
            break

    for j in range(y + 1, cols):  # Move right
        if isinstance(grid[x][j], NumberTile):
            numCons = min(2, grid[x][j]._number, numberTile._number)

            numberTile.set_possible_connection(Direction.RIGHT, numCons, grid[x][j])
            break

    for i in range(x - 1, -1, -1):  # Move up
        if isinstance(grid[i][y], NumberTile):
            numCons = min(2, grid[i][y]._number, numberTile._number)

            numberTile.set_possible_connection(Direction.UP, numCons, grid[i][y])
            break

    for i in range(x + 1, rows):  # Move down
        if isinstance(grid[i][y], NumberTile):
            numCons = min(2, grid[i][y]._number, numberTile._number)

            numberTile.set_possible_connection(Direction.DOWN, numCons, grid[i][y])
            break
