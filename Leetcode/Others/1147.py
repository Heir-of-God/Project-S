class Solution:
    def longestDecomposition(self, text: str) -> int:
        n: int = len(text)
        res: int = 0
        left: int = 0
        right: int = n - 1
        collected_l: list[str] = []
        collected_r: list[str] = []

        while left <= right:
            collected_l.append(text[left])
            collected_r.append(text[right])

            if collected_l == collected_r[::-1]:
                res += 2 if right != left else 1
                collected_l.clear()
                collected_r.clear()

            left += 1
            right -= 1

        if collected_l:
            res += 1

        return res
