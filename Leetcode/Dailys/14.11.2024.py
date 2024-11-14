class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        def check(val) -> bool:
            res = 0
            for q in quantities:
                res += (q + val - 1) // val
                if res > n:
                    return False
            return True

        high: int = max(quantities)
        low: int = 1

        while low < high:
            mid: int = low + (high - low) // 2

            if check(mid):
                high = mid
            else:
                low = mid + 1

        return low
