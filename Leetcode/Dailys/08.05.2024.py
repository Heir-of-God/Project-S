class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        n: int = len(score)
        score = list(enumerate(score))
        score.sort(key=lambda x: -x[1])
        res: list[str] = ["_" for _ in range(n)]

        if n > 0:
            res[score[0][0]] = "Gold Medal"
        if n > 1:
            res[score[1][0]] = "Silver Medal"
        if n > 2:
            res[score[2][0]] = "Bronze Medal"

        for ind in range(3, n, 1):
            res[score[ind][0]] = str(ind + 1)

        return res
