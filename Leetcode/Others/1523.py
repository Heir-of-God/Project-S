class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low & 1 != 1:
            low += 1

        return (high + 2 - low) // 2
