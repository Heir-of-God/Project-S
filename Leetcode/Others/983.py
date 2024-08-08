# Giving TLE
class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        n: int = len(days)
        res: int = float("inf")

        def recursion(cur_ind, cur_res, delta) -> None:
            nonlocal res
            if cur_ind == n:
                res = min(res, cur_res)
                return

            prev_day = days[cur_ind - 1] if cur_ind != 0 else -float("inf")
            if days[cur_ind] - prev_day >= delta:
                recursion(cur_ind + 1, cur_res + costs[0], 1)
                recursion(cur_ind + 1, cur_res + costs[1], 7)
                recursion(cur_ind + 1, cur_res + costs[2], 30)
            else:
                recursion(cur_ind + 1, cur_res, delta - (days[cur_ind] - prev_day))

        recursion(0, 0, 0)
        return res


class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        dp: list[int] = [0 for _ in range(days[-1] + 1)]
        days_set = set(days)

        for day in range(1, days[-1] + 1, 1):
            if day not in days_set:
                dp[day] = dp[day - 1]
                continue

            one_day: int = dp[day - 1] + costs[0]
            one_week: int = dp[max(0, day - 7)] + costs[1]
            one_month: int = dp[max(0, day - 30)] + costs[2]
            dp[day] = min(one_day, one_week, one_month)

        return dp[-1]
