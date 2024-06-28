class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        connects_count: list[int] = [0 for _ in range(n)]
        for node1, node2 in roads:
            connects_count[node1] += 1
            connects_count[node2] += 1

        connects_count.sort()
        res: int = 0
        for mult, c in enumerate(connects_count, 1):
            res += c * mult

        return res
