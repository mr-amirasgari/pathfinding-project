# Project Explanation

## Overview

This project demonstrates shortest-path search on a randomly generated two-dimensional grid using the Breadth-First Search (BFS) algorithm.

The grid contains:

- Free cells
- Randomly generated obstacles
- A start position
- A goal position

The program searches for the shortest valid route from the start to the goal and visualizes the result with Matplotlib.

---

## Why Breadth-First Search?

Breadth-First Search explores nodes level by level.

In an unweighted grid where every movement has the same cost, BFS guarantees that the first path found to the goal is a shortest path.

The project allows movement in four directions:

- Up
- Down
- Left
- Right

Diagonal movement is not allowed.

---

## Main Workflow

1. Generate a square grid.
2. Add random obstacles according to the selected obstacle ratio.
3. Select two different free cells as the start and goal.
4. Run BFS from the start position.
5. Record each visited cell's parent.
6. Reconstruct the shortest path after reaching the goal.
7. Display the grid and search result.

---

## Path Reconstruction

Instead of storing a complete path inside every queue item, the program stores only the parent of each visited cell.

After BFS reaches the goal, the final path is reconstructed by moving backward from the goal to the start through the parent dictionary.

This approach uses less memory than repeatedly copying full paths.

---

## Visualization

The generated grid uses the following colors:

| Color | Meaning |
|---|---|
| White | Free cell |
| Black | Obstacle |
| Blue | Start position |
| Red | Goal position |
| Lime | Shortest path |

The window title also displays the number of steps in the discovered path.

---

## Command-Line Options

The program supports optional arguments:

```bash
python pathfinding.py --size 20 --obstacle-ratio 0.2 --seed 42
```

| Argument | Description |
|---|---|
| `--size` | Grid width and height |
| `--obstacle-ratio` | Fraction of cells used as obstacles |
| `--seed` | Optional seed for reproducible random results |

Example:

```bash
python pathfinding.py --size 30 --obstacle-ratio 0.25 --seed 10
```

---

## Complexity

For a grid with `V` cells and adjacency relationships represented by `E` edges:

- Time complexity: `O(V + E)`
- Space complexity: `O(V)`

For a rectangular grid, each cell has at most four neighbors, so the algorithm scales linearly with the number of cells.

---

## Tests

The automated tests verify that:

- BFS finds the expected shortest path.
- BFS returns `None` when no valid path exists.
- BFS handles the case where the start and goal are identical.

Run the tests with:

```bash
pytest
```

---

## Possible Applications

- Game AI
- Robot navigation
- Maze solving
- Route planning
- Search algorithm demonstrations
- Simulation environments

---

## Possible Improvements

- Add Dijkstra's algorithm
- Add A* search
- Support weighted terrain
- Add diagonal movement
- Animate the BFS exploration process
- Let the user manually select start and goal positions
- Add a graphical control panel
- Compare execution time across algorithms