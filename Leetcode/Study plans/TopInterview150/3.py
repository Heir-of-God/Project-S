# 26. Remove Duplicates from Sorted Array


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        write_ind = 0

        for num in nums:
            if write_ind == 0 or nums[write_ind - 1] != num:
                nums[write_ind] = num
                write_ind += 1

        return write_ind
