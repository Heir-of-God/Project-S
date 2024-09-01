class Solution:
    def stringHash(self, s: str, k: int) -> str:
        n = len(s)
        substrings = [s[i : i + k] for i in range(0, n, k)]
        res = ""

        for substring in substrings:
            sm = 0
            for char in substring:
                sm += ord(char) - ord("a")
            sm %= 26
            res += chr(sm + ord("a"))

        return res
