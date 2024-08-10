class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        res: int = 0
        dp: dict[int, int] = {}  # el -> max length of subseq ending on this el

        for el in arr:
            prev_el: int = el - difference
            length: int = dp.get(prev_el, 0) + 1
            dp[el] = length
            if length > res:
                res = length

        return res
