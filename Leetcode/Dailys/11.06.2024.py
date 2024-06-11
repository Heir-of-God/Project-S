class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        count_in_first: dict[int, int] = {}
        other_elements: list[int] = []
        for el in arr1:
            if el in arr2:
                if el not in count_in_first:
                    count_in_first[el] = 0
                count_in_first[el] += 1
            else:
                other_elements.append(el)

        res: list[int] = []
        for el in arr2:
            freq = count_in_first[el]
            for _ in range(freq):
                res.append(el)
        res += sorted(other_elements)
        return res
