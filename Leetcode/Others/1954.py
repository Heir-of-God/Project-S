class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        level = 0
        while neededApples > 0:
            level += 1
            neededApples -= 12 * level**2
        return 8 * level
