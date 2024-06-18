class Solution:
    def maxArea(self, height: list[int]) -> int:
        res: int = 0
        n: int = len(height)

        left: int = 0
        right: int = n - 1

        while left < right:
            min_val = min(height[left], height[right])
            res = max(res, min_val * (right - left))
            if min_val == height[left]:
                left += 1
            else:
                right -= 1

        return res
