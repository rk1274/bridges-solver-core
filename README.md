# bridges-solver

Bridges (or Hashi) is a type of logic puzzle. It's played on a rectangular grid with no standard size, with some cells having numbers from 1 to 8 inclusive; these are the "islands", the rest of the cells are empty. 

The goal is to connect all of the islands by drawing a series of bridges between the islands. With the bridges following these criteria:
- They must begin and end at distinct islands.
- They must not cross any other bridges or islands.
- They cannot go diagonally.
- A pair of islands can be connected by at most 2 bridges.
- The number of bridges connected to each island must match the number on the island. E.g. an island with a '1' can only have 1 bridge, while a '3' must have 3 bridges.
- The bridges must connect the islands into a single connected group.

Example

![Screenshot 2025-03-11 at 09 19 04](https://github.com/user-attachments/assets/eeb0978a-673b-4153-a266-45cc08d2db0d)
