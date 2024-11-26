class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        teams = set([i for i in range(n)])

        for _, week in edges:
            if week in teams:
                teams.remove(week)

        return teams.pop() if len(teams) == 1 else -1
