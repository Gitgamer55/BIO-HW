memo = {}

def get_neighbours(point):
    row, col = point
    return [(row+1, col), (row+1, col+1)]

def dfs(point, triangle):
    row, col = point
    if row == len(triangle) - 1: return triangle[row][col]
    if point in memo: return memo[point]

    neighbours = get_neighbours(point)
    best = float('inf')

    for neighbour in neighbours: best = min(best, dfs(neighbour, triangle))

    best += triangle[row][col]

    return best


triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

result = dfs((0, 0), triangle)

