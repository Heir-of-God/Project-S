class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(cur_node, parent) -> int:
            if cur_node == None:
                return 0
            moves: int = dfs(cur_node.left, cur_node) + dfs(
                cur_node.right, cur_node
            )  # both values >= since we return abs(coins)
            from_this: int = cur_node.val - 1  # we want to keep 1 coin here
            parent.val += from_this  # transfer this coins from child to parent (without deleting it from child, we already calculated these moves and don't interested in this child anymore)
            moves += abs(
                from_this
            )  # abs() because from_this can be equal to -1 (we want there 1 coin from parent)
            return moves

        return dfs(root, TreeNode())  # adding empty node as parent for root to keep code simple
