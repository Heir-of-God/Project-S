from heapq import nlargest


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levels_sum = []
        stack = [root]

        while stack:
            nxt = []
            res = 0

            for node in stack:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
                res += node.val

            levels_sum.append(res)
            stack = nxt

        largs = nlargest(k, levels_sum)
        return largs[-1] if len(largs) == k else -1
