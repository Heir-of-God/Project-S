class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        def get_number_of_bouquets(day) -> int:
            res: int = 0
            cur_in_row: int = 0

            for flower in bloomDay:
                if flower <= day:
                    cur_in_row += 1
                else:
                    cur_in_row = 0

                if cur_in_row == k:
                    res += 1
                    cur_in_row = 0

            return res

        n: int = len(bloomDay)
        if n < m * k:
            return -1
        left: int = min(bloomDay)
        right: int = max(bloomDay)
        res: int = -1

        while left <= right:
            mid: int = (left + right) // 2
            if get_number_of_bouquets(mid) >= m:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res
