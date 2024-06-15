class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows: list[list[str]] = [[] for _ in range(numRows)]
        cur_row_ind = 0
        cur_step = 1

        for char in s:
            rows[cur_row_ind].append(char)
            cur_row_ind += cur_step
            if cur_row_ind == numRows:
                cur_row_ind = numRows - 2
                cur_step *= -1
            elif cur_row_ind == -1:
                cur_row_ind = 1
                cur_step *= -1
        for ind in range(numRows):
            rows[ind] = "".join(rows[ind])

        return "".join(rows)
