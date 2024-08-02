class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        num_of_1: int = nums.count(1)
        nums += nums[:num_of_1]  # make array bigger so when we traverse it it's like circular
        res: int = float("inf")
        cur_zeros = 0

        for ind in range(len(nums)):
            if ind >= num_of_1:
                res = min(res, cur_zeros)
                if nums[ind - num_of_1] == 0:
                    cur_zeros -= 1
            if nums[ind] == 0:
                cur_zeros += 1

        return res
