# Enter your code here. Read input from STDIN. Print output to STDOUT
n, q = [int(i) for i in input().split()]
representatives = [i for i in range(n + 1)]
graph_sizes = [1 for _ in range(n + 1)]


def get_represantative(person):
    while person != representatives[person]:
        representatives[person], person = representatives[representatives[person]], representatives[person]
    return person


def get_rank(person):
    return graph_sizes[get_represantative(person)]


def merge(person1, person2):
    person1 = get_represantative(person1)
    person2 = get_represantative(person2)
    if person1 == person2:
        return

    if graph_sizes[person1] >= graph_sizes[person2]:
        graph_sizes[person1] += graph_sizes[person2]
        representatives[person2] = person1
    else:
        graph_sizes[person2] += graph_sizes[person1]
        representatives[person1] = person2


for _ in range(q):
    inp = input()
    if inp[0] == "M":
        _, p1, p2 = inp.split()
        merge(int(p1), int(p2))
    elif inp[0] == "Q":
        _, p = inp.split()
        print(get_rank(int(p)))
