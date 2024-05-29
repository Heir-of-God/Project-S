class Solution:
    def jump(self, nums: list[int]) -> int:
        n: int = len(nums)
        dp: list[int] = [-1 for _ in range(n)]
        dp[0] = 0

        for ind in range(n):
            for index_to_jump in range(ind + 1, min(ind + nums[ind] + 1, n), 1):
                cur_val: int = dp[index_to_jump]
                if cur_val == -1:
                    dp[index_to_jump] = dp[ind] + 1
                else:
                    dp[index_to_jump] = min(dp[ind] + 1, dp[index_to_jump])

        return dp[-1]


class Solution:
    def jump(self, nums: list[int]) -> int:
        n: int = len(nums)
        if n == 1:
            return 0
        res: int = 0
        cur_ind: int = 0

        while True:
            res += 1
            if cur_ind + nums[cur_ind] >= n - 1:
                return res
            next_ind: int = 0
            cur_max: int = 0
            for option_ind in range(cur_ind + 1, min(cur_ind + nums[cur_ind] + 1, n), 1):
                if nums[option_ind] != 0 and option_ind - cur_ind + nums[option_ind] >= cur_max:
                    cur_max = option_ind - cur_ind + nums[option_ind]
                    next_ind = option_ind
            cur_ind = next_ind
