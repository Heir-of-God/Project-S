class TrieNode:
    def __init__(self) -> None:
        self.end = False
        self.children: dict[str, TrieNode] = {}


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add_path(self, path: list[str]) -> bool:
        cur = self.root

        for char in path:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
            if cur.end:
                return False

        cur.end = True
        return True


class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort(key=len)
        trie = Trie()
        res: list[str] = []

        for path in folder:
            splited: list[str] = path.split("/")[1:]
            added: bool = trie.add_path(splited)
            if added:
                res.append(path)

        return res


class Solution:
    def removeSubfolders(self, folder) -> list[str]:
        folder.sort()
        res: list[str] = [folder[0]]
        last_added: str = folder[0] + "/"

        for ind in range(1, len(folder)):
            if not folder[ind].startswith(last_added):
                last_added = folder[ind] + "/"
                res.append(folder[ind])

        return res
