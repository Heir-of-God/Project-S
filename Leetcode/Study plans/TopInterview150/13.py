class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n: int = len(nums)
        product_prefix: list[int] = nums[:]
        for ind in range(1, n, 1):
            product_prefix[ind] = product_prefix[ind - 1] * nums[ind]
        product_suffix: list[int] = nums[:]
        for ind in range(n - 2, -1, -1):
            product_suffix[ind] = product_suffix[ind + 1] * nums[ind]

        res: list[int] = [1 for _ in range(n)]
        res[0] = product_suffix[1]
        res[-1] = product_prefix[-2]
        for ind in range(1, n - 1, 1):
            res[ind] = product_prefix[ind - 1] * product_suffix[ind + 1]
        return res


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n: int = len(nums)
        res: list[int] = [1 for _ in range(n)]
        cur_prefix = 1
        for ind in range(n):
            res[ind] *= cur_prefix
            cur_prefix *= nums[ind]

        cur_sufix = 1
        for ind in range(n - 1, -1, -1):
            res[ind] *= cur_sufix
            cur_sufix *= nums[ind]

        return res
