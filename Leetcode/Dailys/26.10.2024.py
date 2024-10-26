class Solution:
    def treeQueries(self, root: Optional[TreeNode], q: List[int]) -> List[int]:
        mp1, mp2, sz = {}, {}, {}
        counter = 0

        def dfs(node, h):
            nonlocal counter
            if not node:
                return 0
            mp1[node.val] = counter
            mp2[counter] = h
            counter += 1
            left_size = dfs(node.left, h + 1)
            right_size = dfs(node.right, h + 1)
            sz[mp1[node.val]] = 1 + left_size + right_size
            return 1 + left_size + right_size

        dfs(root, 0)

        left = [0] * counter
        right = [0] * counter

        for i in range(counter):
            left[i] = mp2[i]
            if i > 0:
                left[i] = max(left[i - 1], left[i])

        for i in range(counter - 1, -1, -1):
            right[i] = mp2[i]
            if i + 1 < counter:
                right[i] = max(right[i], right[i + 1])

        ans = []
        for node in q:
            node_id = mp1[node]
            l, r = node_id, node_id + sz[node_id] - 1
            h = 0
            if l > 0:
                h = max(h, left[l - 1])
            if r + 1 < counter:
                h = max(h, right[r + 1])
            ans.append(h)

        return ans
