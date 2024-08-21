class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        def is_possible(speed) -> bool:
            res = 0
            for ind, distance in enumerate(dist):
                res += ((distance + speed - 1) // speed) if ind != n - 1 else distance / speed

            return res <= hour

        n: int = len(dist)
        left: int = 1
        right: int = 10**7
        res: int = -1

        while left <= right:
            mid = (left + right) // 2
            ans: bool = is_possible(mid)
            if ans:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res
