class Solution:
    def maxSum(self, nums: list[int]) -> int:
        def get_max_digit(num) -> int:
            res = 0
            while num > 0:
                res = max(res, num % 10)
                if res == 9:
                    return res
                num //= 10

            return res

        maximums: list[list[int | None]] = [[None, None] for _ in range(10)]
        for num in nums:
            mx_dig: int = get_max_digit(num)
            if not maximums[mx_dig][0] or maximums[mx_dig][0] < num:
                maximums[mx_dig][1] = maximums[mx_dig][0]
                maximums[mx_dig][0] = num
            elif not maximums[mx_dig][1] or maximums[mx_dig][1] < num:
                maximums[mx_dig][1] = num

        res: int = -1
        for max1, max2 in maximums:
            if max1 and max2:
                res = max(res, max1 + max2)

        return res
