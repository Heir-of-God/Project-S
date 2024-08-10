class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        s = 0
        min1r1 = float("inf")
        min2r1 = float("inf")
        min1r2 = float("inf")
        min2r2 = float("inf")

        for n in nums:
            s += n
            if n % 3 == 1:
                if n < min1r1:
                    min2r1, min1r1 = min1r1, n
                elif n < min2r1:
                    min2r1 = n
            if n % 3 == 2:
                if n < min1r2:
                    min2r2, min1r2 = min1r2, n
                elif n < min2r2:
                    min2r2 = n

        if s % 3 == 0:
            return s
        elif s % 3 == 1:
            return max(s - min1r2 - min2r2, s - min1r1)
        else:
            return max(s - min1r1 - min2r1, s - min1r2)


class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        dp: list[int] = [0, 0, 0]
        for num in nums:
            for prev_sum in dp[:]:
                dp[(prev_sum + num) % 3] = max(dp[(prev_sum + num) % 3], prev_sum + num)
        return dp[0]
