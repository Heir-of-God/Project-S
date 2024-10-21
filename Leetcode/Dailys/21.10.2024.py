class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n: int = len(s)
        included: set[int] = set()
        res: int = 0

        def recursion(cur_ind: int) -> None:
            nonlocal res

            if cur_ind >= n:
                res = max(res, len(included))
                return
            elif len(included) + n - cur_ind <= res:
                return

            for right_ind in range(cur_ind, n, 1):
                if s[cur_ind : right_ind + 1] not in included:
                    included.add(s[cur_ind : right_ind + 1])
                    recursion(right_ind + 1)
                    included.remove(s[cur_ind : right_ind + 1])

        recursion(0)
        return res
