from heapq import heappop, heappush


class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        times = [(t[0], t[1], i) for i, t in enumerate(times)]
        times.sort()
        n: int = len(times)
        free_chairs: list[int] = [i for i in range(n)]
        when_free: list[list[int, int]] = []

        for arrive, leave, friend in times:
            while when_free and when_free[0][0] <= arrive:
                _, chair = heappop(when_free)
                heappush(free_chairs, chair)

            if friend == targetFriend:
                return heappop(free_chairs)
            heappush(when_free, [leave, heappop(free_chairs)])

        return -1
