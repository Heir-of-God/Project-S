class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        start: int = False
        prev: int = False
        res: list[str] = []
        if nums:
            nums.append(nums[-1] + 2)

        for num in nums:
            if start is False:
                start = num
            elif num - prev != 1:
                res.append(f"{start}->{prev}" if start != prev else str(start))
                start = num

            prev = num

        return res
