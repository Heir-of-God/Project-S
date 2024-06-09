class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        n: int = len(nums)
        nums[0] %= k
        for ind in range(1, n):
            nums[ind] = (nums[ind - 1] + nums[ind]) % k

        res = 0
        count_seen: dict[int, int] = {}
        count_seen[0] = 1  # From start we don't have any sum

        for num in nums:
            if num in count_seen:
                res += count_seen[num]
            count_seen[num] = count_seen.get(num, 0) + 1

        return res
