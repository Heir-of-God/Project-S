class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        res = 0

        for ind in range(1, len(colors) - 1):
            if colors[ind - 1] == colors[ind + 1] and colors[ind - 1] != colors[ind]:
                res += 1

        res += colors[1] == colors[-1] and colors[1] != colors[0]
        res += colors[0] == colors[-2] and colors[-1] != colors[0]

        return res
