class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        n: int = len(books)
        cache: list[int] = [
            float("inf") for _ in range(n + 1)
        ]  # cache[ind] means you need cache[ind] height to put all the books in the bookshelf from ind to n
        cache[n] = 0

        for ind in range(n - 1, -1, -1):
            shelf_width: int = shelfWidth
            shelf_height: int = 0

            add_book_ind: int = ind
            while add_book_ind < n and shelf_width >= books[add_book_ind][0]:
                shelf_width -= books[add_book_ind][0]
                shelf_height = max(shelf_height, books[add_book_ind][1])
                cache[ind] = min(cache[ind], cache[add_book_ind + 1] + shelf_height)
                add_book_ind += 1

        return cache[0]
