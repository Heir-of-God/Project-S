class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        worker.sort()
        jobs: list[tuple[int, int]] = sorted(list(zip(difficulty, profit)))
        cur_job_ind: int = 0
        cur_max_profit: int = 0
        res: int = 0

        for w in worker:
            while cur_job_ind != len(jobs) and w >= jobs[cur_job_ind][0]:
                cur_max_profit = max(cur_max_profit, jobs[cur_job_ind][1])
                cur_job_ind += 1
            res += cur_max_profit

        return res
