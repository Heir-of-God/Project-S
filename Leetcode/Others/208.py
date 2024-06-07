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

    def search(self, word: str) -> bool:
        cur: TrieNode = self.root
        for char in word:
            if not char in cur.children:
                return False
            cur = cur.children[char]
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur: TrieNode = self.root
        for char in prefix:
            if not char in cur.children:
                return False
            cur = cur.children[char]
        return True
