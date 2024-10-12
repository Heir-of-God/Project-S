class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        intersections: list[int] = [0 for _ in range(10**6 + 2)]
        check_start: int = float("inf")
        check_end: int = -float("inf")

        for start, end in intervals:
            intersections[start] += 1
            check_start = min(check_start, start)
            intersections[end + 1] -= 1
            check_end = max(check_end, end)

        res = 1
        cur_intervals = 0
        for ind in range(check_start, check_end + 1):
            cur_intervals += intersections[ind]
            res: int = max(res, cur_intervals)

        return res


class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        events: list[list[int, int]] = []
        for start, end in intervals:
            events.append([start, 1])
            events.append([end + 1, -1])
        events.sort()
        ind = 0
        cur = 0
        res = 1

        while ind != len(events):
            cur += events[ind][1]
            ind += 1
            while ind != len(events) and events[ind - 1][0] == events[ind][0]:
                cur += events[ind][1]
                ind += 1
            res = max(res, cur)

        return res
