class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        write_ind: int = 0
        cur_num: int = None
        cur_count: int = 0

        for num in nums:
            if num != cur_num:
                cur_count = 1
                cur_num = num
            else:
                cur_count += 1

            if cur_count <= 2:
                nums[write_ind] = cur_num
                write_ind += 1

        return write_ind
