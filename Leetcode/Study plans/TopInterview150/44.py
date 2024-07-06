class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indexes: dict[int, int] = {}

        for ind, num in enumerate(nums):
            num2: int = target - num
            if num2 in indexes:
                return [indexes[num2], ind]
            indexes[num] = ind

        return
