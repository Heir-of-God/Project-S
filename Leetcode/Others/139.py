class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n: int = len(s)
        words = set(wordDict)
        memo: list[int | bool] = [-1 for _ in range(n)]

        def recursion(cur_ind):
            if cur_ind == n:
                return True
            if memo[cur_ind] != -1:
                return memo[cur_ind]

            res = False
            for end_ind in range(cur_ind, min(n, cur_ind + 20), 1):
                if s[cur_ind : end_ind + 1] in words:
                    res = res or recursion(end_ind + 1)
            memo[cur_ind] = res
            return res

        return recursion(0)


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n: int = len(s)
        words = set(wordDict)
        dp: list[bool] = [False for _ in range(n + 1)]
        dp[0] = True

        for end_ind in range(n):
            for start_word_ind in range(end_ind, max(-1, end_ind - 20), -1):
                if dp[start_word_ind] and s[start_word_ind : end_ind + 1] in words:
                    dp[end_ind + 1] = True
                    break
        return dp[n]
