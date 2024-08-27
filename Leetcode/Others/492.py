class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        for W in range(int(area**0.5), 0, -1):
            if area % W == 0:
                L: int = area // W
                return [L, W]

        return "F"
