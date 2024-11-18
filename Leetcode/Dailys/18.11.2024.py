class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n: int = len(code)
        flip: bool = False
        if k < 0:
            k *= -1
            code.reverse()
            flip = True
        elif k == 0:
            return [0 for _ in range(n)]

        res: list[int] = []
        cur_sm = 0
        for ind in range(1, n + k, 1):
            cur_sm += code[ind % n]

            if ind >= k:
                res.append(cur_sm)
                cur_sm -= code[(ind - k + 1) % n]

        if flip:
            res.reverse()

        return res
