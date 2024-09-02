class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        n: int = len(potions)

        def get_number(spell_strength: int) -> int:
            left: int = 0
            right: int = n - 1
            res: int = 0

            while left <= right:
                mid: int = (left + right) // 2
                mid_el: int = potions[mid]

                if spell_strength * mid_el >= success:
                    right = mid - 1
                    res = n - mid
                else:
                    left = mid + 1

            return res

        return [get_number(el) for el in spells]


class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort(reverse=True)
        spells = sorted([(spell, ind) for ind, spell in enumerate(spells)])
        right = 0
        res: list[int] = [0 for _ in range(len(spells))]

        for spell, ind in spells:
            while right != len(potions) and potions[right] * spell >= success:
                right += 1
            res[ind] = right

        return res
