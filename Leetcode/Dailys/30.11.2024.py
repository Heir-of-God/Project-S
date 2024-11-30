from collections import defaultdict


class Solution:
    def validArrangement(self, pairs: list[list[int]]) -> list[list[int]]:
        graph = defaultdict(list)
        degrees_delta = defaultdict(int)

        for start, end in pairs:
            graph[start].append(end)
            degrees_delta[start] += 1
            degrees_delta[end] -= 1

        startNode: int = pairs[0][0]
        for node in degrees_delta:
            if degrees_delta[node] == 1:
                startNode = node
                break

        path = []

        def dfs(curr):
            while graph[curr]:
                nextNode = graph[curr].pop()
                dfs(nextNode)
                path.append((curr, nextNode))

        dfs(startNode)
        return path[::-1]
