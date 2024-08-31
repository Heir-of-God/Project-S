class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        MOD = 10**9 + 7
        n: int = len(nums)
        nums.sort()
        left: int = 0
        right: int = n - 1
        res: int = 0
        pre: list[int] = [1]
        for _ in range(1, n + 1, 1):
            pre.append((pre[-1] << 1) % MOD)

        while left <= right:
            while left <= right and nums[left] + nums[right] > target:
                right -= 1
            if left <= right:
                res += pre[right - left]
            left += 1

        return res % MOD
