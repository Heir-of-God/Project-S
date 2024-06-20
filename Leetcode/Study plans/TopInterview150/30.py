from math import isinf


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n: int = len(nums)
        cur_sum: int = 0
        res: int = float("inf")
        left: int = 0

        for right in range(n):
            cur_sum += nums[right]
            while cur_sum - nums[left] >= target:
                cur_sum -= nums[left]
                left += 1
            if cur_sum >= target:
                res = min(res, right - left + 1)

        return res if not isinf(res) else 0


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n: int = len(nums)
        prefix_sum: list[int] = nums[:]
        for ind in range(1, n):
            prefix_sum[ind] += prefix_sum[ind - 1]

        res = 0
        for first_ind in range(n):
            here: int = prefix_sum[first_ind]
            left: int = first_ind
            right: int = n - 1

            cur_r: int = -1
            while left <= right:
                mid: int = (left + right) // 2
                cur_sum: int = prefix_sum[mid] - here + nums[first_ind]
                if cur_sum < target:
                    left = mid + 1
                else:
                    cur_r = mid
                    right = mid - 1
            if cur_r == -1:
                return res
            if res == 0 or cur_r - first_ind + 1 < res:
                res = cur_r - first_ind + 1

        return res
