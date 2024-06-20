class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n: int = len(nums)
        nums.sort()
        res: list[list[int]] = []

        for first_ind in range(n):
            if first_ind != 0 and nums[first_ind] == nums[first_ind - 1]:
                continue
            target: int = -nums[first_ind]
            left_ind: int = first_ind + 1
            right_ind: int = n - 1

            while left_ind < right_ind:
                cur_sum: int = nums[left_ind] + nums[right_ind]
                if cur_sum < target:
                    left_ind += 1
                elif cur_sum > target:
                    right_ind -= 1
                else:
                    res.append([nums[first_ind], nums[left_ind], nums[right_ind]])
                    left_ind += 1
                    right_ind -= 1
                    while left_ind != n - 1 and nums[left_ind] == nums[left_ind - 1]:
                        left_ind += 1
                    while right_ind != 0 and nums[right_ind] == nums[right_ind + 1]:
                        right_ind -= 1

        return res
