class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        graph = defaultdict(list)
        for src, destination, distance in zip(original, changed, cost):
            graph[src].append([destination, distance])

        def dijkstra(source):
            queue: list[tuple[int, int]] = [(0, source)]
            shortest = [float("inf") for _ in range(26)]
            visited = set()

            while queue:
                cur_cost, cur_node = heappop(queue)
                if cur_node not in visited:
                    shortest[ord(cur_node) - ord("a")] = cur_cost
                    visited.add(cur_node)
                    for neighbor, dist in graph[cur_node]:
                        heappush(queue, (dist + cur_cost, neighbor))
            return shortest

        n: int = len(source)
        res = 0
        temp: dict[str, list[int]] = {}  # char -> list 26 values shortest path from this char to any other
        for ind in range(n):
            src: str = source[ind]
            trg: str = target[ind]
            if src != trg:
                if src not in temp:
                    temp[src] = dijkstra(src)
                if temp[src][ord(trg) - ord("a")] == float("inf"):
                    return -1
                res += temp[src][ord(trg) - ord("a")]

        return res


class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        matrix: list[list[int]] = [[float("inf") for _ in range(26)] for _ in range(26)]

        for char_ind in range(0, 26, 1):
            matrix[char_ind][char_ind] = 0

        for ind in range(len(original)):
            src: str = original[ind]
            dest: str = changed[ind]
            dist: int = cost[ind]
            matrix[ord(src) - ord("a")][ord(dest) - ord("a")] = min(
                dist, matrix[ord(src) - ord("a")][ord(dest) - ord("a")]
            )

        for midle in range(26):
            for src in range(26):
                for dest in range(26):
                    matrix[src][dest] = min(matrix[src][dest], matrix[src][midle] + matrix[midle][dest])

        res = 0
        for ind in range(len(source)):
            src = source[ind]
            trg: str = target[ind]
            min_cost: int = matrix[ord(src) - ord("a")][ord(trg) - ord("a")]
            if isinf(min_cost):
                return -1
            res += min_cost

        return res
