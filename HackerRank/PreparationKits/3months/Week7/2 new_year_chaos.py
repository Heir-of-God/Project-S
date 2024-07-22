def minimumBribes(q: list[int]) -> None:

    def find_how_many_need_to_swap_with_me(n, sorted_list) -> int:
        need_to_swap = 0
        for number in sorted_list:
            if number < n:
                need_to_swap += 1
            else:
                break
        return need_to_swap

    res = 0
    sorted_queue: list[int] = sorted(q)
    for person in q:
        sorted_queue.remove(person)
        overtaken: int = find_how_many_need_to_swap_with_me(person, sorted_queue)
        if overtaken > 2:
            print("Too chaotic")
            return
        res += overtaken
    print(res)


if __name__ == "__main__":
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)
