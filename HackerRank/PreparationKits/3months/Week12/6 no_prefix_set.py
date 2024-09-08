class TrieNode:
    def __init__(self, val) -> None:
        self.val = val
        self.children = {}
        self.word_end = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode("")

    def add_str(self, s: str) -> bool:
        node: TrieNode = self.root
        for char in s:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
            if node.word_end:
                return False
        node.word_end = True
        return True if not node.children else False

    # def is_there_prefix(self) -> bool:
    #     queue = [self.root]
    #     while queue:
    #         node = queue.pop()
    #         if node.word_end and node.children:
    #             return True
    #         for _, child in node.children.items():
    #             queue.append(child)

    #     return False


def noPrefix(words: list[str]) -> None:
    trie = Trie()
    res: str = "GOOD SET"
    for word in words:
        if not trie.add_str(word):
            res = f"BAD SET\n{word}"
            break
    print(res)


if __name__ == "__main__":
    n = int(input().strip())
    words = []
    for _ in range(n):
        words_item = input()
        words.append(words_item)
    noPrefix(words)
