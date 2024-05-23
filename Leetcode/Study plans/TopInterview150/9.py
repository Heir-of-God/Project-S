class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n: int = len(nums)
        dp: list[bool] = [False for _ in range(n)]
        dp[0] = True

        for ind in range(n):
            if dp[ind] == True:
                steps: int = nums[ind]
                if steps >= n - ind - 1:
                    return True
                for delta_ind in range(1, steps + 1, 1):
                    dp[ind + delta_ind] = True

        return dp[-1]


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        cur_ind: int = 0
        n: int = len(nums)

        while cur_ind < n:
            steps_from_there: int = nums[cur_ind]
            if steps_from_there >= n - cur_ind - 1:
                return True
            nxt_ind = None
            mx_steps = 0
            for delta_ind in range(1, steps_from_there + 1, 1):
                if delta_ind + nums[delta_ind + cur_ind] >= mx_steps:
                    mx_steps: int = delta_ind + nums[delta_ind + cur_ind]
                    nxt_ind: int = delta_ind + cur_ind
            if nxt_ind is None:
                return False
            cur_ind = nxt_ind

        return True


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        gas: int = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1

        return True
