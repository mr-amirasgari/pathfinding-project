
# Pathfinding in a 20x20 Grid

This Python project demonstrates pathfinding in a 20x20 grid using the **Breadth-First Search (BFS)** algorithm. An agent (blue) finds the optimal path to a target (red) while avoiding obstacles (black).

## Features

- **Dynamic Grid Generation**: Randomly placed obstacles.
- **Random Start and Target**: Positions are generated dynamically.
- **Path Analysis**: Uses BFS to find the shortest path without physical movement.
- **Visual Output**: Displays the grid with a legend using `matplotlib`.

## Visualization Legend

- **Blue**: Agent (Player)
- **Red**: Target (Goal)
- **Lime**: Optimal Path
- **Black**: Obstacle

## Requirements

- Python 3.x
- Libraries:
  - `numpy`
  - `matplotlib`

Install dependencies:

```bash
pip install numpy matplotlib
```
How to Run:

1.Save the script as pathfinding.py.
2.Execute:
```bash
python pathfinding.py
```
Output

The program prints the number of steps in the shortest path and displays a visual grid with a legend on the right side.

Made with ❤️ by Amir Mohammad Asgari.
