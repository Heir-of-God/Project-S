class Solution:
    def longestPalindrome(self, s: str) -> str:
        def get_mx(left, right) -> tuple[int, int]:
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return (left, right)

        n: int = len(s)
        mx: int = 1
        res: str = s[0]

        for ind in range(1, n, 1):
            one_left, one_right = get_mx(ind - 1, ind + 1)
            if one_right - one_left - 1 > mx:
                mx = one_right - one_left - 1
                res = s[one_left + 1 : one_right]
            if s[ind] == s[ind - 1]:
                two_left, two_right = get_mx(ind - 2, ind + 1)
                if two_right - two_left - 1 > mx:
                    mx = two_right - two_left - 1
                    res = s[two_left + 1 : two_right]

        return res
