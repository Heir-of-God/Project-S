class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        n: int = len(events)
        events.sort()
        suffix_maxes: list[int] = []
        mx: int = 0
        for _, _, val in events[::-1]:
            mx = max(mx, val)
            suffix_maxes.append(mx)
        suffix_maxes.reverse()

        res: int = 0
        for ind in range(n):
            res = max(res, events[ind][2])
            left: int = ind + 1
            right: int = n - 1

            while left < right:
                mid: int = left + (right - left) // 2

                if events[mid][0] > events[ind][1]:
                    right = mid
                else:
                    left = mid + 1

            if left < n and events[left][0] > events[ind][1]:
                res = max(res, events[ind][2] + suffix_maxes[left])

        return res
