class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> tuple[int]:
        res: list[tuple[int, int]] = []
        for ind1 in range(len(arr)):
            for ind2 in range(ind1 + 1, len(arr), 1):
                res.append((arr[ind1], arr[ind2]))

        res.sort(key=lambda x: x[0] / x[1])
        return res[k - 1]
