# bridges-solver

This repo contains an algorithm for solving the logic puzzle bridges.

## What is bridges?

Bridges (or Hashi) is a type of logic puzzle. It's played on a rectangular grid with no standard size, with some cells having numbers from 1 to 8 inclusive; these are the "islands", the rest of the cells are empty. 

The goal is to connect all of the islands by drawing a series of bridges between the islands. With the bridges following these criteria:
- They must begin and end at distinct islands.
- They must not cross any other bridges or islands.
- They cannot go diagonally.
- A pair of islands can be connected by at most 2 bridges.
- The number of bridges connected to each island must match the number on the island. E.g. an island with a '1' can only have 1 bridge, while a '3' must have 3 bridges.
- The bridges must connect the islands into a single connected group.

Example:

![Screenshot 2025-03-11 at 09 19 04](https://github.com/user-attachments/assets/eeb0978a-673b-4153-a266-45cc08d2db0d)

## My approach

### Extract and prepare tiles
- Collect all number tiles on the grid.
- Populate possible connections for each tile based on the board layout.

### Deterministic solving
- `handle_mandatory_connections`: Apply guaranteed connections.
- `handle_reducible_connections`: Apply connections that can be logically deduced.

### Recursive backtracking
- `handle_guess_and_check`: For complex puzzles, make a guess and recursively check if it leads to a valid solution.
- If a guess fails, backtrack and try alternative connections.

### Heuristics
- Tiles are sorted by the number of possible connections to reduce branching in the recursion.

### TDD methodology
- Tests start with simple puzzles and gradually increase in complexity, ensuring that each function is robust before moving on to more challenging boards.
