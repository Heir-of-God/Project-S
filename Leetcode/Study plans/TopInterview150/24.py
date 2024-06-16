class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        lines: list[str] = []
        cur_length: int = 0
        cur_line: list[str] = []

        for word in words:
            l: int = len(word)
            if cur_length + l + len(cur_line) <= maxWidth:
                cur_length += l
                cur_line.append(word)
            else:
                if not len(cur_line) == 1:
                    spaces_width = maxWidth - cur_length
                    spaces_length = spaces_width // (len(cur_line) - 1)
                    extra_spaces = spaces_width - (spaces_length * (len(cur_line) - 1))
                    res: str = cur_line[0]
                    for ind in range(1, len(cur_line), 1):
                        res += " " * (spaces_length if ind > extra_spaces else spaces_length + 1)
                        res += cur_line[ind]
                else:
                    res = cur_line[0] + " " * (maxWidth - len(cur_line[0]))
                lines.append(res)
                cur_length = len(word)
                cur_line = [word]
        if cur_line:
            res = " ".join(cur_line)
            res += " " * (maxWidth - len(res))
            lines.append(res)
        return lines
