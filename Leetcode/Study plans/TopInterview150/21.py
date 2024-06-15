class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        return " ".join(s[::-1])


class Solution:
    def reverseWords(self, s: str) -> str:
        words: list[str] = []
        cur_start_ind: int | None = None
        s += " "

        for ind, char in enumerate(s):
            if char != " ":
                if cur_start_ind is None:
                    cur_start_ind = ind
            else:
                if not cur_start_ind is None:
                    words.append(s[cur_start_ind:ind])
                    cur_start_ind = None

        res: str = ""
        for ind in range(len(words) - 1, -1, -1):
            res += words[ind]
            res += " "

        return res[:-1]
