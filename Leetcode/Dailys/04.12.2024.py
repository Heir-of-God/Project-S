class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        cur: int = 0  # ind in str2

        for char in str1:
            nxt: str = chr(ord(char) + 1) if char != "z" else "a"
            if char == str2[cur] or nxt == str2[cur]:
                cur += 1
            if cur == len(str2):
                return True

        return False
