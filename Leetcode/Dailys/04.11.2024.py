class Solution:
    def compressedString(self, word: str) -> str:
        res: list[str] = []
        cur_char: str = word[0]
        cur_count = 0
        word += "_"

        for char in word:
            if char != cur_char or cur_count == 9:
                res.append(str(cur_count) + cur_char)
                cur_char = char
                cur_count = 0
            cur_count += 1

        return "".join(res)
