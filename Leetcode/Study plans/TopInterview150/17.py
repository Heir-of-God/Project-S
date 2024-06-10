class Solution:
    def romanToInt(self, s: str) -> int:
        values: dict[str, int] = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n: int = len(s)
        res: int = 0
        nxt_val: int = values[s[0]]

        for ind in range(n):
            cur_val = nxt_val
            if ind != n - 1:
                nxt_val = values[s[ind + 1]]
            if cur_val < nxt_val:
                cur_val *= -1
            res += cur_val

        return res
