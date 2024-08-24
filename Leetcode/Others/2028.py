class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        m: int = len(rolls)
        sm: int = mean * (m + n)
        missing: int = sm - sum(rolls)

        if missing < n or n * 6 < missing:
            return []
        extra: int = missing - n
        full_dices: int = extra // 5
        add_to_last: int = extra - (full_dices * 5)

        res: list[int] = [6 for _ in range(full_dices)] + [1 for _ in range(n - full_dices - 1)]
        if n != full_dices:
            res.append(1 + add_to_last)

        return res
