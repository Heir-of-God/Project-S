from collections import deque
from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target: str = "123450"
        initial: str = "".join(str(num) for row in board for num in row)

        neighbors: dict[int, list[int]] = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4], 4: [1, 3, 5], 5: [2, 4]}

        q: list[list[str, int]] = deque([(initial, 0)])
        visited: set[str] = set([initial])

        while q:
            state, moves = q.popleft()

            if state == target:
                return moves
            zero_pos = state.index("0")

            for neighbor in neighbors[zero_pos]:
                new = list(state)
                new[zero_pos], new[neighbor] = new[neighbor], new[zero_pos]
                new = "".join(new)

                if new not in visited:
                    visited.add(new)
                    q.append((new, moves + 1))

        return -1
