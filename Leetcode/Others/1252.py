class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        rows: list[int] = [0 for _ in range(m)]
        cols: list[int] = [0 for _ in range(n)]

        for row, col in indices:
            rows[row] += 1
            cols[col] += 1

        odd_rows: int = len([1 for row in rows if row & 1 == 1])
        odd_cols: int = len([1 for col in cols if col & 1 == 1])

        return (n - odd_cols) * odd_rows + (m - odd_rows) * odd_cols


class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        rows: list[int] = [0 for _ in range(m)]
        cols: list[int] = [0 for _ in range(n)]
        odd_rows = odd_cols = 0

        for row, col in indices:
            rows[row] = 0 if rows[row] else 1
            cols[col] = 0 if cols[col] else 1
            odd_rows += 1 if rows[row] else -1
            odd_cols += 1 if cols[col] else -1

        return (n - odd_cols) * odd_rows + (m - odd_rows) * odd_cols
