class Solution:
    def numDecodings(self, s: str) -> int:
        n: int = len(s)
        prev_char: str = "_"
        dp: list[int] = [0 for _ in range(n + 1)]  # dp[i] number of ways to decode first i characters of string s
        dp[0] = 1  # you have 1 way to decode empty string

        for number_of_chars in range(1, n + 1, 1):
            cur_char: str = s[number_of_chars - 1]

            if cur_char == "0":
                if prev_char not in "12":
                    return 0
            else:
                dp[number_of_chars] = dp[number_of_chars - 1]

            if prev_char == "1" or (prev_char == "2" and cur_char not in "789"):
                dp[number_of_chars] += dp[number_of_chars - 2]
            prev_char = cur_char

        return dp[n]
