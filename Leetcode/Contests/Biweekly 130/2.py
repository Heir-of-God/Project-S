class Solution:
    def maxPointsInsideSquare(self, points: list[list[int]], s: str) -> int:
        n: int = len(points)
        for ind in range(n):
            points[ind][0] = abs(points[ind][0])
            points[ind][1] = abs(points[ind][1])

        low: int = 0
        high: int = 10**9
        res = 0

        while low <= high:
            mid: int = (low + high) // 2
            tags: dict[str, int] = {}

            for ind in range(n):
                if points[ind][0] <= mid and points[ind][1] <= mid:
                    c: str = s[ind]
                    tags[c] = tags.get(c, 0) + 1

            norm_state: bool = all(val <= 1 for val in tags.values())

            if norm_state:
                res: int = mid
                low = mid + 1
            else:
                high = mid - 1

        count: int = sum(1 for point in points if point[0] <= res and point[1] <= res)

        return count
