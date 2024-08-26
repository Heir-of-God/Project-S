class Solution:
    def postorder(self, root: "Node") -> list[int]:
        res: list[int] = []

        def recursion(node):
            if not node:
                return
            for child in node.children:
                recursion(child)
            res.append(node.val)

        recursion(root)
        return res


class Solution:
    def postorder(self, root: "Node") -> list[int]:
        if not root:
            return []

        res: list[int] = []
        stack: list[tuple["Node", bool]] = [(root, False)]  # (node, already visited its children)

        while stack:
            node, visited = stack.pop()
            if visited:
                res.append(node.val)
            else:
                stack.append((node, True))  # we want to return to this node as soon as we check all its children
                for child in node.children[::-1]:  # [::-1 because we want left-most children to be considered first]
                    stack.append((child, False))

        return res
