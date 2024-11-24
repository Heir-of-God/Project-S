class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        full_sm: int = 0
        subtract: int = float("inf")
        number_of_negatives: int = 0

        for row in matrix:
            for val in row:
                full_sm += abs(val)
                if val < 0:
                    number_of_negatives += 1
                subtract = min(subtract, abs(val))

        return full_sm if number_of_negatives & 1 == 0 else full_sm - 2 * subtract
