class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        n: int = len(nums)
        if n == 0:
            return 0

        dp: list[list[int]] = [[0] * (k + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1

        result: int = 1
        for cur_ind in range(1, n):
            for changes in range(k + 1):
                dp[cur_ind][changes] = 1
                for last_ind in range(cur_ind):
                    if nums[last_ind] == nums[cur_ind]:
                        dp[cur_ind][changes] = max(dp[cur_ind][changes], dp[last_ind][changes] + 1)
                    elif changes > 0:
                        dp[cur_ind][changes] = max(dp[cur_ind][changes], dp[last_ind][changes - 1] + 1)
                result = max(result, dp[cur_ind][changes])

        return result


s = Solution()
print(s.maximumLength([1, 2, 3, 4, 5, 1], 0))
