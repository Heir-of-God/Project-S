class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        events: list[list[int, int]] = []
        for ind, elems in enumerate(nums):
            for elem in elems:
                events.append([elem, ind])

        events.sort()
        res: list[int] = [-float("inf"), float("inf")]
        count: dict[int, int] = {i: 0 for i in range(len(nums))}
        intervals_covered = 0
        left = 0

        for right in range(len(events)):
            count[events[right][1]] += 1
            if count[events[right][1]] == 1:
                intervals_covered += 1

            while intervals_covered == len(nums):
                if events[right][0] - events[left][0] < res[1] - res[0]:
                    res = [events[left][0], events[right][0]]
                count[events[left][1]] -= 1
                if count[events[left][1]] == 0:
                    intervals_covered -= 1
                left += 1

        return res
