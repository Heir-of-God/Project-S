import os


def get_new_positions(grid, dp, x, y):
    ranges = [
        [[x, y] for x in range(x + 1, n)],
        [[x, y] for x in range(x - 1, -1, -1)],
        [[x, y] for y in range(y + 1, n)],
        [[x, y] for y in range(y - 1, -1, -1)],
    ]
    result = []
    for r in ranges:
        for [x, y] in r:
            if grid[x][y] == "X" or dp[x][y] != -1:
                break
            result.append([x, y])
    return result


def minimumMoves(grid, startX, startY, goalX, goalY):
    n: int = len(grid)
    dp: list[list[int]] = [[-1 for i in range(n)] for i in range(n)]
    move = 0
    dp[startX][startY] = move
    currentPositions = [[startX, startY]]
    while len(currentPositions) > 0:
        nextPositions = []
        for [x, y] in currentPositions:
            nextPositions += get_new_positions(grid, dp, x, y)
        move += 1
        for [x, y] in nextPositions:
            dp[x][y] = move
        currentPositions = nextPositions
    return dp[goalX][goalY]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    first_multiple_input = input().rstrip().split()
    startX = int(first_multiple_input[0])
    startY = int(first_multiple_input[1])
    goalX = int(first_multiple_input[2])
    goalY = int(first_multiple_input[3])
    result = minimumMoves(grid, startX, startY, goalX, goalY)
    fptr.write(str(result) + "\n")
    fptr.close()
