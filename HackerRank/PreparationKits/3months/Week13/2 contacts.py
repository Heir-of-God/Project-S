import os


class TrieNode:
    def __init__(self, val: str) -> None:
        self.val = val
        self.count = 0
        self.children = {}
        self.word_end = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode("")

    def add_word(self, name: str) -> None:
        cur_node: TrieNode = self.root
        for char in name:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode(char)
            cur_node = cur_node.children[char]
            cur_node.count += 1
        cur_node.word_end = True

    def count_with_prefix(self, prefix: str) -> int:
        cur_node = self.root
        for char in prefix:
            if char not in cur_node.children:
                return 0
            cur_node = cur_node.children[char]

        return cur_node.count


def contacts(queries: list[list[str]]) -> list[int]:
    res = []
    trie = Trie()
    for query in queries:
        command, val = query
        if command == "add":
            trie.add_word(val)
        elif command == "find":
            res.append(trie.count_with_prefix(val))

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    queries_rows = int(input().strip())
    queries = []
    for _ in range(queries_rows):
        queries.append(input().rstrip().split())
    result = contacts(queries)
    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")
    fptr.close()
