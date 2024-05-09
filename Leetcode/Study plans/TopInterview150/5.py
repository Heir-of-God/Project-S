class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        cur_maj: int = None
        cur_count = 0

        for num in nums:
            if cur_count == 0:
                cur_maj = num
            cur_count += 1 if num == cur_maj else -1

        return cur_maj


# using https://www.geeksforgeeks.org/boyer-moore-majority-voting-algorithm/
