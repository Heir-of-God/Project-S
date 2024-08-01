class Solution:
    def countSeniors(self, details: list[str]) -> int:
        res: int = 0
        for detail in details:
            age: str = detail[11:13]
            if int(age) > 60:
                res += 1

        return res
