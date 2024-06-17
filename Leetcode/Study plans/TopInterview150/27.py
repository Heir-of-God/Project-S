class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n: int = len(numbers)
        left: int = 0
        right: int = n - 1

        while True:  # There is always one solution
            cur_sum: int = numbers[left] + numbers[right]
            if cur_sum < target:
                left += 1
            elif cur_sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
