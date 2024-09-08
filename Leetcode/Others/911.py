class TopVotedCandidate:

    def __init__(self, persons: list[int], times: list[int]):
        self.res: list[int] = []
        cur_winner = -1
        count: dict[int, int] = {-1: -1}
        for vote in persons:
            if vote not in count:
                count[vote] = 0
            count[vote] += 1
            if count[vote] >= count[cur_winner]:
                cur_winner = vote
            self.res.append(cur_winner)
        self.times: list[int] = times

    def _binary_search(self, time: int):
        left: int = 0
        right: int = len(self.times) - 1
        res: int = -1
        while left <= right:
            mid: int = (left + right) // 2
            if self.times[mid] <= time:
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res

    def q(self, t: int) -> int:
        return self.res[self._binary_search(t)]
