class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        m: int = len(rolls)
        cur_sm: int = sum(rolls)
        need: int = (m + n) * mean - cur_sm

        if need < n or need > 6 * n:
            return []

        full: int = (need - n) // 5
        add_to_last: int = need - n - full * 5
        res: list[int] = [6 for _ in range(full)] + [1 for _ in range(n - full)]
        res[-1] += add_to_last

        return res
