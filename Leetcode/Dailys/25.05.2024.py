class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)
        results = []
        self.backtrack(s, word_set, [], results, 0)
        return results

    def backtrack(
        self,
        s: str,
        word_set: set,
        current_sentence: list[str],
        results: list[str],
        start_index: int,
    ):
        if start_index == len(s):
            results.append(" ".join(current_sentence))
            return

        for end_index in range(start_index + 1, len(s) + 1):
            word = s[start_index:end_index]
            if word in word_set:
                current_sentence.append(word)
                self._backtrack(s, word_set, current_sentence, results, end_index)
                current_sentence.pop()
