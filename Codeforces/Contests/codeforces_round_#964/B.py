t = int(input())

for _ in range(t):
    a, b, c, d = [int(i) for i in input().split()]
    ab = a + b
    cd = c + d
    res = 0

    for first_suneet_card in (a, b):
        second_seneet_card = ab - first_suneet_card
        for first_slavik_card in (c, d):
            second_slavik_card = cd - first_slavik_card
            if (
                (first_suneet_card > first_slavik_card and second_seneet_card > second_slavik_card)
                or (first_suneet_card == first_slavik_card and second_seneet_card > second_slavik_card)
                or (first_suneet_card > first_slavik_card and second_seneet_card == second_slavik_card)
            ):
                res += 1

    print(res)
