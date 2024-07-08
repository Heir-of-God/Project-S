import os


def gridChallenge(grid: list[str]) -> str:
    cols: int = len(grid[0])

    grid = [sorted(lst) for lst in grid]
    for col_ind in range(cols):
        prev = None
        for row in grid:
            if prev is not None and ord(prev) > ord(row[col_ind]):
                return "NO"
            prev = row[col_ind]
    return "YES"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        grid = []
        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)
        result = gridChallenge(grid)
        fptr.write(result + "\n")
    fptr.close()
