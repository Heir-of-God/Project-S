class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        grid: list[list[str]] = [["-" for _ in range(n)] for _ in range(m)]

        for row, col in guards:
            grid[row][col] = "g"

        for row, col in walls:
            grid[row][col] = "w"

        res = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "g":
                    r: int = row + 1
                    c: int = col
                    while r < m and c < n and grid[r][c] not in "gw":
                        if grid[r][c] == "-":
                            res += 1
                            grid[r][c] = "+"
                        r += 1

                    r = row - 1
                    c = col
                    while 0 <= r and 0 <= c and grid[r][c] not in "gw":
                        if grid[r][c] == "-":
                            res += 1
                            grid[r][c] = "+"
                        r -= 1

                    r = row
                    c = col + 1
                    while r < m and c < n and grid[r][c] not in "gw":
                        if grid[r][c] == "-":
                            res += 1
                            grid[r][c] = "+"
                        c += 1

                    r = row
                    c = col - 1
                    while 0 <= r and 0 <= c and grid[r][c] not in "gw":
                        if grid[r][c] == "-":
                            res += 1
                            grid[r][c] = "+"
                        c -= 1

        return m * n - res - len(guards) - len(walls)
