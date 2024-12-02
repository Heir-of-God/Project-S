class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for ind, word in enumerate(sentence.split()):
            if word.startswith(searchWord):
                return ind + 1
        return -1
