class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if "" in strs:
            return ""

        cur_ind = 0
        while True:
            char = None
            for word in strs:
                if len(word) == cur_ind:
                    return word
                if char is None:
                    char = word[cur_ind]
                elif word[cur_ind] != char:
                    return word[:cur_ind]
            cur_ind += 1
