<div align="center">

# BFS Pathfinding Visualizer

A Python project that finds and visualizes the shortest path across a randomly generated grid using Breadth-First Search.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Algorithm](https://img.shields.io/badge/Algorithm-BFS-6C63FF?style=for-the-badge)

</div>

---

## Overview

The program generates a square grid containing random obstacles, selects free start and goal positions, and uses Breadth-First Search to find the shortest path between them.

The result is displayed with Matplotlib.

## Features

- Random grid generation
- Configurable grid size
- Configurable obstacle ratio
- Reproducible results with a random seed
- Shortest-path search using BFS
- Memory-efficient parent-based path reconstruction
- Matplotlib visualization
- Automated tests with Pytest
- Command-line arguments

## Visualization

| Color | Meaning |
|---|---|
| White | Free cell |
| Black | Obstacle |
| Blue | Start position |
| Red | Goal position |
| Lime | Shortest path |

## Project Structure

```text
pathfinding-project/
├── tests/
│   └── test_pathfinding.py
├── .gitignore
├── EXPLANATION.md
├── pathfinding.py
├── pytest.ini
├── README.md
├── requirements-dev.txt
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone https://github.com/mr-amirasgari/pathfinding-project.git
cd pathfinding-project
```

Install runtime dependencies:

```bash
python -m pip install -r requirements.txt
```

Install development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

## Usage

Run with default settings:

```bash
python pathfinding.py
```

Run with custom settings:

```bash
python pathfinding.py --size 30 --obstacle-ratio 0.25 --seed 42
```

### Arguments

| Argument | Description | Default |
|---|---|---|
| `--size` | Grid width and height | `20` |
| `--obstacle-ratio` | Fraction of obstacle cells | `0.2` |
| `--seed` | Random seed for reproducible output | None |

## Example Output

```text
Path found in 6 steps.
Visited cells: 40
Start: (15, 16)
Goal: (19, 18)
```

## Tests

Run all tests:

```bash
pytest
```

The tests cover:

- Finding the expected shortest path
- Detecting when no path exists
- Handling identical start and goal positions

## Algorithm

Breadth-First Search explores the grid level by level. Because every movement has equal cost, BFS guarantees a shortest path in this unweighted grid.

Movement is limited to four directions:

- Up
- Down
- Left
- Right

For additional technical details, see [EXPLANATION.md](./EXPLANATION.md).

## Possible Improvements

- Add A* search
- Add Dijkstra's algorithm
- Animate the search process
- Support weighted terrain
- Allow diagonal movement
- Add interactive start and goal selection
- Compare algorithm performance

## Author

**Amir Mohammad Asgari**

[GitHub Profile](https://github.com/mr-amirasgari)