class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        n: int = len(tops)
        candidate_a: int = tops[0]
        candidate_b: int = bottoms[0]

        a_reverse1 = 0
        a_reverse2 = 0
        b_reverse1 = 0
        b_reverse2 = 0

        for ind in range(n):
            top_val = tops[ind]
            bot_val = bottoms[ind]
            if candidate_a not in [top_val, bot_val]:
                a_reverse1 = -1
                a_reverse2 = -1
            if candidate_b not in [top_val, bot_val]:
                b_reverse1 = -1
                b_reverse2 = -1
            if a_reverse1 == b_reverse1 == -1:
                return -1

            if a_reverse1 != -1 and bot_val == candidate_a and top_val != candidate_a:
                a_reverse1 += 1
            if a_reverse2 != -1 and bot_val != candidate_a and top_val == candidate_a:
                a_reverse2 += 1
            if b_reverse1 != -1 and bot_val == candidate_b and top_val != candidate_b:
                b_reverse1 += 1
            if b_reverse2 != -1 and bot_val != candidate_b and top_val == candidate_b:
                b_reverse2 += 1

        return min([p for p in [a_reverse1, a_reverse2, b_reverse1, b_reverse2] if p != -1])
