class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows: int = len(grid)
        cols: int = len(grid[0])

        top: int = rows
        bottom: int = -1
        left: int = cols
        right: int = -1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    top = min(top, i)
                    bottom = max(bottom, i)
                    left = min(left, j)
                    right = max(right, j)

        if bottom == -1:
            return 0

        height: int = bottom - top + 1
        width: int = right - left + 1

        return height * width
