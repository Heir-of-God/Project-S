n, k = input().split()
n = int(n)
k = int(k)
scores = [int(i) for i in input().split()]

first_ind_smaller = k - 1
minimum_required = scores[first_ind_smaller]

while first_ind_smaller != 0 and scores[first_ind_smaller - 1] == 0:
    first_ind_smaller -= 1

while first_ind_smaller < n and scores[first_ind_smaller] != 0 and scores[first_ind_smaller] == minimum_required:
    first_ind_smaller += 1

print(first_ind_smaller if first_ind_smaller != -1 else 0)
