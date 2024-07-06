class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res: dict[str, list[str]] = {}

        for word in strs:
            sorted_word: str = "".join(sorted(list(word)))
            if sorted_word not in res:
                res[sorted_word] = []
            res[sorted_word].append(word)

        return res.values()
