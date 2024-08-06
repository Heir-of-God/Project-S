class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        n: int = len(pairs)
        pairs.sort(key=lambda el: el[1])
        dp: list[int] = [0 for _ in range(n)]
        dp[0] = 1

        for ind in range(1, n, 1):
            cur_start: int = pairs[ind][0]

            for prev_ind in range(0, ind, 1):
                prev_end: int = pairs[prev_ind][1]
                if prev_end < cur_start:
                    dp[ind] = max(dp[ind], dp[prev_ind] + 1)

        return max(dp)


class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        n: int = len(pairs)
        pairs.sort(key=lambda el: el[1])
        last_end = -1001
        res = 0

        for ind in range(n):
            cur_start: int = pairs[ind][0]

            if cur_start > last_end:
                res += 1
                last_end = pairs[ind][1]

        return res
