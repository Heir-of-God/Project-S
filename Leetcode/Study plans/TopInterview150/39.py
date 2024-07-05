class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        needed_count: dict[str, int] = {}
        cur_count: dict[str, int] = {}
        for char in ransomNote:
            if char not in needed_count:
                needed_count[char] = 0
                cur_count[char] = 0
            needed_count[char] += 1

        for char in magazine:
            if char in cur_count:
                cur_count[char] += 1

        for char in needed_count:
            if needed_count[char] > cur_count[char]:
                return False

        return True
