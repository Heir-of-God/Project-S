class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res: int = 0
        while start or goal:
            bit_start: int = start & 1
            bit_goal: int = goal & 1
            start >>= 1
            goal >>= 1
            res += bit_start != bit_goal

        return res
