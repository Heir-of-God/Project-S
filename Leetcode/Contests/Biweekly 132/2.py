class Solution:
    def findWinningPlayer(self, skills: list[int], k: int) -> int:
        if k >= len(skills) - 1:
            return skills.index(max(skills))

        win_count = 0
        current_winner: int = skills[0]

        for i in range(1, len(skills)):
            if skills[i] > current_winner:
                current_winner = skills[i]
                win_count = 1
            else:
                win_count += 1

            if win_count == k:
                return skills.index(current_winner)

        return skills.index(current_winner)
