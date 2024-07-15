class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> Optional[TreeNode]:
        def construct_tree(cur_node_val):
            new_node = TreeNode(cur_node_val)
            if cur_node_val in children_hashmap:
                if children_hashmap[cur_node_val][0] is not None:
                    new_node.left = construct_tree(children_hashmap[cur_node_val][0])
                if children_hashmap[cur_node_val][1] is not None:
                    new_node.right = construct_tree(children_hashmap[cur_node_val][1])
            return new_node

        children_set = set()
        children_hashmap: dict[int, list[int]] = {}

        for parent, child, isleft in descriptions:
            if not parent in children_hashmap:
                children_hashmap[parent] = [None, None]  # left and right
            children_set.add(child)
            target = 0 if isleft else 1
            children_hashmap[parent][target] = child

        for parent in children_hashmap:
            if parent not in children_set:
                head_node_val: int = parent
                break
        head = construct_tree(head_node_val)
        return head
