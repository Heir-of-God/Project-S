class Solution:
    def minimumDeletions(self, s: str) -> int:
        res: int = float("inf")
        b_before: int = 0
        a_after: int = s.count("a")
        s += "#"

        for char in s:
            res = min(res, a_after + b_before)
            if char == "b":
                b_before += 1
            else:
                a_after -= 1

        return res
