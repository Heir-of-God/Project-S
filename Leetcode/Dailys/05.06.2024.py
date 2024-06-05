class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        freq: dict[str, list[int]] = {}  # char -> array which contain frequency for every word
        for char in words[0]:
            if not char in freq:
                freq[char] = []

        for ind, word in enumerate(words):
            for key in freq:
                freq[key].append(0)

            for char in word:
                if char in freq:
                    freq[char][ind] += 1

        res: list[str] = []
        for char in freq:
            f: int = min(freq[char])
            for _ in range(f):
                res.append(char)

        return res


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        freq: dict[str, int] = {}  # char -> min frequency for this character
        for char in words[0]:
            if not char in freq:
                freq[char] = 101

        counter: dict[str, int] = {char: 0 for char in freq}
        for word in words:
            for k in counter:
                counter[k] = 0

            for char in word:
                if char in counter:
                    counter[char] += 1

            for char in counter:
                freq[char] = min(freq[char], counter[char])

        res: list[str] = []
        for char, val in freq.items():
            for _ in range(val):
                res.append(char)

        return res
