import heapq

queries = int(input())
heap: list[int] = []
for _ in range(queries):
    inp: list[str] = input().split()
    if inp[0] == "1":
        heapq.heappush(heap, int(inp[1]))
    elif inp[0] == "2":
        ind: int = heap.index(int(inp[1]))
        heap[ind] = heap[-1]
        heap.pop()
        if heap:
            heapq._siftup(heap, min(ind, len(heap) - 1))
    else:
        print(heap[0])
