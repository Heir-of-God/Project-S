class Solution:
    def rotateTheBox(self, box: list[list[str]]) -> list[list[str]]:
        rows: int = len(box)
        cols: int = len(box[0])

        for row in range(rows):
            place: int = cols - 1
            for col in range(cols - 1, -1, -1):
                if box[row][col] == "*":
                    place = col
                elif box[row][col] == "#":
                    box[row][col] = "."
                    while box[row][place] != ".":
                        place -= 1
                    box[row][place] = "#"

        box = [row[::-1] for row in zip(*box)]
        return box
