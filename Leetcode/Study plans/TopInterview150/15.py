class Solution:
    def candy(self, ratings: list[int]) -> int:
        n: int = len(ratings)
        res: list[int] = [1 for _ in range(n)]

        # every right bigger must have more candies
        for ind in range(1, n, 1):
            if ratings[ind] > ratings[ind - 1]:
                res[ind] = res[ind - 1] + 1

        # every left bigger must have more candies
        for ind in range(n - 2, -1, -1):
            if ratings[ind] > ratings[ind + 1]:
                res[ind] = max(res[ind], res[ind + 1] + 1)

        return sum(res)
