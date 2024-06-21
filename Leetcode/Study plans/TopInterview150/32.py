class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        from collections import defaultdict

        needed_count = defaultdict(int)
        for word in words:
            needed_count[word] += 1

        n: int = len(s)
        word_length: int = len(words[0])
        res: list[int] = []

        # there can be up to word_length shifting
        for possible_left in range(word_length):
            seen = defaultdict(int)
            left = possible_left
            cur_length_words = 0

            for word_start in range(left, n - word_length + 1, word_length):
                temp_word: str = s[word_start : word_start + word_length]
                if temp_word not in needed_count:
                    seen.clear()
                    cur_length_words = 0
                    left: int = word_start + word_length
                else:
                    seen[temp_word] += 1
                    cur_length_words += 1

                    while seen[temp_word] > needed_count[temp_word]:
                        cur_left_word: str = s[left : left + word_length]
                        seen[cur_left_word] -= 1
                        cur_length_words -= 1
                        left += word_length

                if cur_length_words == len(words):
                    res.append(left)
                    seen[s[left : left + word_length]] -= 1
                    cur_length_words -= 1
                    left += word_length

        return res
