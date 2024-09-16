class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        times: list[int] = []
        for timepoint in timePoints:
            hour = int(timepoint.split(":")[0])
            minutes = int(timepoint.split(":")[1])
            times.append(hour * 60 + minutes)

        times.sort()
        res: int = min(times[-1] - times[0], times[0] + (24 * 60 - times[-1]))
        for ind in range(1, len(times), 1):
            res = min(res, min(times[ind] - times[ind - 1], times[ind - 1] + (24 * 60 - times[ind])))

        return res


class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        times: list[bool] = [False for _ in range(24 * 60)]
        for timepoint in timePoints:
            hour = int(timepoint.split(":")[0])
            minutes = int(timepoint.split(":")[1])
            time: int = (hour * 60 + minutes) % (24 * 60)
            if not times[time]:
                times[time] = True
            else:
                return 0

        first = -1
        last = -1
        res: int = float("inf")
        for time, presented in enumerate(times):
            if presented:
                if first == -1:
                    first = time
                if last != -1:
                    res = min(res, time - last)
                last = time

        return min(res, first + (24 * 60 - last))
