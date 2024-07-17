from collections import deque


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: list[int]) -> list[TreeNode]:
        res: dict[int, TreeNode] = {root.val: root}
        to_delete: set[int] = set(to_delete)

        def recursion(parent: TreeNode | None, cur_node: TreeNode | None, isleft: bool) -> None:
            nonlocal res
            if cur_node is None:
                return

            recursion(cur_node, cur_node.left, True)
            recursion(cur_node, cur_node.right, False)

            if cur_node.val in to_delete:
                if cur_node.val in res:
                    del res[cur_node.val]

                if parent:
                    if isleft:
                        parent.left = None
                    else:
                        parent.right = None

                if cur_node.left:
                    res[cur_node.left.val] = cur_node.left
                if cur_node.right:
                    res[cur_node.right.val] = cur_node.right

        recursion(None, root, False)
        return res.values()


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: list[int]) -> list[TreeNode]:
        if not root:
            return

        to_delete: set[int] = set(to_delete)
        res: list[TreeNode] = [root] if not root.val in to_delete else []
        queue: deque[TreeNode] = deque([root])

        while queue:
            cur_node: TreeNode = queue.popleft()

            if cur_node.left:
                queue.append(cur_node.left)

                if cur_node.left.val in to_delete:
                    cur_node.left = None  # disconnect left child if we will delete it

            if cur_node.right:
                queue.append(cur_node.right)

                if cur_node.right.val in to_delete:
                    cur_node.right = None

            if cur_node.val in to_delete:  # if we need to delete this node
                if cur_node.left is not None:  # It's None if we need to delete left child too
                    res.append(cur_node.left)
                if cur_node.right is not None:
                    res.append(cur_node.right)

        return res
