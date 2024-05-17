class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root:
            root.left = self.removeLeafNodes(root.left, target)
            root.right = self.removeLeafNodes(root.right, target)
            if root.val == target and not root.left and not root.right:
                root = None
        return root


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:  # edge case
            return None

        stack: list[TreeNode] = []
        cur_node = root
        last_right = None

        while stack or cur_node:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left

            cur_node = stack[-1]

            if cur_node.right and cur_node.right is not last_right:
                cur_node = cur_node.right
                continue
            stack.pop()

            if not cur_node.right and not cur_node.left and cur_node.val == target:
                if (
                    not stack
                ):  # if stack is empty and there's no right or left then we're deleting the root and want to return None
                    return None

                parent = (
                    stack[-1] if stack else None
                )  # if stack is empty then we are considering root node and it doesn't have parent

                if parent and parent.left is cur_node:
                    parent.left = None
                elif parent and parent.right is cur_node:
                    parent.right = None

            last_right = cur_node
            cur_node = None

        return root
