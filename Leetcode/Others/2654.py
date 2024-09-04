class Solution:
    def minOperations(self, nums: list[int]) -> int:
        def gcd(x: int, y: int) -> int:
            while y != 0:
                x, y = y, x % y
            return x

        n: int = len(nums)
        ones_in_arr: int = nums.count(1)
        if ones_in_arr:
            return n - ones_in_arr

        for steps in range(n):
            for i in range(n - steps - 1):
                new: int = gcd(nums[i], nums[i + 1])
                if new == 1:
                    return steps + n
                nums[i] = new

        return -1
