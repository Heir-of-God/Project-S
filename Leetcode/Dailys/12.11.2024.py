class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        items.sort()
        queries = sorted([val, ind] for ind, val in enumerate(queries))
        res: list[int] = [0 for _ in range(len(queries))]
        mx: int = 0
        ind: int = 0

        for val, ind_q in queries:
            while ind < len(items) and items[ind][0] <= val:
                mx = max(mx, items[ind][1])
                ind += 1
            res[ind_q] = mx

        return res
