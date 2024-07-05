class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words: list[str] = s.split()
        if len(pattern) != len(words):
            return False
        matches: dict[str, str] = {}
        matched_words: set[str] = set()
        n: int = len(pattern)

        for char_ind in range(n):
            pattern_char: str = pattern[char_ind]
            if not pattern_char in matches:
                word: str = words[char_ind]
                if word in matched_words:
                    return False
                matches[pattern_char] = word
                matched_words.add(word)

            else:
                if matches[pattern_char] != words[char_ind]:
                    return False

        return True
