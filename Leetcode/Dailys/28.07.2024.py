from collections import defaultdict, deque


class Solution:
    def secondMinimum(self, n: int, edges: list[list[int]], time: int, change: int) -> int:
        graph: dict[int, list[int]] = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        queue: deque[int] = deque([1])
        minimums: list[int] = [float("inf") for _ in range(n + 1)]
        second_minimums: list[int] = [float("inf") for _ in range(n + 1)]
        minimums[1] = 0
        time_on_next_level: int = 0

        while queue:
            nodes_on_this_level: int = len(queue)
            time_on_next_level += (change - (time_on_next_level % change)) * ((time_on_next_level // change) & 1)
            time_on_next_level += time

            for _ in range(nodes_on_this_level):
                cur_node: int = queue.popleft()

                for neighbor in graph[cur_node]:
                    if minimums[neighbor] > time_on_next_level:
                        second_minimums[neighbor] = minimums[neighbor]
                        minimums[neighbor] = time_on_next_level
                        queue.append(neighbor)
                    elif minimums[neighbor] < time_on_next_level < second_minimums[neighbor]:
                        second_minimums[neighbor] = time_on_next_level
                        queue.append(neighbor)

        return second_minimums[n]
