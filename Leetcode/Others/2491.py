class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        n: int = len(skill)
        skill.sort()
        res: int = 0
        prev: int = skill[-1] + skill[0]

        for ind in range(n // 2):
            reversed_ind: int = n - ind - 1
            if skill[reversed_ind] + skill[ind] != prev:
                return -1
            res += skill[reversed_ind] * skill[ind]

        return res
