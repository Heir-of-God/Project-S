class Solution:
    def maximumPoints(self, enemyEnergies: list[int], currentEnergy: int) -> int:
        mn: int = min(enemyEnergies)
        if mn > currentEnergy:
            return 0
        energy: int = currentEnergy + sum(enemyEnergies) - mn

        return energy // mn
