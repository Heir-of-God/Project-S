class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        n1 = set(nums1)
        n2 = set(nums2)
        n3 = set(nums3)
        res = set()

        for val in n1:
            if val in n2 or val in n3:
                res.add(val)

        for val in n2:
            if val not in res and val in n3:
                res.add(val)

        return list(res)
