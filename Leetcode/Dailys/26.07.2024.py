class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        # first convert graph to adjacency list representation
        graph: list[list[int]] = [[] for _ in range(n)]  # i-th nodes will have graph[i] neighbors
        for node1, node2, distance in edges:
            graph[node1].append([node2, distance])
            graph[node2].append([node1, distance])

        def get_number_of_neighbors_in_distance(source: int) -> int:
            queue: list[tuple[int, int]] = [
                (0, source)
            ]  # distance to node itself is 0, first store distance so heap is "sorted" b distance
            visited = set()

            while queue:
                distance_to_this_node, cur_node = heappop(queue)
                if not cur_node in visited:
                    visited.add(cur_node)
                    for neighbor, distance in graph[cur_node]:
                        distance_from_source = distance_to_this_node + distance
                        if distance_from_source <= distanceThreshold:  # ensure that we're allowed to go to this node
                            heappush(queue, (distance_from_source, neighbor))

            # actually you can return len(visited) and with math there will be nothing wrong but actually we have len(visited) - 1 neighbors since we're not neighbor of ourselves
            return len(visited) - 1

        minimum_number: int = n
        res: int = None

        for source in range(n):
            neighbors: int = get_number_of_neighbors_in_distance(source)
            # we iterate source from smaller to bigger this ensures that we choose node with greater value if they have equal number of neighbors
            if neighbors <= minimum_number:
                minimum_number = neighbors
                res = source

        return res


class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        distance: list[list[int]] = [[float("inf") for _ in range(n)] for _ in range(n)]
        for node in range(n):
            distance[node][node] = 0  # distance to itself is 0

        # The distance between nodes which are connected temporary distance between them
        for node1, node2, dist in edges:
            distance[node1][node2] = dist
            distance[node2][node1] = dist

        for midle in range(n):
            for source in range(n):
                for destination in range(n):
                    distance[source][destination] = min(
                        distance[source][destination], distance[source][midle] + distance[midle][destination]
                    )  # the minimum distance is either current value or new value with path that goes through midle

        minimum_number: int = n
        res: int = None

        for source in range(n):
            source_count = 0
            for destination in range(n):
                if distance[source][destination] <= distanceThreshold:
                    source_count += 1

            if source_count <= minimum_number:  # as in dijkstra when number equal we choose greater node
                minimum_number = source_count
                res = source

        return res
