class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        n: int = len(nums)
        included: set[int] = set()
        cur_sm: int = 0
        res: int = 0
        left: int = 0

        for right in range(n):
            cur_sm += nums[right]

            while right - left + 1 > k or nums[right] in included:
                included.remove(nums[left])
                cur_sm -= nums[left]
                left += 1

            included.add(nums[right])
            if cur_sm > res and right - left + 1 == k:
                res = max(res, cur_sm)

        return res
