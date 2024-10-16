from heapq import heapify, heappop, heappush


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [[-a, "a"], [-b, "b"], [-c, "c"]]
        heapify(heap)
        res = ""

        while heap and heap[0][0] != 0:
            count, char = heappop(heap)
            count *= -1
            if len(res) >= 2 and res[-1] == res[-2] == char:
                if not heap or heap[0][0] == 0:
                    break
                nxt_count, nxt_char = heappop(heap)
                nxt_count *= -1
                res += nxt_char
                heappush(heap, [-(nxt_count - 1), nxt_char])
                heappush(heap, [-count, char])
            else:
                res += char
                count -= 1
                heappush(heap, [-count, char])

        return res
