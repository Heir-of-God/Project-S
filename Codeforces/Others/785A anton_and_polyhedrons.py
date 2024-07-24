res = 0
mapping = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20,
}
n = int(input())

for _ in range(n):
    res += mapping[input()]

print(res)
