from heapq import heappop, heappush


class Solution:
    def maxProbability(
        self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int
    ) -> float:
        graph: list[list[tuple[int, float]]] = [[] for _ in range(n)]
        for ind in range(len(edges)):
            n1, n2, prob = *edges[ind], succProb[ind]
            graph[n1].append((n2, prob))
            graph[n2].append((n1, prob))

        def djikstra(src: int, end: int) -> float:
            queue: list[tuple[float, int]] = [(-1, src)]  # (probability, node)
            visited = set()

            while queue:
                prob, node = heappop(queue)
                prob *= -1
                if node not in visited:
                    if node == end:
                        return prob

                    visited.add(node)
                    for children, edge_prob in graph[node]:
                        heappush(queue, (prob * (-edge_prob), children))
            return 0

        return djikstra(start_node, end_node)
