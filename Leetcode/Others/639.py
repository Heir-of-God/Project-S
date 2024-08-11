class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        prev_prev: int = 1
        prev: int = 1
        prev_char: str = ""

        for char in s:
            cur = 0
            if char == "0" and prev_char == "0":
                return 0

            if char != "0":
                cur += prev * (1 if char != "*" else 9)  # decode this character as single digit

            # based on the previous character group it and current
            if prev_char == "*":
                cur += prev_prev * (15 if char == "*" else 2 if char in "0123456" else 1)
            elif prev_char == "1":
                cur += prev_prev * (9 if char == "*" else 1)
            elif prev_char == "2":
                cur += prev_prev * (6 if char == "*" else 1 if char in "0123456" else 0)

            prev_char = char
            prev_prev, prev = prev, cur % MOD

        return prev
