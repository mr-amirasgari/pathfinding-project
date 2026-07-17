import numpy as np

from pathfinding import bfs_find_path


def test_bfs_finds_shortest_path() -> None:
    grid = np.array(
        [
            [0, 0, 0],
            [1, 1, 0],
            [0, 0, 0],
        ],
        dtype=np.int8,
    )

    path, visited_count = bfs_find_path(
        grid,
        start=(0, 0),
        goal=(2, 2),
    )

    assert path == [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 2),
        (2, 2),
    ]
    assert visited_count > 0


def test_bfs_returns_none_when_no_path_exists() -> None:
    grid = np.array(
        [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0],
        ],
        dtype=np.int8,
    )

    path, visited_count = bfs_find_path(
        grid,
        start=(0, 0),
        goal=(2, 2),
    )

    assert path is None
    assert visited_count == 1


def test_bfs_handles_same_start_and_goal() -> None:
    grid = np.zeros((2, 2), dtype=np.int8)

    path, visited_count = bfs_find_path(
        grid,
        start=(1, 1),
        goal=(1, 1),
    )

    assert path == [(1, 1)]
    assert visited_count == 1