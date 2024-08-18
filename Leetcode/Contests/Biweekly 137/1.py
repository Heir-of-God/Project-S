class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        if k == 1:
            return nums
        n: int = len(nums)
        res: list[int] = []
        last_start: int = 0
        ind = 1

        while ind < k:
            prev: int = nums[ind - 1]
            if nums[ind] - prev != 1:
                last_start = ind
            ind += 1

        if last_start == 0:
            res.append(nums[k - 1])
            last_start += 1
        else:
            res.append(-1)

        while ind < n:
            prev_el: int = nums[ind - 1]
            cur_el: int = nums[ind]

            if cur_el - prev_el == 1 and ind - last_start + 1 == k:
                res.append(cur_el)
                last_start += 1
            else:
                if cur_el - prev_el != 1:
                    last_start = ind
                res.append(-1)
            ind += 1

        return res
