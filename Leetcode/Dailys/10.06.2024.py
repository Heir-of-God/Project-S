class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        n: int = len(heights)
        expected: list[int] = sorted(heights)
        res: int = 0

        for ind in range(n):
            if heights[ind] != expected[ind]:
                res += 1

        return res
