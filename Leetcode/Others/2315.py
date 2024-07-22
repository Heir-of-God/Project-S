class Solution:
    def countAsterisks(self, s: str) -> int:
        pipe_even: bool = True
        res: int = 0

        for char in s:
            if char == "*" and pipe_even:
                res += 1
            elif char == "|":
                pipe_even = not pipe_even

        return res
