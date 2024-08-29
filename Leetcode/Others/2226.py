class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        def can_get_piles(candies_in_pile) -> bool:
            count = 0
            for pile in candies:
                count += pile // candies_in_pile
                if count >= k:
                    return True
            return False

        left: int = 1
        right: int = min(max(candies), sum(candies) // k)
        res: int = 0

        while left <= right:
            mid: int = (left + right) // 2
            possible: bool = can_get_piles(mid)
            if possible:
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res
