class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sm: int = sum(nums)
        if sm & 1 == 1:
            return False
        subset_sum: int = sm // 2

        can_achieve: set[int] = {0}

        for num in nums:
            can_achieve.update([prev_val + num for prev_val in can_achieve if prev_val + num <= subset_sum])

            if subset_sum in can_achieve:
                return True

        return False
