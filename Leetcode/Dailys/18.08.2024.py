class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res: list[int] = [1]
        cur_ind2 = 0
        cur_ind3 = 0
        cur_ind5 = 0

        while len(res) != n:
            two, three, five = res[cur_ind2] * 2, res[cur_ind3] * 3, res[cur_ind5] * 5
            if two == three or two == five:
                cur_ind2 += 1
                continue
            elif five == three:
                cur_ind3 += 1
                continue

            if two < three and two < five:
                res.append(two)
                cur_ind2 += 1
            elif three < two and three < five:
                res.append(three)
                cur_ind3 += 1
            elif five < two and five < three:
                res.append(five)
                cur_ind5 += 1
        return res[-1]
