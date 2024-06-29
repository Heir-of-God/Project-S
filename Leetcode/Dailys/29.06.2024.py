from collections import defaultdict


class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        res: list[list[int]] = [[] for _ in range(n)]
        paths = defaultdict(list)
        for source, destination in edges:
            paths[source].append(destination)

        def dfs(add_ancestor, cur_node):
            for neighbor in paths[cur_node]:
                if not neighbor in seen:
                    seen.add(neighbor)
                    dfs(add_ancestor, neighbor)

        seen = set()
        for node in range(n):
            dfs(node, node)
            for child in seen:
                res[child].append(node)

            seen.clear()

        return res
