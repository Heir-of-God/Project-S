class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n: int = len(nums)
        count: list[int] = [0, 0, 0]
        for num in nums:
            count[num] += 1

        cur_ind: int = 0
        cur_pick: int = 0
        while cur_ind != n:
            while count[cur_pick] == 0 and cur_pick < 3:
                cur_pick += 1
            nums[cur_ind] = cur_pick
            count[cur_pick] -= 1
            cur_ind += 1


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n: int = len(nums)
        left_ind: int = 0
        cur_ind: int = 0
        right_ind: int = n - 1

        while cur_ind <= right_ind:
            if nums[cur_ind] == 0:
                nums[cur_ind], nums[left_ind] = nums[left_ind], nums[cur_ind]
                cur_ind += 1
                left_ind += 1
            elif nums[cur_ind] == 1:
                cur_ind += 1
            elif nums[cur_ind] == 2:
                nums[cur_ind], nums[right_ind] = nums[right_ind], nums[cur_ind]
                right_ind -= 1
