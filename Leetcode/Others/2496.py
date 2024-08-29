class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = 0
        for s in strs:
            val = len(s) if not s.isnumeric() else int(s)
            res = max(res, val)
        return res
