from collections import defaultdict
from heapq import heapify, heappop, heappush
import os


def prims(n: int, edges: list[list[int]], start: int) -> int:
    graph = defaultdict(list)
    for node1, node2, weight in edges:
        graph[node1].append((weight, node2))
        graph[node2].append((weight, node1))

    visited = set([edges[0][0]])
    edges_heap = graph[edges[0][0]]
    heapify(edges_heap)
    res = 0

    while len(visited) != n:
        weight, node = heappop(edges_heap)
        if not node in visited:
            res += weight
            visited.add(node)
            for el in graph[node]:
                heappush(edges_heap, el)

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))
    start = int(input().strip())
    result = prims(n, edges, start)
    fptr.write(str(result) + "\n")
    fptr.close()
