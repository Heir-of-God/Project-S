class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        res: int = 0
        cur_max_ending: int = 0
        cur_ind: int = 0

        while cur_max_ending < n:
            if cur_ind < len(nums) and nums[cur_ind] <= cur_max_ending + 1:
                cur_max_ending += nums[cur_ind]
                cur_ind += 1
            else:
                cur_max_ending += cur_max_ending + 1
                res += 1

        return res
