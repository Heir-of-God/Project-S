class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        overall: int = 3 * 2 ** (n - 1)
        if overall < k:
            return ""
        strings: list[str] = []

        def recursion(prev, cur) -> None:
            if cur == n:
                strings.append(prev)
                return

            for char in "abc":
                if not prev or char != prev[-1]:
                    recursion(prev + char, cur + 1)

        recursion("", 0)
        strings.sort()

        return strings[k - 1]
