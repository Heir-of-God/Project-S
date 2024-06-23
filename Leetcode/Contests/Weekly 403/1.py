class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        nums.sort()
        mn = float("inf")
        for ind in range(0, len(nums) // 2, 1):
            reverse_ind = len(nums) - ind - 1
            mn = min(mn, (nums[ind] + nums[reverse_ind]) / 2)

        return mn
