class Solution:
    def countTriplets(self, nums: list[int]) -> int:
        n: int = len(nums)
        count_elems = defaultdict(int)
        count_and_for_two = defaultdict(int)

        for ind1 in range(n):
            el1: int = nums[ind1]
            count_elems[el1] += 1

            for ind2 in range(n):
                el2: int = nums[ind2]
                val: int = el1 & el2
                count_and_for_two[val] += 1

        res = 0
        for el, count_el in count_elems.items():
            for double, count_double in count_and_for_two.items():
                if el & double == 0:
                    res += count_el * count_double

        return res
