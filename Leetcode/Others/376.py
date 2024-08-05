class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        n: int = len(nums)
        difs: list[int] = [nums[i] - nums[i - 1] for i in range(1, n) if nums[i] - nums[i - 1] != 0]
        if not difs:
            return 1

        res = 2
        for dif_ind in range(1, len(difs), 1):
            res += (difs[dif_ind] > 0 and difs[dif_ind - 1] < 0) or (difs[dif_ind] < 0 and difs[dif_ind - 1] > 0)

        return res


class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        n: int = len(nums)
        prev_up: int = 1  # up to this index when last dif was > 0
        prev_down: int = 1  # up to this index when last dif was < 0

        for ind in range(1, n, 1):
            dif: int = nums[ind] - nums[ind - 1]
            if dif == 0:
                continue
            isup: bool = dif > 0
            if isup:
                prev_up = prev_down + 1
            else:
                prev_down = prev_up + 1

        return max(prev_up, prev_down)
