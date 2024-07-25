class Solution:
    def semiOrderedPermutation(self, nums: list[int]) -> int:
        n: int = len(nums)
        for ind, num in enumerate(nums):
            if num == 1:
                one_ind: int = ind
            elif num == n:
                n_ind: int = ind

        return one_ind + (n - n_ind - 1) - (1 if one_ind > n_ind else 0)
