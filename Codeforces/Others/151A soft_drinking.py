friends, bottles, millimiters, limes, slices, salt, need_ml, need_salt = [int(i) for i in input().split()]

print(min([bottles * millimiters // need_ml, limes * slices, salt // need_salt]) // friends)
