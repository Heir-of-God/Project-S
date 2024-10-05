class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_need = [0 for _ in range(26)]

        for char in s1:
            counter_need[ord(char) - ord("a")] += 1

        left = 0
        for char in s2:
            counter_need[ord(char) - ord("a")] -= 1
            while counter_need[ord(char) - ord("a")] < 0:
                counter_need[ord(s2[left]) - ord("a")] += 1
                left += 1

            if counter_need == [0 for _ in range(26)]:
                return True

        return False
