import heapq


class Solution:
    def modifiedGraphEdges(self, n, edges, source, destination, target):
        adjacency_list = [[] for _ in range(n)]
        for i, (u, v, w) in enumerate(edges):
            adjacency_list[u].append((v, i))
            adjacency_list[v].append((u, i))

        distances = [[float("inf")] * 2 for _ in range(n)]
        distances[source][0] = distances[source][1] = 0

        def dijkstra(include_negatives, difference):
            pq = [(0, source)]
            while pq:
                current_dist, node = heapq.heappop(pq)
                if current_dist > distances[node][include_negatives]:
                    continue
                for neighbor, idx in adjacency_list[node]:
                    weight = edges[idx][2]
                    if weight == -1:
                        weight = 1
                    if include_negatives == 1 and edges[idx][2] == -1:
                        new_weight = difference + distances[neighbor][0] - distances[node][1]
                        weight = max(weight, new_weight)
                        edges[idx][2] = weight
                    if distances[neighbor][include_negatives] > current_dist + weight:
                        distances[neighbor][include_negatives] = current_dist + weight
                        heapq.heappush(pq, (distances[neighbor][include_negatives], neighbor))

        dijkstra(0, 0)
        diff = target - distances[destination][0]
        if diff < 0:
            return []

        dijkstra(1, diff)
        if distances[destination][1] < target:
            return []

        for edge in edges:
            if edge[2] == -1:
                edge[2] = 1

        return edges
