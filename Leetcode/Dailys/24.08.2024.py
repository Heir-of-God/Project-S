class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def half_to_palindrome(left: int, odd: bool) -> int:
            res: int = left
            if odd:
                left = left // 10
            while left > 0:
                res = res * 10 + left % 10
                left //= 10
            return res

        length: int = len(n)
        first_half = int(n[: length // 2 + (1 if length & 1 == 1 else 0)])
        n = int(n)
        min_diff: int = float("inf")
        res: int = -1

        candidates: list[tuple[int, int]] = []
        for delta in range(-1, 2, 1):
            palindrome: int = half_to_palindrome(first_half + delta, length & 1)
            diff: int = abs(palindrome - n)
            candidates.append((palindrome, diff))

        candidates.append((10 ** (length - 1) - 1, abs(10 ** (length - 1) - 1 - n)))
        candidates.append((10**length + 1, abs(10**length + 1 - n)))

        for num, diff in candidates:
            if num != n:
                if diff < min_diff:
                    min_diff = diff
                    res = num
                elif diff == min_diff:
                    res = min(res, num)

        return str(res)
