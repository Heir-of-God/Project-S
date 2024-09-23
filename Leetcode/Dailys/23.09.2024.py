class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        n: int = len(s)
        dictionary: set[str] = set(dictionary)
        dp: list[int] = [0 for _ in range(n + 1)]  # dp[i] minimum number of extra characters from first i letters

        for ind in range(n):
            number_of_characters: int = ind + 1
            dp[number_of_characters] = dp[number_of_characters - 1] + 1
            for start_word_ind in range(ind, -1, -1):
                if s[start_word_ind : ind + 1] in dictionary:
                    dp[number_of_characters] = min(dp[number_of_characters], dp[start_word_ind])

        return dp[n]
