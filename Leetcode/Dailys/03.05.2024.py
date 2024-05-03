class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1: list[int] = [int(i) for i in version1.split(".")]
        ind1 = 0
        v2: list[int] = [int(i) for i in version2.split(".")]
        ind2 = 0
        l1: int = len(v1)
        l2: int = len(v2)

        while ind1 < l1 or ind2 < l2:
            rev1: int = v1[ind1] if ind1 < l1 else 0
            rev2: int = v2[ind2] if ind2 < l2 else 0
            ind1 += 1
            ind2 += 1

            if rev1 > rev2:
                return 1
            elif rev1 < rev2:
                return -1

        return 0
