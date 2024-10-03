class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        n = len(nums)
        s = sum(nums)
        need_to_remove = s % p
        if need_to_remove == 0:
            return 0
        elif s < p:
            return -1

        mod_map = {0: -1}  # mod_sum -> ind_last_meet
        cur = 0
        res = n

        for right in range(n):
            cur = (cur + nums[right]) % p
            allowed_end_left_subarr = (cur - need_to_remove) % p

            if allowed_end_left_subarr in mod_map:
                # count from the next el after allowed up to this el
                res = min(res, right - mod_map[allowed_end_left_subarr])
            mod_map[cur] = right

        return res if res != n else -1
