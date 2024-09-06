class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        n: int = len(graph)
        paths: list[list[int]] = []
        cur_path: list[int] = []

        def dfs(cur_node) -> None:
            cur_path.append(cur_node)
            if cur_node == n - 1:
                paths.append(cur_path[:])
                cur_path.pop()
                return

            for neighbor in graph[cur_node]:
                dfs(neighbor)
            cur_path.pop()

        dfs(0)
        return paths
