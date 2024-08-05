class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        counter = defaultdict(int)
        stack: list[int] = []

        for string in arr:
            if string not in counter:
                stack.append(string)
            counter[string] += 1

        distinct_count = 0
        for string in stack:
            if counter[string] == 1:
                distinct_count += 1
            if distinct_count == k:
                return string

        return ""
