class Solution:
    def edgeScore(self, edges: list[int]) -> int:
        scores: dict[int, int] = {}
        mx: int = 0

        for ind, pointing in enumerate(edges):
            if pointing not in scores:
                scores[pointing] = 0
            scores[pointing] += ind
            mx = max(mx, scores[pointing])

        return min([edge for edge in scores if scores[edge] == mx])
