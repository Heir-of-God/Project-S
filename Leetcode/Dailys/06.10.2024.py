class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1: list[str] = sentence1.split()
        s2: list[str] = sentence2.split()
        if len(s1) == 1:
            return s1[0] in (s2[0], s2[-1])
        elif len(s2) == 1:
            return s2[0] in (s1[0], s1[-1])

        left: int = 0
        right1: int = len(s1) - 1
        right2: int = len(s2) - 1

        while left <= right1 and left <= right2:
            if s1[left] != s2[left] and s1[right1] != s2[right2]:
                return False

            if s1[left] == s2[left]:
                left += 1

            if s1[right1] == s2[right2]:
                right1 -= 1
                right2 -= 1

        return True
