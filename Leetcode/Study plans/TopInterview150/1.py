# 88. Merge Sorted Array


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        pointer1: int = m - 1
        pointer2: int = n - 1
        write_pointer = m + n - 1

        while pointer2 != -1:
            if pointer1 < 0 or nums2[pointer2] >= nums1[pointer1]:
                nums1[write_pointer] = nums2[pointer2]
                pointer2 -= 1
            else:
                nums1[write_pointer] = nums1[pointer1]
                pointer1 -= 1
            write_pointer -= 1

        return None
