class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if not len(hand) % groupSize == 0:
            return False
        freq: dict[int, int] = {}
        unique: list[int] = []
        for card in hand:
            if not card in freq:
                freq[card] = 0
                unique.append(card)
            freq[card] += 1

        unique.sort()
        cur_ind = 0
        while cur_ind != len(unique):
            cur_start: int = unique[cur_ind]
            if freq[cur_start] == 0:
                cur_ind += 1
            else:
                for n in range(cur_start, cur_start + groupSize, 1):
                    if not n in freq or freq[n] == 0:
                        return False
                    freq[n] -= 1

        return True
