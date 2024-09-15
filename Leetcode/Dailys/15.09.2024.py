class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        res = 0
        xores = {(0, 0, 0, 0, 0): -1}
        cur = [0, 0, 0, 0, 0]

        for ind, char in enumerate(s):
            match char:
                case "a":
                    cur[0] = 1 if not cur[0] else 0
                case "e":
                    cur[1] = 1 if not cur[1] else 0
                case "o":
                    cur[2] = 1 if not cur[2] else 0
                case "i":
                    cur[3] = 1 if not cur[3] else 0
                case "u":
                    cur[4] = 1 if not cur[4] else 0

            key = tuple(cur)
            if key in xores:
                res = max(res, ind - xores[key])
            else:
                xores[key] = ind

        return res
