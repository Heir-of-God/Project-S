class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        cur_needle_ind: int = 0
        cur_ind: int = 0
        n: int = len(needle)

        while cur_ind < len(haystack):
            char: str = haystack[cur_ind]
            print(cur_ind, char)
            if char == needle[cur_needle_ind]:
                cur_needle_ind += 1
                if cur_needle_ind == n:
                    return cur_ind - cur_needle_ind + 1
            else:
                cur_ind -= cur_needle_ind
                cur_needle_ind = 0

            cur_ind += 1

        return -1
