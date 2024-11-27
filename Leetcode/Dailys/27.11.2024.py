from heapq import heappop, heappush


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        def get_shortest() -> int:
            start: int = 0
            target: int = n - 1

            heap: list[tuple[int, int]] = [(0, start)]  # (cur_node, distance) (djikstra)
            visited: set[int] = set()

            while heap:
                dist, node = heappop(heap)

                if node not in visited:
                    visited.add(node)
                    if node == target:
                        return dist
                    for child in graph[node]:
                        heappush(heap, (dist + 1, child))

            return -1

        graph: dict[int, list[int]] = {}
        for node in range(0, n - 1, 1):
            graph[node] = [node + 1]

        res: list[int] = []
        for src, dst in queries:
            graph[src].append(dst)
            res.append(get_shortest())

        return res


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        def get_shortest() -> int:
            start: int = 0
            target: int = n - 1

            level: list[int] = [start]  # (cur_node) (bfs)
            vis: set[int] = set([start])
            res: int = 0

            while level:
                nxt: list[int] = []
                for node in level:
                    if node == target:
                        return res
                    for child in graph[node]:
                        if child not in vis:
                            nxt.append(child)
                            vis.add(child)
                level = nxt
                res += 1

            return -1

        graph: dict[int, list[int]] = {}
        for node in range(0, n - 1, 1):
            graph[node] = [node + 1]

        res: list[int] = []
        for src, dst in queries:
            graph[src].append(dst)
            res.append(get_shortest())

        return res
