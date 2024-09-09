# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> list[list[int]]:
        res: list[list[int]] = [[-1 for _ in range(n)] for _ in range(m)]
        dirs: list[tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_dir = 0
        row, col = 0, 0

        while head:
            val: int = head.val
            head = head.next
            res[row][col] = val

            if (
                not 0 <= row + dirs[cur_dir][0] < m
                or not 0 <= col + dirs[cur_dir][1] < n
                or res[row + dirs[cur_dir][0]][col + dirs[cur_dir][1]] != -1
            ):
                cur_dir += 1
                cur_dir %= 4
            row += dirs[cur_dir][0]
            col += dirs[cur_dir][1]

        return res
