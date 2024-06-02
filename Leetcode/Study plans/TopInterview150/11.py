class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        n: int = len(citations)
        cur_h: int = n

        for num in citations:
            if num >= cur_h:
                return cur_h
            cur_h -= 1

        return 0
