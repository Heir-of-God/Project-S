from typing import Counter


class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = Counter(num)

        res: list[str] = []
        mx_odd: str = ""
        for digit, cnt in sorted(count.items(), reverse=True):  # sorting takes O(1) cause len(count) <= 10
            for _ in range(cnt // 2):
                res.append(digit)
            if cnt & 1 == 1 and not mx_odd:
                mx_odd = digit

        if res and res[0] == "0":
            res.clear()

        second_half = reversed(res)
        if mx_odd:
            res.append(mx_odd)
        res += second_half

        return "".join(res) if res else max(count)
