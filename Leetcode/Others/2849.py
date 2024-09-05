class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        return max(abs(sx - fx), abs(sy - fy)) <= t and (sx != fx or sy != fy or t != 1)
