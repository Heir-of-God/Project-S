from collections import defaultdict
from heapq import heappop, heappush


def getCost(g_nodes: int, g_from: list[int], g_to: list[int], g_weight: int):
    graph = defaultdict(list)
    for node1, node2, cost in zip(g_from, g_to, g_weight):
        graph[node1].append((node2, cost))
        graph[node2].append((node1, cost))

    def dijkstra(src, dest):
        visited = set()
        queue = [(0, src)]

        while queue:
            cost, node = heappop(queue)
            if node not in visited:
                visited.add(node)
                if node == dest:
                    return cost

                for neighbor, weight in graph[node]:
                    heappush(queue, (cost + (0 if cost > weight else weight - cost), neighbor))

        return -1

    res = dijkstra(1, g_nodes)
    print("NO PATH EXISTS" if res == -1 else res)


if __name__ == "__main__":
    g_nodes, g_edges = map(int, input().rstrip().split())
    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges
    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())
    getCost(g_nodes, g_from, g_to, g_weight)
