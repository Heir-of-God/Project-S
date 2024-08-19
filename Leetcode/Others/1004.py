class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        res: int = 0
        start_ind: int = 0
        cur_flipped: int = 0

        for ind, num in enumerate(nums):
            if num == 0:
                if cur_flipped != k:
                    cur_flipped += 1
                else:
                    res = max(res, ind - start_ind)
                    while nums[start_ind] != 0:
                        start_ind += 1
                    start_ind += 1
        res = max(res, ind - start_ind + 1)

        return res


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        res = 0
        flipped = 0
        left = 0

        for ind, num in enumerate(nums):
            if num == 0:
                flipped += 1
                if flipped > k:
                    res = max(res, ind - left)
                    flipped -= 1
                    while nums[left] != 0:
                        left += 1
                    left += 1
        res = max(res, len(nums) - left)
        return res
