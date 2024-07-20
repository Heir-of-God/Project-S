class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        res = 0
        while x > 0 and y > 3:
            res += 1
            x -= 1
            y -= 4

        return "Alice" if res % 2 == 1 else "Bob"
