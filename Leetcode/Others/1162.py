from collections import deque


class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        n: int = len(grid)

        def bfs(src_queue) -> int:
            if not src_queue or len(src_queue) == n**2:
                return -1
            queue = deque(src_queue)
            visited = set(src_queue)
            dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
            res = 0

            while queue:
                check_cells: int = len(queue)
                for _ in range(check_cells):
                    cur_row, cur_col = queue.popleft()
                    for delta_row, delta_col in dirs:
                        r, c = cur_row + delta_row, cur_col + delta_col
                        if 0 <= r < n and 0 <= c < n and (r, c) not in visited:
                            grid[r][c] = 1
                            queue.append((r, c))
                            visited.add((r, c))
                if queue:
                    res += 1
            return res

        src_queue: list[tuple[int, int]] = []
        for row_ind in range(n):
            for col_ind in range(n):
                if grid[row_ind][col_ind] == 1:
                    src_queue.append((row_ind, col_ind))
        return bfs(src_queue)
