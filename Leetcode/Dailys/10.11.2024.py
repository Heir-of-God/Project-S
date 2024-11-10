class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        bits_counter: list[int] = [0 for _ in range(30)]  # 10^9 < 2^30
        cur_number: int = 0
        left: int = 0
        res: int = float("inf")

        for right, num in enumerate(nums):
            pos = 0
            cur_number |= num

            while num > 0:
                bits_counter[pos] += num & 1
                num >>= 1
                pos += 1

            while cur_number >= k and left <= right:
                res = min(res, right - left + 1)

                left_num: int = nums[left]
                pos = 0
                while left_num > 0:
                    if left_num & 1:
                        bits_counter[pos] -= 1
                        if bits_counter[pos] == 0:
                            cur_number ^= 1 << pos
                    left_num >>= 1
                    pos += 1
                left += 1

        return res if res != float("inf") else -1
