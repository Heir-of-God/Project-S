class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        def binary_search(val) -> int:
            left: int = 0
            right: int = len(cur_lis) - 1
            res: int = -1

            while left <= right:
                mid: int = (left + right) // 2
                mid_el: int = cur_lis[mid]

                if mid_el >= val:
                    res = mid
                    right = mid - 1
                else:
                    left = mid + 1

            return res

        cur_lis: list[int] = []

        for el in nums:
            if not cur_lis or cur_lis[-1] < el:
                cur_lis.append(el)
            else:
                to_replace: int = binary_search(el)
                cur_lis[to_replace] = el

        return len(cur_lis)
