class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        res = list(s)
        cur_shifts: int = sum(shifts)
        ind = 0

        while cur_shifts > 0:
            res[ind] = chr(((ord(res[ind]) - ord("a") + cur_shifts) % 26) + ord("a"))
            cur_shifts -= shifts[ind]
            ind += 1

        return "".join(res)
