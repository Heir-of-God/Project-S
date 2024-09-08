class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        res = [s[i : i + k] for i in range(0, n, k)]
        res[-1] += (k - len(res[-1])) * fill
        return res
