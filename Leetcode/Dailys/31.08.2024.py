from heapq import heappop, heappush


class Solution:
    def maxProbability(
        self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int
    ) -> float:
        graph: list[list[tuple[int, float]]] = [[] for _ in range(n)]
        for (node1, node2), prob in zip(edges, succProb):
            graph[node1].append((node2, prob))
            graph[node2].append((node1, prob))

        def dijkstra(src, dest) -> float:
            queue: list[tuple[float, int]] = [(-1, src)]
            visited = set()

            while queue:
                prob, node = heappop(queue)
                prob *= -1
                if node not in visited:
                    if node == dest:
                        return prob
                    visited.add(node)
                    for child, edge_prob in graph[node]:
                        heappush(queue, (-prob * edge_prob, child))

            return 0

        return dijkstra(start_node, end_node)
