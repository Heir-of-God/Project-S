class Solution:

    def maximumTotalCost(self, nums: list[int]) -> int:
        n: int = len(nums)
        dp: list[list[int]] = [[-1 for _ in range(2)] for _ in range(n)]

        def calculate_maximum_cost(cur_ind: int, changed_sign: int) -> int:
            if cur_ind < 0:  # if we reached impossible state
                return 0
            if cur_ind == 0:
                if changed_sign == 0:
                    return nums[0]
                else:
                    return -float("inf")
            if dp[cur_ind][changed_sign] != -1:
                return dp[cur_ind][changed_sign]

            if changed_sign == 0:
                max_cost = nums[cur_ind] + calculate_maximum_cost(cur_ind - 1, 0)
                max_cost = max(max_cost, nums[cur_ind] + calculate_maximum_cost(cur_ind - 1, 1))
            else:
                max_cost = -nums[cur_ind] + calculate_maximum_cost(cur_ind - 1, 0)

            dp[cur_ind][changed_sign] = max_cost
            return max_cost

        return max(
            calculate_maximum_cost(n - 1, 0),
            calculate_maximum_cost(n - 1, 1),
        )
