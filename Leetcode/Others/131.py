class Solution:
    def partition(self, s: str) -> list[list[str]]:
        def is_palindrome(left, right) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        n: int = len(s)
        res: list[list[str]] = []
        cur_sequence: list[str] = []

        def recursion(cur_ind) -> None:
            nonlocal cur_sequence, res

            if cur_ind == n:
                res.append(cur_sequence[:])
                return

            for end in range(cur_ind, n, 1):
                if is_palindrome(cur_ind, end):
                    cur_sequence.append(s[cur_ind : end + 1])
                    recursion(end + 1)
                    cur_sequence.pop()

        recursion(0)
        return res
