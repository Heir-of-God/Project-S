class Solution:
    def minimumSteps(self, s: str) -> int:
        n: int = len(s)
        left: int = 0
        right: int = n - 1

        res = 0
        while left < right:
            if s[left] == "1":
                while left < right and s[right] != "0":
                    right -= 1
                res += right - left
                right -= 1

            left += 1

        return res
