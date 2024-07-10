class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if not intervals:
            return [newInterval]
        res: list[list[int]] = []
        appended_new: bool = False

        for interval in intervals:
            if appended_new or interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] <= newInterval[1]:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            else:
                res.append(newInterval)
                res.append(interval)
                appended_new = True
        if not appended_new:
            res.append(newInterval)

        return res
