class TrieNode:
    def __init__(self) -> None:
        self.is_end: bool = False  # indicating that word ends there
        self.children: dict[str, TrieNode] = {}  # character -> child which starts with this character


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur: TrieNode = self.root
        for char in word:
            if not char in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_end = True

    def get_prefix_by_word(self, word) -> str:
        cur: TrieNode = self.root
        for ind, char in enumerate(word):
            if cur.is_end:
                return word[:ind]
            if not char in cur.children:
                break
            cur = cur.children[char]
        return word


class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        words: list[str] = sentence.split()
        trie = Trie()
        for prefix in dictionary:
            trie.insert(prefix)
        return " ".join([trie.get_prefix_by_word(word) for word in words])
