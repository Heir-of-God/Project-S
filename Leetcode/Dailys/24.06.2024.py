from collections import deque


class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        n: int = len(nums)
        res: int = 0
        left: int = 0
        flipped_indexes: deque[int] = deque()

        while left < n:
            while flipped_indexes and flipped_indexes[0] < left - k + 1:
                flipped_indexes.popleft()
            flipped_times: int = len(flipped_indexes)
            cur_bit: int = nums[left] if flipped_times & 1 == 0 else int(not nums[left])
            if cur_bit == 0:
                if left < n - k + 1:
                    res += 1
                    flipped_indexes.append(left)
                else:
                    return -1
            left += 1

        return res
