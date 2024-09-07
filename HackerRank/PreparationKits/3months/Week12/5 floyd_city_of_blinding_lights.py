if __name__ == "__main__":
    road_nodes, road_edges = map(int, input().rstrip().split())
    matrix: list[list[float]] = [[float("inf") for _ in range(road_nodes + 1)] for _ in range(road_nodes + 1)]

    for node in range(1, road_nodes + 1, 1):
        matrix[node][node] = 0

    for i in range(road_edges):
        src, dest, weight = map(int, input().rstrip().split())
        matrix[src][dest] = weight

    for middle in range(1, road_nodes + 1, 1):
        for source in range(1, road_nodes + 1, 1):
            for dest in range(1, road_nodes + 1, 1):
                if matrix[source][middle] + matrix[middle][dest] < matrix[source][dest]:
                    matrix[source][dest] = matrix[source][middle] + matrix[middle][dest]

    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input: list[str] = input().rstrip().split()
        x = int(first_multiple_input[0])
        y = int(first_multiple_input[1])
        print(matrix[x][y] if matrix[x][y] != float("inf") else -1)
