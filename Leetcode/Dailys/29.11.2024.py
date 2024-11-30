from heapq import heappop, heappush


class Solution:
    def minimumTime(self, grid: list[list[int]]) -> int:
        if 1 not in (grid[0][1], grid[1][0]) and 0 not in (grid[0][1], grid[1][0]):
            return -1

        rows: int = len(grid)
        cols: int = len(grid[0])

        def dijkstra() -> int:
            trg: tuple[int, int] = (rows - 1, cols - 1)
            heap: list[tuple[int, int, int]] = [(0, 0, 0)]  # (current_time, row, col)
            grid[0][0] = -1

            while heap:
                cur_time, row, col = heappop(heap)

                if (row, col) == trg:
                    return cur_time

                for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nrow, ncol = row + dr, col + dc
                    if 0 <= nrow < rows and 0 <= ncol < cols and grid[nrow][ncol] != -1:
                        if grid[nrow][ncol] <= cur_time:
                            next_time = cur_time + 1
                        elif (grid[nrow][ncol] - cur_time) & 1 == 1:
                            next_time = (grid[nrow][ncol] - cur_time) + cur_time
                        else:
                            next_time = (grid[nrow][ncol] - cur_time + 1) + cur_time
                        grid[nrow][ncol] = -1
                        heappush(heap, (next_time, nrow, ncol))
            return -1

        return dijkstra()
