from collections import deque
import heapq


class Solution:
    def __init__(self) -> None:
        self.roww: list[int] = [0, 0, -1, 1]
        self.coll: list[int] = [-1, 1, 0, 0]

    def bfs(self, grid, score, n) -> None:
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    score[i][j] = 0
                    q.append((i, j))

        while q:
            x, y = q.popleft()
            s = score[x][y]

            for i in range(4):
                new_x = x + self.roww[i]
                new_y = y + self.coll[i]

                if 0 <= new_x < n and 0 <= new_y < n and score[new_x][new_y] > s + 1:
                    score[new_x][new_y] = s + 1
                    q.append((new_x, new_y))

    def maximumSafenessFactor(self, grid):
        n: int = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return 0

        score = [[float("inf")] * n for _ in range(n)]
        self.bfs(grid, score, n)

        vis = [[False] * n for _ in range(n)]
        pq = [(-score[0][0], 0, 0)]
        heapq.heapify(pq)

        while pq:
            safe, x, y = heapq.heappop(pq)
            safe = -safe

            if x == n - 1 and y == n - 1:
                return safe

            vis[x][y] = True

            for i in range(4):
                new_x: int = x + self.roww[i]
                new_y: int = y + self.coll[i]

                if 0 <= new_x < n and 0 <= new_y < n and not vis[new_x][new_y]:
                    s: float = min(safe, score[new_x][new_y])
                    heapq.heappush(pq, (-s, new_x, new_y))
                    vis[new_x][new_y] = True

        return -1
