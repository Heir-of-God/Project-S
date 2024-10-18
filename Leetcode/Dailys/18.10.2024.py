class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        n: int = len(nums)
        max_or: int = 0
        for num in nums:
            max_or |= num

        def recursion(cur_ind, cur_or):
            if cur_ind == n:
                return cur_or == max_or

            not_include = recursion(cur_ind + 1, cur_or)
            include = recursion(cur_ind + 1, cur_or | nums[cur_ind])

            return not_include + include

        return recursion(0, 0)
