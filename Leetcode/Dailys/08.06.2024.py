class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        n: int = len(nums)
        nums[0] %= k
        for ind in range(1, n, 1):
            nums[ind] = (nums[ind] + nums[ind - 1]) % k

        seen: dict[int, int] = {0: -1}  # number remainder % k -> first index we've met it
        for ind, num in enumerate(nums):
            if num in seen and ind - seen[num] >= 2:
                return True
            if not num in seen:
                seen[num] = ind

        return False
