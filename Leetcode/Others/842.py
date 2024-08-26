class Solution:
    def splitIntoFibonacci(self, num: str) -> list[int]:
        n: int = len(num)
        cur: list[int] = []

        def recursion(cur_ind) -> bool:
            nonlocal cur

            if cur_ind == n and len(cur) >= 3:
                return True

            for ind in range(cur_ind, min(cur_ind + 10, n), 1):
                part = int(num[cur_ind : ind + 1])
                if len(cur) < 2 or cur[-1] + cur[-2] == part and part < 2**31:
                    cur.append(part)
                    if recursion(ind + 1):
                        return True
                    cur.pop()
                if ind == cur_ind and num[ind] == "0":
                    break

            return False

        recursion(0)
        return cur
