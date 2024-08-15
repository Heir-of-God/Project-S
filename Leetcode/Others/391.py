class Solution:
    def isRectangleCover(self, rectangles: list[list[int]]) -> bool:
        area_sum = 0
        mn_x: int = float("inf")
        mx_x: int = -float("inf")
        mn_y: int = float("inf")
        mx_y: int = -float("inf")
        seen_corners = {}
        seen_rects = set()

        for first_x, first_y, second_x, second_y in rectangles:
            area_sum += (second_x - first_x) * (second_y - first_y)
            mx_x = max(mx_x, second_x)
            mn_x = min(mn_x, first_x)
            mx_y = max(mx_y, second_y)
            mn_y = min(mn_y, first_y)

            if (first_x, first_y, second_x, second_y) in seen_rects:
                return False
            seen_rects.add((first_x, first_y, second_x, second_y))

            seen_corners[(first_x, first_y)] = seen_corners.get((first_x, first_y), 0) + 1
            seen_corners[(second_x, second_y)] = seen_corners.get((second_x, second_y), 0) + 1
            seen_corners[(second_x, first_y)] = seen_corners.get((second_x, first_y), 0) + 1
            seen_corners[(first_x, second_y)] = seen_corners.get((first_x, second_y), 0) + 1

        main_corners: tuple[tuple[int, int], ...] = ((mn_x, mn_y), (mn_x, mx_y), (mx_x, mx_y), (mx_x, mn_y))
        for coors, count in seen_corners.items():
            if (coors[0], coors[1]) not in main_corners and count & 1 == 1:
                return False

        return area_sum == (mx_x - mn_x) * (mx_y - mn_y)
