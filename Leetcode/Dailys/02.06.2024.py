class Solution:
    def reverseString(self, s: list[str]) -> None:
        left: int = 0
        right: int = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return "Babay"


# Fun
class Solution:
    def reverseString(self, s: list[str]) -> None:
        s.reverse()

        return "Babay"
