class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        res: int = 0
        tokens.sort()
        n: int = len(tokens)
        left: int = 0
        right: int = n - 1
        score = 0

        while left <= right:
            if power >= tokens[left]:
                score += 1
                res = max(res, score)
                power -= tokens[left]
                left += 1
            else:
                if not score:
                    return res
                score -= 1
                power += tokens[right]
                right -= 1

        return res
