class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        s += "_"
        n: int = len(s)
        res: list[list[int]] = []
        cur_group_start: int = 0

        for ind in range(1, n):
            cur_char = s[ind]
            if cur_char != s[ind - 1]:
                if ind - cur_group_start >= 3:
                    res.append([cur_group_start, ind - 1])
                cur_group_start = ind

        return res
