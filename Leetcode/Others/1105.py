class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        n: int = len(books)
        dp: list[float] = [float("inf") for _ in range(n + 1)]  # dp[i] minimum height for first i books from books
        dp[0] = 0

        for number_of_books in range(1, n + 1, 1):
            shelf_height: int = 0
            shelf_width: int = shelfWidth

            cur_ind: int = number_of_books - 1
            while cur_ind >= 0 and shelf_width >= books[cur_ind][0]:
                shelf_width -= books[cur_ind][0]
                shelf_height = max(shelf_height, books[cur_ind][1])
                dp[number_of_books] = min(dp[number_of_books], dp[cur_ind] + shelf_height)
                cur_ind -= 1

        return dp[n]
