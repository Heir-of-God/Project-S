from math import ceil


class Solution:
    def minDamage(self, power: int, damage: list[int], health: list[int]) -> int:
        n: int = len(damage)
        enemies: list[tuple[int, int]] = [(damage[i], ceil(health[i] / power)) for i in range(n)]
        enemies.sort(key=lambda x: x[0] / x[1], reverse=True)
        res = 0
        current_time = 0
        for dps, time_to_kill in enemies:
            res += dps * (current_time + time_to_kill)
            current_time += time_to_kill

        return res
