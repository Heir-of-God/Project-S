class Solution:
    def fractionAddition(self, expression: str) -> str:
        def gcd(num1, num2) -> int:
            if num2 == 0:
                return num1
            return gcd(num2, num1 % num2)

        if expression[0] != "-":
            expression = "+" + expression
        n: int = len(expression)
        fractions: list[list[int]] = []
        start_ind: int = n - 1
        for ind in range(n - 1, -1, -1):
            char: str = expression[ind]
            if char in "+-":
                fractions.append(expression[ind : start_ind + 1])
                start_ind = ind - 1

        fractions = [list(map(int, frac.split("/"))) for frac in fractions]
        common_denomitor: int = 1
        for _, denominator in fractions:
            common_denomitor *= denominator // gcd(common_denomitor, denominator)

        nom = 0
        for nomitor, denominator in fractions:
            nom += nomitor * (common_denomitor // denominator)

        common: int = gcd(abs(nom), common_denomitor)
        nom //= common
        common_denomitor //= common
        res: str = f"{nom}/{common_denomitor}"

        return res
