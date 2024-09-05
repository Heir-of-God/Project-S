class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]

        while queue:
            new = []
            res.append([])

            for node in queue:
                res[-1].append(node.val)
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)

            queue = new

        return res[::-1]
