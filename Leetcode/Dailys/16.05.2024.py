# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return root.val

        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        elif root.val == 3:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        res: dict[TreeNode, int] = {}  # dictionaty node -> value (0 - False, 1 - True)

        while stack:
            last_node = stack[-1]  # Take the node which we've added last iteration
            if not last_node.left and not last_node.right:  # if this node is leaf
                stack.pop()  # we don't need this node anymore
                res[last_node] = last_node.val

            if (
                last_node.left in res and last_node.right in res
            ):  # if this node isn't leaf and we've already calculated its childrens' values
                stack.pop(-1)  # we don't need this node anymore
                if last_node.val == 2:
                    res[last_node] = res[last_node.left] or res[last_node.right]
                elif last_node.val == 3:
                    res[last_node] = res[last_node.left] and res[last_node.right]
            elif (
                last_node.left and last_node.right
            ):  # if this node isn't leaf but we haven't evaluated its children
                stack.append(last_node.left)
                stack.append(last_node.right)

        return res[root]
