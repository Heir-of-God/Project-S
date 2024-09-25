class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.count = 0


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, string: str) -> None:
        node: TrieNode = self.root
        for char in string:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1

    def get_prefix_sum(self, string: str) -> int:
        res: int = 0
        node: TrieNode = self.root
        for char in string:
            node = node.children[char]
            res += node.count
        return res


class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        res: list[int] = []
        for word in words:
            res.append(trie.get_prefix_sum(word))

        return res
