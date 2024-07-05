class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n: int = len(s)
        changes: dict[str, str] = {}
        used_change_to: set[str] = set()

        for char_ind in range(n):
            char_s: str = s[char_ind]
            char_t: str = t[char_ind]

            if char_s in changes:
                if char_t != changes[char_s]:
                    return False
            else:
                if char_t in used_change_to:
                    return False

                changes[char_s] = char_t
                used_change_to.add(char_t)

        return True
