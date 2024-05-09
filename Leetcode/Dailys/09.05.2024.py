class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0

        for ind in range(k):
            happy: int = happiness[ind] - ind
            if happy <= 0:
                return res
            res += happy

        return res
