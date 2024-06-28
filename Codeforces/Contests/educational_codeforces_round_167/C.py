t = int(input())

res = []
for _ in range(t):
    n = int(input())
    first_movie = input().split()
    second_movie = input().split()
    disliked_both = 0
    liked_both = 0
    first_movie_rating = 0
    second_movie_rating = 0

    for ind in range(n):
        f = int(first_movie[ind])
        s = int(second_movie[ind])

        if f in [0, -1] and s == 1:
            second_movie_rating += 1
        elif f == -1 and s == -1:
            disliked_both += 1
        elif f == 1 and s == 1:
            liked_both += 1
        elif f == 1 and s in [0, -1]:
            first_movie_rating += 1

    while disliked_both != 0:
        mx = max(first_movie_rating, second_movie_rating)
        if first_movie_rating == mx:
            first_movie_rating -= 1
        else:
            second_movie_rating -= 1
        disliked_both -= 1

    while liked_both != 0:
        mn = min(first_movie_rating, second_movie_rating)
        if mn == first_movie_rating:
            first_movie_rating += 1
        else:
            second_movie_rating += 1
        liked_both -= 1

    res.append(min(first_movie_rating, second_movie_rating))

for i in res:
    print(i)
