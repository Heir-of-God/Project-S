# 27. Remove Element


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        write_ind = 0
        for num in nums:
            if num != val:
                nums[write_ind] = num
                write_ind += 1

        return write_ind
