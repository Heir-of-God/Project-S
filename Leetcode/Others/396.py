class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        last_ind: int = len(nums) - 1
        current_state_sum: int = 0
        all_numbers_sum: int = 0

        for ind, num in enumerate(nums):
            current_state_sum += num * ind
            all_numbers_sum += num

        res: int = current_state_sum
        for ind in range(last_ind, -1, -1):
            current_state_sum -= nums[ind] * last_ind
            current_state_sum += all_numbers_sum - nums[ind]
            if current_state_sum > res:
                res = current_state_sum

        return res
