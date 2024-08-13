class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        n: int = len(candidates)
        cur_combination: list[int] = []
        candidates.sort()

        def recursion(cur_ind: int, cur_sum: int) -> list[list[int]]:
            nonlocal cur_combination

            if cur_sum == target:
                return [cur_combination[:]]
            if cur_ind >= n:
                return []

            prev: int = -1
            local_res: list[list[int]] = []
            for nxt_ind in range(cur_ind, n, 1):
                el: int = candidates[nxt_ind]
                if cur_sum + el > target:
                    break
                if el == prev:
                    continue
                # pick
                cur_combination.append(el)
                output: list[list[int]] = recursion(nxt_ind + 1, cur_sum + el)
                for lst in output:
                    local_res.append(lst)
                cur_combination.pop()
                prev = el

            return local_res

        return recursion(0, 0)
