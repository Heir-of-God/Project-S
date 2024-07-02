class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counting1: list[int] = [0 for _ in range(1001)]
        counting2: list[int] = [0 for _ in range(1001)]

        for n in nums1:
            counting1[n] += 1

        for n in nums2:
            counting2[n] += 1

        res: list[int] = []
        for number in range(1001):
            c1: int = counting1[number]
            c2: int = counting2[number]
            mn: int = min(c1, c2)
            for _ in range(mn):
                res.append(number)

        return res


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()

        ind1: int = 0
        ind2: int = 0
        l1: int = len(nums1)
        l2: int = len(nums2)
        res: list[int] = []

        while ind1 != l1 and ind2 != l2:
            n1: int = nums1[ind1]
            n2: int = nums2[ind2]
            if n1 == n2:
                res.append(n1)
                ind1 += 1
                ind2 += 1
            elif n1 > n2:
                ind2 += 1
            else:
                ind1 += 1

        return res
