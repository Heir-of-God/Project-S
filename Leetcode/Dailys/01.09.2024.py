class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        return [] if len(original) != m * n else [original[i : i + n] for i in range(0, m * n, n)]
