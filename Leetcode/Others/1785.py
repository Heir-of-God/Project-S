class Solution:
    def minElements(self, nums: list[int], limit: int, goal: int) -> int:
        sm: int = sum(nums)
        need_to_add: int = abs(goal - sm)
        res: int = need_to_add // limit + (need_to_add % limit != 0)
        return res
