from collections import defaultdict


class Node(object):
    def __init__(self):
        self.key_set = set([])
        self.prev, self.nxt = None, None

    def add_key(self, key):
        self.key_set.add(key)

    def remove_key(self, key):
        self.key_set.remove(key)

    def get_any_key(self):
        if self.key_set:
            result = self.key_set.pop()
            self.add_key(result)
            return result
        else:
            return None

    def count(self):
        return len(self.key_set)

    def is_empty(self):
        return len(self.key_set) == 0


class DoubleLinkedList(object):
    def __init__(self):
        self.head_node, self.tail_node = Node(), Node()
        self.head_node.nxt, self.tail_node.prev = self.tail_node, self.head_node
        return

    def insert_after(self, x):
        node, temp = Node(), x.nxt
        x.nxt, node.prev = node, x
        node.nxt, temp.prev = temp, node
        return node

    def insert_before(self, x):
        return self.insert_after(x.prev)

    def remove(self, x):
        prev_node = x.prev
        prev_node.nxt, x.nxt.prev = x.nxt, prev_node
        return

    def get_head(self):
        return self.head_node.nxt

    def get_tail(self):
        return self.tail_node.prev

    def get_sentinel_head(self):
        return self.head_node

    def get_sentinel_tail(self):
        return self.tail_node


class AllOne(object):
    def __init__(self):
        self.dll, self.key_counter = DoubleLinkedList(), defaultdict(int)
        self.node_freq = {0: self.dll.get_sentinel_head()}

    def _rmv_key_pf_node(self, pf, key):
        node = self.node_freq[pf]
        node.remove_key(key)
        if node.is_empty():
            self.dll.remove(node)
            self.node_freq.pop(pf)
        return

    def inc(self, key):
        self.key_counter[key] += 1
        cf, pf = self.key_counter[key], self.key_counter[key] - 1
        if cf not in self.node_freq:
            # No need to test if pf = 0 since frequency zero points to sentinel node
            self.node_freq[cf] = self.dll.insert_after(self.node_freq[pf])
        self.node_freq[cf].add_key(key)
        if pf > 0:
            self._rmv_key_pf_node(pf, key)

    def dec(self, key):
        if key in self.key_counter:
            self.key_counter[key] -= 1
            cf, pf = self.key_counter[key], self.key_counter[key] + 1
            if self.key_counter[key] == 0:
                self.key_counter.pop(key)
            if cf != 0:
                if cf not in self.node_freq:
                    self.node_freq[cf] = self.dll.insert_before(self.node_freq[pf])
                self.node_freq[cf].add_key(key)
            self._rmv_key_pf_node(pf, key)

    def getMaxKey(self):
        return self.dll.get_tail().get_any_key() if self.dll.get_tail().count() > 0 else ""

    def getMinKey(self):
        return self.dll.get_head().get_any_key() if self.dll.get_tail().count() > 0 else ""
