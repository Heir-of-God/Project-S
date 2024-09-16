class Solution:
    def countPoints(self, rings: str) -> int:
        colors: list[list[bool]] = [[False for _ in range(3)] for _ in range(10)]

        for start_ind in range(0, len(rings), 2):
            color: int = 0 if rings[start_ind] == "B" else 1 if rings[start_ind] == "G" else 2
            ring = int(rings[start_ind + 1])
            colors[ring][color] = True

        res = 0
        for ring in colors:
            if all(ring):
                res += 1

        return res
