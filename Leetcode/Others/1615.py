class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        counter: list[list[int]] = [[0, ind] for ind in range(n)]
        roads = set(tuple(i) for i in roads)
        for n1, n2 in roads:
            counter[n1][0] += 1
            counter[n2][0] += 1
        counter.sort(reverse=True)

        change = False
        ind = 1
        while ind != n:
            if counter[ind][0] != counter[ind - 1][0]:
                if change:
                    break
                change = True
            ind += 1
        counter = counter[:ind]

        mx: int = 0
        n: int = len(counter)
        for ind1 in range(n - 1):
            for ind2 in range(ind1 + 1, n, 1):
                node1, node2 = counter[ind1][1], counter[ind2][1]
                res: int = (
                    counter[ind1][0]
                    + counter[ind2][0]
                    - (not (not (node1, node2) in roads and not (node2, node1) in roads))
                )
                mx = max(mx, res)

        return mx
