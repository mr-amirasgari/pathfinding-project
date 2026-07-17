"""Random-grid pathfinding visualizer using Breadth-First Search (BFS)."""

from __future__ import annotations

import argparse
from collections import deque
from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import BoundaryNorm, ListedColormap

Position = tuple[int, int]
Path = list[Position]

DIRECTIONS: tuple[Position, ...] = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
)


def validate_settings(size: int, obstacle_ratio: float) -> None:
    """Validate grid-generation settings."""
    if size < 2:
        raise ValueError("Grid size must be at least 2.")

    if not 0 <= obstacle_ratio < 1:
        raise ValueError("Obstacle ratio must be between 0 and 1.")


def generate_grid_with_obstacles(
    size: int,
    obstacle_ratio: float,
    rng: np.random.Generator,
) -> np.ndarray:
    """Create a square grid containing randomly placed obstacles."""
    validate_settings(size, obstacle_ratio)

    grid = np.zeros((size, size), dtype=np.int8)
    obstacle_count = int(grid.size * obstacle_ratio)

    obstacle_indices = rng.choice(
        grid.size,
        size=obstacle_count,
        replace=False,
    )
    grid.flat[obstacle_indices] = 1

    return grid


def get_random_free_position(
    grid: np.ndarray,
    rng: np.random.Generator,
    excluded: Optional[set[Position]] = None,
) -> Position:
    """Return a random free cell that is not excluded."""
    excluded = excluded or set()

    free_positions = [
        (int(row), int(column))
        for row, column in np.argwhere(grid == 0)
        if (int(row), int(column)) not in excluded
    ]

    if not free_positions:
        raise ValueError("The grid does not contain enough free cells.")

    index = int(rng.integers(0, len(free_positions)))
    return free_positions[index]


def reconstruct_path(
    parents: dict[Position, Optional[Position]],
    goal: Position,
) -> Path:
    """Reconstruct a path from the goal to the start."""
    path: Path = []
    current: Optional[Position] = goal

    while current is not None:
        path.append(current)
        current = parents[current]

    path.reverse()
    return path


def bfs_find_path(
    grid: np.ndarray,
    start: Position,
    goal: Position,
) -> tuple[Optional[Path], int]:
    """Find the shortest path from start to goal using BFS."""
    if start == goal:
        return [start], 1

    row_count, column_count = grid.shape
    queue: deque[Position] = deque([start])
    parents: dict[Position, Optional[Position]] = {start: None}

    while queue:
        row, column = queue.popleft()

        for row_offset, column_offset in DIRECTIONS:
            next_position = (
                row + row_offset,
                column + column_offset,
            )
            next_row, next_column = next_position

            is_inside_grid = (
                0 <= next_row < row_count
                and 0 <= next_column < column_count
            )

            if not is_inside_grid:
                continue

            if grid[next_position] == 1:
                continue

            if next_position in parents:
                continue

            parents[next_position] = (row, column)

            if next_position == goal:
                return reconstruct_path(parents, goal), len(parents)

            queue.append(next_position)

    return None, len(parents)


def visualize_grid(
    grid: np.ndarray,
    start: Position,
    goal: Position,
    path: Optional[Path],
) -> None:
    """Display the generated grid and the shortest path."""
    display_grid = np.copy(grid)
    display_grid[start] = 2
    display_grid[goal] = 3

    if path:
        for position in path[1:-1]:
            display_grid[position] = 4

    color_map = ListedColormap(
        ["white", "black", "blue", "red", "lime"]
    )
    boundaries = [0, 1, 2, 3, 4, 5]
    normalization = BoundaryNorm(boundaries, color_map.N)

    figure, axes = plt.subplots(figsize=(10, 8))
    axes.imshow(
        display_grid,
        cmap=color_map,
        norm=normalization,
    )

    axes.set_xticks(
        np.arange(-0.5, grid.shape[1], 1),
        minor=True,
    )
    axes.set_yticks(
        np.arange(-0.5, grid.shape[0], 1),
        minor=True,
    )
    axes.grid(which="minor", linewidth=0.5)
    axes.tick_params(
        which="both",
        bottom=False,
        left=False,
        labelbottom=False,
        labelleft=False,
    )

    legend_items = [
        plt.Line2D(
            [0],
            [0],
            marker="s",
            linestyle="",
            markerfacecolor="blue",
            markersize=10,
            label="Start",
        ),
        plt.Line2D(
            [0],
            [0],
            marker="s",
            linestyle="",
            markerfacecolor="red",
            markersize=10,
            label="Goal",
        ),
        plt.Line2D(
            [0],
            [0],
            marker="s",
            linestyle="",
            markerfacecolor="lime",
            markersize=10,
            label="Shortest path",
        ),
        plt.Line2D(
            [0],
            [0],
            marker="s",
            linestyle="",
            markerfacecolor="black",
            markersize=10,
            label="Obstacle",
        ),
    ]

    axes.legend(
        handles=legend_items,
        loc="center left",
        bbox_to_anchor=(1, 0.5),
    )

    title = (
        f"BFS Shortest Path — {len(path) - 1} steps"
        if path
        else "BFS Pathfinding — No Path Found"
    )
    axes.set_title(title)

    figure.tight_layout()
    plt.show()


def parse_arguments() -> argparse.Namespace:
    """Read command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Visualize BFS pathfinding on a random grid."
    )
    parser.add_argument(
        "--size",
        type=int,
        default=20,
        help="Grid width and height. Default: 20",
    )
    parser.add_argument(
        "--obstacle-ratio",
        type=float,
        default=0.2,
        help="Fraction of cells containing obstacles. Default: 0.2",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Optional random seed for reproducible results.",
    )
    return parser.parse_args()


def main() -> None:
    """Generate a grid, run BFS, and display the result."""
    arguments = parse_arguments()
    validate_settings(arguments.size, arguments.obstacle_ratio)

    rng = np.random.default_rng(arguments.seed)

    grid = generate_grid_with_obstacles(
        size=arguments.size,
        obstacle_ratio=arguments.obstacle_ratio,
        rng=rng,
    )

    start = get_random_free_position(grid, rng)
    goal = get_random_free_position(
        grid,
        rng,
        excluded={start},
    )

    path, visited_count = bfs_find_path(
        grid,
        start,
        goal,
    )

    if path:
        print(f"Path found in {len(path) - 1} steps.")
    else:
        print("No path exists between the start and goal.")

    print(f"Visited cells: {visited_count}")
    print(f"Start: {start}")
    print(f"Goal: {goal}")

    visualize_grid(
        grid,
        start,
        goal,
        path,
    )


if __name__ == "__main__":
    main()