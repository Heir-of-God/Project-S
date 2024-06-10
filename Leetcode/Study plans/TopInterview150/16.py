class Solution:
    def trap(self, height: list[int]) -> int:
        n: int = len(height)
        res: int = 0

        right_biggest: list[int] = [0 for _ in range(n)]
        for ind in range(n - 2, -1, -1):
            right_biggest[ind] = max(right_biggest[ind + 1], height[ind + 1])

        cur_max_left: int = 0
        for ind, h in enumerate(height):
            here: int = min(cur_max_left, right_biggest[ind]) - h
            if here > 0:
                res += here
            cur_max_left = max(cur_max_left, h)

        return res
