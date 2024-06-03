class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        cur_ind: int = 0
        n: int = len(t)
        for char in s:
            if char == t[cur_ind]:
                cur_ind += 1
                if cur_ind == n:
                    return 0
        return n - cur_ind
