from collections import defaultdict


class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        visited_points = set()
        cols_by_row = defaultdict(list)
        rows_by_col = defaultdict(list)

        stones = [tuple(i) for i in stones]
        for row, col in stones:
            cols_by_row[row].append(col)
            rows_by_col[col].append(row)

        res = 0
        for stone in stones:
            if stone not in visited_points:
                visited_points.add(stone)
                queue: list[list[int]] = [stone]
                res -= 1
                while queue:
                    row, col = queue.pop()
                    res += 1

                    for new_col in cols_by_row[row]:
                        if (row, new_col) not in visited_points:
                            visited_points.add((row, new_col))
                            queue.append((row, new_col))

                    for new_row in rows_by_col[col]:
                        if (new_row, col) not in visited_points:
                            visited_points.add((new_row, col))
                            queue.append((new_row, col))

        return res
