class TrieNode:
    def __init__(self, value=0):
        self.val = value
        self.word_end = False
        self.children = {}


class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert_string(self, s: str, val: int):
        cur = self.head

        for char in s:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]

        cur.word_end = True
        cur.val = val
        return

    def get_sum(self, prefix: str):
        cur = self.head

        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]

        res = 0
        queue = [cur]
        while queue:
            cur = queue.pop()

            if cur.word_end:
                res += cur.val

            for child in cur.children.values():
                queue.append(child)

        return res


class MapSum:

    def __init__(self):
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.insert_string(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.get_sum(prefix)
