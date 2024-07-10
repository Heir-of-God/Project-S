year = int(input()) + 1


def is_only_distinct(year):
    year = str(year)
    seen = set()

    for char in year:
        if char in seen:
            return False
        seen.add(char)

    return True


while not is_only_distinct(year):
    year += 1

print(year)
