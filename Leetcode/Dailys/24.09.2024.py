class TrieNode:
    def __init__(self) -> None:
        self.children: dict[int, TrieNode] = {}


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, num_digits) -> None:
        node = self.root
        for digit in num_digits:
            if not digit in node.children:
                node.children[digit] = TrieNode()
            node = node.children[digit]

    def find_longest_prefix(self, num_digits) -> int:
        node = self.root
        res = 0

        for digit in num_digits:
            if not digit in node.children:
                break
            res += 1
            node = node.children[digit]

        return res


class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        def get_digit_lst(num):
            res = []
            while num > 0:
                res.append(num % 10)
                num //= 10
            return res[::-1] if res else 0

        trie = Trie()
        for num in arr1:
            trie.insert(get_digit_lst(num))

        res = 0
        for num in arr2:
            res = max(res, trie.find_longest_prefix(get_digit_lst(num)))

        return res
