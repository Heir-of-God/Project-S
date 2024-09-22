class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        k -= 1
        cur_number = 1

        def count_numbers(root):
            res = 0
            left_root = root
            right_root = root + 1
            while left_root <= n:
                res += min(n + 1, right_root) - left_root
                left_root *= 10
                right_root *= 10
            return res

        while k > 0:
            numbers_under = count_numbers(cur_number)
            if numbers_under <= k:
                k -= numbers_under
                cur_number += 1  # move to the next root
            else:
                cur_number *= 10  # move down the root
                k -= 1

        return cur_number
