class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        if k == 1:
            return nums

        n = len(nums)
        last_not_included = -1
        res = []

        for ind in range(1, n):
            if nums[ind] - nums[ind - 1] != 1:
                last_not_included = ind - 1

            if ind >= k - 1:
                if ind - last_not_included >= k:
                    res.append(nums[ind])
                else:
                    res.append(-1)

        return res
