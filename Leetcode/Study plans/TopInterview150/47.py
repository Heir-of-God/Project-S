class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        uniques: set[int] = set(nums)
        max_length: int = 0

        while uniques:
            first_in_seq: int = uniques.pop()
            last_in_seq: int = first_in_seq

            while first_in_seq - 1 in uniques or last_in_seq + 1 in uniques:
                if first_in_seq - 1 in uniques:
                    uniques.remove(first_in_seq - 1)
                    first_in_seq -= 1

                if last_in_seq + 1 in uniques:
                    uniques.remove(last_in_seq + 1)
                    last_in_seq += 1

            max_length = max(last_in_seq - first_in_seq + 1, max_length)

        return max_length
