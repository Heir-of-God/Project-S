class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        n: int = len(position)
        position.sort()

        def can_place_balls(mn_force: int) -> int:
            placed: int = 0
            last_placed: int = None

            for pos in position:
                if last_placed is None or pos - last_placed >= mn_force:
                    last_placed = pos
                    placed += 1

            return placed

        left: int = n // m
        right: int = (position[-1] - position[0]) // (m - 1)
        res: int = -1

        while left <= right:
            mid: int = (right + left) // 2
            balls_to_place = can_place_balls(mid)
            if balls_to_place < m:
                right = mid - 1
            else:
                res = mid
                left = mid + 1

        return res
