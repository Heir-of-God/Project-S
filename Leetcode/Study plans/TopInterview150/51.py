class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()
        res: int = 1
        prev: list[int] = points[0]

        for balloon_ind in range(1, len(points), 1):
            start: int = points[balloon_ind][0]
            end: int = points[balloon_ind][1]

            if start <= prev[1]:
                prev[0] = start
                prev[1] = min(prev[1], end)
            else:
                prev = [start, end]
                res += 1

        return res
