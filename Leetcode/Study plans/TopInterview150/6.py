class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n: int = len(nums)
        k %= n

        nums.reverse()
        for ind in range(k // 2):
            nums[ind], nums[k - ind - 1] = nums[k - ind - 1], nums[ind]

        for ind in range(k, (n + k) // 2, 1):
            nums[ind], nums[n - ind - 1 + k] = nums[n - ind - 1 + k], nums[ind]
