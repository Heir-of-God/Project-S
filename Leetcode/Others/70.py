class Solution:
    def climbStairs(self, n: int) -> int:
        prev_prev: int = 0
        prev: int = 1

        for _ in range(n):
            prev_prev, prev = prev, prev_prev + prev

        return prev
