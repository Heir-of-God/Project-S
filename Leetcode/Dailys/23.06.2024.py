from collections import deque


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        n: int = len(nums)
        min_deque: list[tuple[int, int]] = deque()
        max_deque: list[tuple[int, int]] = deque()
        res: int = 0
        left: int = 0

        for ind in range(n):
            num: int = nums[ind]

            while min_deque and num < min_deque[-1][1]:
                min_deque.pop()
            while max_deque and num > max_deque[-1][1]:
                max_deque.pop()
            min_deque.append((ind, num))
            max_deque.append((ind, num))

            while min_deque and max_deque and max_deque[0][1] - min_deque[0][1] > limit:
                mn_ind: int = min(min_deque[0][0], max_deque[0][0])
                left = mn_ind + 1
                while min_deque and min_deque[0][0] < left:
                    min_deque.popleft()
                while max_deque and max_deque[0][0] < left:
                    max_deque.popleft()

            res = max(res, ind - left + 1)

        return res
