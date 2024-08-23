class Solution:
    def minTimeToType(self, word: str) -> int:
        n: int = len(word)
        res: int = n
        cur: int = ord("a")

        for char in word:
            cur_n: int = ord(char)
            dist_to_char: int = abs(cur - ord(char))
            moves: int = min(dist_to_char, 26 - dist_to_char)
            res += moves
            cur = cur_n

        return res
