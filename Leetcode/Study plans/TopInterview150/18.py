class Solution:
    def intToRoman(self, num: int) -> str:
        romans: list[list] = [
            ["I", 1],
            ["IV", 4],
            ["V", 5],
            ["IX", 9],
            ["X", 10],
            ["XL", 40],
            ["L", 50],
            ["XC", 90],
            ["C", 100],
            ["CD", 400],
            ["D", 500],
            ["CM", 900],
            ["M", 1000],
        ]
        cur_ind: int = len(romans) - 1
        res: str = ""
        while num != 0:
            while num < romans[cur_ind][1] and cur_ind != 0:
                cur_ind -= 1
            res += romans[cur_ind][0]
            num -= romans[cur_ind][1]

        return res
