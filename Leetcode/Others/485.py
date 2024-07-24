class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        res: int = 0
        cur_one: int = 0
        nums.append(0)

        for num in nums:
            if num == 1:
                cur_one += 1
            else:
                res = max(res, cur_one)
                cur_one = 0

        return res
