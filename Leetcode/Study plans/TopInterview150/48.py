class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res: list[str] = []
        cur_range: list[int] = []
        if nums:
            nums.append(nums[-1])

        for n in nums:
            if not cur_range or n - cur_range[-1] == 1:
                cur_range.append(n)
            else:
                if len(cur_range) != 1:
                    res.append(f"{cur_range[0]}->{cur_range[-1]}")
                else:
                    res.append(str(cur_range[0]))
                cur_range = [n]

        return res
