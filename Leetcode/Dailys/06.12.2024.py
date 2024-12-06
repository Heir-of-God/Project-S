class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        res = 0
        s = 0
        cur_num = 1

        while cur_num <= n and s + cur_num <= maxSum:
            if cur_num not in banned:
                s += cur_num
                res += 1
            cur_num += 1

        return res
