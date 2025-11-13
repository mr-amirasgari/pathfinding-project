import numpy as np
import matplotlib.pyplot as plt
from collections import deque

def generate_random_valid_position(grid):
    size = len(grid)
    while True:
        r = np.random.randint(0, size)
        c = np.random.randint(0, size)
        if grid[r, c] == 0:  # Only free cells
            return (r, c)

def generate_grid_with_obstacles(size=20, obstacle_ratio=0.2):
    grid = np.zeros((size, size), dtype=int)
    total_cells = size * size
    num_obstacles = int(total_cells * obstacle_ratio)
    obstacles = np.random.choice(total_cells, num_obstacles, replace=False)
    obs_positions = np.unravel_index(obstacles, (size, size))
    grid[obs_positions] = 1
    return grid

def bfs_find_path(grid, start, goal):
    n = len(grid)
    if start == goal:
        return [start]
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        (r, c), path = queue.popleft()
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr, nc] == 0 and (nr, nc) not in visited:
                if (nr, nc) == goal:
                    return path + [(nr, nc)]
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))
    return None

def visualize_path_with_legend(grid, start, goal, path):
    display = np.copy(grid)
    display[start] = 2   # Player
    display[goal] = 3    # Prize
    for pos in path:
        if pos != start and pos != goal:
            display[pos] = 4  # Path

    # Define colors
    cmap = plt.cm.colors.ListedColormap(['white', 'black', 'blue', 'red', 'lime'])
    bounds = [0,1,2,3,4,5]
    norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.imshow(display, cmap=cmap, norm=norm)
    ax.grid(color='gray', linewidth=0.5, which='both')
    ax.set_xticks([])
    ax.set_yticks([])

    # Add legend
    legend_elements = [
        plt.Line2D([0], [0], marker='s', color='w', markerfacecolor='blue', markersize=10, label='Player (Blue)'),
        plt.Line2D([0], [0], marker='s', color='w', markerfacecolor='red', markersize=10, label='Prize (Red)'),
        plt.Line2D([0], [0], marker='s', color='w', markerfacecolor='lime', markersize=10, label='Path (Lime)'),
        plt.Line2D([0], [0], marker='s', color='w', markerfacecolor='black', markersize=10, label='Obstacle (Black)'),
    ]
    ax.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10)
    plt.tight_layout()
    plt.title("Optimal Path Found via BFS Analysis")
    plt.show()

# --- RUN ---
grid = generate_grid_with_obstacles(20, obstacle_ratio=0.2)
start = generate_random_valid_position(grid)
goal = generate_random_valid_position(grid)
while goal == start:
    goal = generate_random_valid_position(grid)

path = bfs_find_path(grid, start, goal)

if path:
    print(f"✅ Path found! Steps: {len(path) - 1}")
    visualize_path_with_legend(grid, start, goal, path)
else:
    print("❌ No path exists between start and goal.")