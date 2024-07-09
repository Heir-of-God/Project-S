class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        n: int = len(intervals)
        res: list[list[int]] = [intervals[0]]

        for interval_ind in range(1, n, 1):
            prev_int: list[int] = res[-1]
            cur_int: list[int] = intervals[interval_ind]

            if prev_int[1] >= cur_int[0]:
                if not cur_int[1] <= prev_int[1]:
                    res[-1][1] = cur_int[1]
            else:
                res.append(cur_int)

        return res
