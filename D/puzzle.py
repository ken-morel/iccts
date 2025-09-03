"""
puzzle.py algorithm for creating a puzzle board from input words and size.
Works exclusively with upper case letters.

The matrixes used are in python's row-major format: [x][y].

Tried to op for a set of simple, single operating functions(abit julian, but easier documented).
"""

import random
from contextlib import contextmanager

try:
    import pyoload

    pyoload = pyoload.pyoload
except:
    pyoload = lambda f: f

A = ord("A")
Z = ord("Z")
N = chr(0)


randch = lambda: chr(random.randrange(A, Z + 1))


@pyoload
class Board(list):
    """
    The puzzle board class

    The board character(unit length string) matrix.
    A null character(`N`), represents an empty cell.


    :attr width: The board's width
    :attr height: The board's height
    """

    class CanNotPlace(Exception):
        """
        Raised when the required place could not be made.
        """

    width: int
    height: int

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        super().__init__([[N for _ in range(height)] for _ in range(width)])

    @contextmanager
    def reset_on_noplace(self):
        orig = [i.copy() for i in self.matrix]
        try:
            yield
        except Board.CanNotPlace:
            self.matrix = orig
        except:
            raise

    def placeword_horizontaly(self, word: str, x: int, y: int):
        for i in range(len(word)):
            self[x + i][y] = word[i]

    def placeword_verticaly(self, word: str, x: int, y: int):
        for i in range(len(word)):
            self[x][y + i] = word[i]

    def placeword_topwards(self, word: str, x: int, y: int):
        self.placeword_verticaly(word[::-1], x, y - len(word))

    def placeword_downwards(self, word: str, x: int, y: int):
        self.placeword_verticaly(word, x, y)

    def placeword_leftwards(self, word: str, x: int, y: int):
        self.placeword_horizontaly(word[::-1], x - len(word), y)

    def placeword_rightwards(self, word: str, x: int, y: int):
        self.placeword_horizontaly(word, x, y)

    def textify(self) -> str:
        text = ""
        for y in range(self.height):
            for x in range(self.width):
                ch = self[x][y]
                text += " " if ch == N else ch
            text += "\n"
        return text


def main():
    test_words = list(map(str.upper, ["banana", "orange", "blue", "purple"]))
    board = Board(10, 10)
    board.placeword_leftwards("banana".upper(), 9, 5)
    print(board.textify())


if __name__ == "__main__":
    main()
