class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        rows: int = len(points)
        cols: int = len(points[0])

        for row_ind in range(1, rows):
            prev_left = 0
            prev_right = 0
            elems: list[int] = points[row_ind][:]

            for col_ind in range(cols):
                prev_left: int = max(prev_left - 1, points[row_ind - 1][col_ind])
                points[row_ind][col_ind] = prev_left + elems[col_ind]

            for col_ind in range(cols - 1, -1, -1):
                prev_right: int = max(prev_right - 1, points[row_ind - 1][col_ind])
                points[row_ind][col_ind] = max(points[row_ind][col_ind], prev_right + elems[col_ind])

        return max(points[-1])
