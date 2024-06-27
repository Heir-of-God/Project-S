class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        seen = set()
        for edge in edges:
            first: int = edge[0]
            second: int = edge[1]

            if first in seen:
                return first
            elif second in seen:
                return second
            seen.add(first)
            seen.add(second)


class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        candidate_a: int = edges[0][0]
        candidate_b: int = edges[0][1]

        if candidate_a in edges[1]:
            return candidate_a
        else:
            return candidate_b
