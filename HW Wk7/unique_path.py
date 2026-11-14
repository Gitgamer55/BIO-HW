memo = {}

def get_neighbours(point, maze):
    row, col = point
    rows = len(maze)
    cols = len(maze[0])
    neighbors = []
    directions = [(0, 1), (1, 0)]
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == 0:
            neighbors.append((new_row, new_col))
    return neighbors


def dfs(point, dest, maze):
    if point == dest: return 1
    if point in memo: return memo[point]

    neighbors = get_neighbours(point, maze)
    counter = 0
    for neighbor in neighbors: counter += dfs(neighbor, dest, maze)
    memo[point] = counter
    return counter


maze = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

dest = (len(maze) - 1, len(maze[0]) - 1)
result = dfs((0, 0), dest, maze)

print(result) 