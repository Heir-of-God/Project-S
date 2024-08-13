class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        def binary_search_prev_job(left: int, endtime: int) -> int:
            left: int = left
            right: int = n - 1
            res: int = -1

            while left <= right:
                mid: int = (left + right) // 2
                start_time: int = jobs[mid][0]

                if start_time >= endtime:
                    res = mid
                    right = mid - 1
                else:
                    left = mid + 1

            return res

        n: int = len(profit)
        jobs: list[tuple[int, int, int]] = [(startTime[i], endTime[i], profit[i]) for i in range(n)]
        jobs.sort()

        dp: list[int] = [0 for _ in range(n)]
        dp[-1] = jobs[-1][2]  # if we have only 1 job then maximum we can get - complete it

        for ind in range(n - 2, -1, -1):
            start, end, prof = jobs[ind]

            nxt_job_ind: int = binary_search_prev_job(ind + 1, end)
            dp[ind] = max(dp[ind + 1], (dp[nxt_job_ind] if nxt_job_ind != -1 else 0) + prof)

        return dp[0]
