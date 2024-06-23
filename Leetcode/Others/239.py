class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n: int = len(nums)
        deque: list[tuple[int, int]] = []
        res: list[int] = []

        for ind in range(n):
            num: int = nums[ind]
            while deque and deque[-1][1] <= num:
                deque.pop()
            deque.append((ind, num))
            while deque[0][0] < ind - k + 1:
                deque.pop(0)

            if ind >= k - 1:
                res.append(deque[0][1])

        return res
