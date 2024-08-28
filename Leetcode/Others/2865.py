class Solution:
    def maximumSumOfHeights(self, heights: list[int]) -> int:
        s: int = sum(heights)
        n: int = len(heights)
        res = 0

        for peak_ind in range(n):
            local_res = 0
            prev: int = heights[peak_ind]
            for left in range(peak_ind - 1, -1, -1):
                if heights[left] > prev:
                    local_res += heights[left] - prev
                else:
                    prev = heights[left]

            prev = heights[peak_ind]
            for right in range(peak_ind + 1, n, 1):
                if heights[right] > prev:
                    local_res += heights[right] - prev
                else:
                    prev = heights[right]

            res: int = max(res, s - local_res)

        return res
