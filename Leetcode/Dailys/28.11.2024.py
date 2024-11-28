from heapq import heappop, heappush


class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0])
        heap: list[tuple[int, int, int]] = [(0, 0, 0)]  # (distance, row, col)
        visited: set[tuple[int, int]] = set([(0, 0)])

        while heap:
            dist, row, col = heappop(heap)

            visited.add((row, col))
            if (row, col) == (rows - 1, cols - 1):
                return dist

            for dr, dc in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                if 0 <= row + dr < rows and 0 <= col + dc < cols and (row + dr, col + dc) not in visited:
                    heappush(heap, (dist + grid[row + dr][col + dc], row + dr, col + dc))
                    visited.add((row + dr, col + dc))

        return -1
