class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        cur_ind: int = 0
        n: int = len(s)

        for char in t:
            if char == s[cur_ind]:
                cur_ind += 1
                if cur_ind == n:
                    return True

        return False
