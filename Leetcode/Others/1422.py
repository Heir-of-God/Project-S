class Solution:
    def maxScore(self, s: str) -> int:
        cur_zeros: int = 0
        cur_ones: int = s.count("1")
        res: int = 0

        for ind in range(0, len(s) - 1, 1):
            el: str = s[ind]
            if el == "0":
                cur_zeros += 1
            elif el == "1":
                cur_ones -= 1

            local_score: int = cur_zeros + cur_ones
            res = max(res, local_score)

        return res
