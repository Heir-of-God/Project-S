class TrieNode:
    def __init__(self, val) -> None:
        self.val = val
        self.children = {}
        self.end_word = False


class TrieTree:
    def __init__(self) -> None:
        self.root = TrieNode("")

    def add_word(self, word: str) -> None:
        cur_node: TrieNode = self.root
        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode(char)
            cur_node = cur_node.children[char]
        cur_node.end_word = True

    def search(self, word: str, start_node: TrieNode = None) -> bool:
        if word == "":
            return True
        cur_node: TrieNode = start_node if start_node else self.root

        for ind, char in enumerate(word):
            if char != "." and char not in cur_node.children:
                return False
            if char == ".":
                if ind == len(word) - 1:
                    for child, nxt in cur_node.children.items():
                        if nxt.end_word:
                            return True
                    return False
                res = False
                for child, nxt in cur_node.children.items():
                    res = res or self.search(word[ind + 1 :], nxt)
                return res
            else:
                cur_node = cur_node.children[char]

        return cur_node.end_word


class WordDictionary:
    def __init__(self):
        self.trie = TrieTree()

    def addWord(self, word: str) -> None:
        self.trie.add_word(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
