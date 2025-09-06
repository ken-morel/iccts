"""
puzzle.py algorithm for creating a puzzle board from input words and size.
Works exclusively with upper case letters.

The matrixes used are in python's row-major format: [x][y].

Tried to op for a set of simple, single operating functions(abit julian, but easier documented).
"""

import random
from contextlib import contextmanager
from types import FunctionType

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

    class CanNotwrite(Exception):
        """
        Raised when the required write could not be made.
        """

    class CanNotPlace(Exception):
        """
        Raised when the required word could not be found a place.
        """

    @classmethod
    def frommatrix(cls, matrix: list[list[str]]) -> "Board":
        """
        Create a board using the prepared matrix character data.
        """
        assert len(matrix) > 0, "Cannot use an empty matrix"
        board = Board(len(matrix), len(matrix[0]))
        board[:] = [m.copy() for m in matrix]  # make sure to make a real copy
        return board

    width: int
    height: int

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        super().__init__([[N for _ in range(height)] for _ in range(width)])

    @contextmanager
    def reset_on_noplace(self):
        """
        Hold and reset the board state if `Board.CanNotwrite` raised in context.

        A context manager which reset's the board to it's original state if
        `Board.CanNotwrite` is raised
        """
        orig = [i.copy() for i in self]
        try:
            yield
        except Board.CanNotPlace:
            self[:] = orig
        except:
            raise

    def writeword_horizontaly(self, word: str, x: int, y: int):
        """
        Attemp to write the `word` horizontaly starting at (x, y).
        """
        for i in range(len(word)):
            self[x + i][y] = word[i]

    def writeword_verticaly(self, word: str, x: int, y: int):
        """
        Attempt to write `word` vertically from (x, y) going downwards.
        """
        for i in range(len(word)):
            self[x][y + i] = word[i]

    def textify(self) -> str:
        """
        Represent the board as console-printable, simple plain text.
        """
        text = ""
        for y in range(self.height):
            for x in range(self.width):
                ch = self[x][y]
                text += " " if ch == N else ch
            text += "\n"
        return text

    def placeword_horizontaly(self, word: str):
        """
        Try to find a way to place the word horizontaly.

        This function places the word in the same sense it was
        passed, so reversing should be done prior to calling it.
        """
        words = [word, word[::-1]]
        random.shuffle(words)
        possible = [
            (x, y) for x in range(self.width - len(word)) for y in range(self.height)
        ]
        random.shuffle(possible)
        for x, y in possible:
            placed = False
            for word in words:
                if self.word_can_go_there_horizontaly(x, y, word):
                    self.writeword_horizontaly(word, x, y)
                    placed = True
                    break
            if placed:
                break
        else:
            raise Board.CanNotPlace(word, "horizontaly")

    def placeword_vertically(self, word: str):
        """
        Try to find a way to place the word verticaly downwards.

        This function places the word in the same sense it was
        passed but downwards, so reversing should be done prior to calling it.
        """
        words = [word, word[::-1]]
        random.shuffle(words)
        possible = [
            (x, y) for x in range(self.width) for y in range(self.height - len(word))
        ]
        random.shuffle(possible)
        for x, y in possible:
            placed = False
            for word in words:
                if self.word_can_go_there_verticaly(x, y, word):
                    self.writeword_verticaly(word, x, y)
                    placed = True
                    break
            if placed:
                break
        else:
            raise Board.CanNotPlace(word, "verticaly")

    def placeword(self, word: str):
        order = ["v", "h"]
        random.shuffle(order)
        error = None
        for o in order:
            try:
                (self.placeword_horizontaly if o == "h" else self.placeword_vertically)(
                    word
                )
            except Board.CanNotPlace as e:
                error = e
                continue
            else:
                break
        else:
            if error is not None:
                raise error
            else:
                raise Board.CanNotPlace(
                    "Details unexpectedly unvailable "
                    "Well, yeah, this is kinda a bug"
                    ". Sorry"
                )

    def word_can_go_there_horizontaly(self, x: int, y: int, word: str) -> bool:
        """
        Checks if the word can be written horizontaly from (x, y).

        It checks if the word passed can be written horizontaly
        rightwards from (x, y).
        """
        return all([self[x + i][y] in (word[i], N) for i in range(len(word))])

    def word_can_go_there_verticaly(self, x: int, y: int, word: str) -> bool:
        """
        Checks if the word can be written verticaly from (x, y).

        It checks if the word passed can be written verticaly
        downwards from (x, y).
        """
        return all([self[x][y + i] in (word[i], N) for i in range(len(word))])

    def fill_empty_spaces(self):
        """
        Fills empty spaces in the board.
        replace the empty spaces(equal to `N`) with a random uppercase english letter.
        """
        for x in range(self.width):
            for y in range(self.height):
                if self[x][y] == N:
                    self[x][y] = randch()


def create_crossward(words: list[str]) -> list[list[str]]:
    """
    This is the function asked in the excersice it creates a board,
    places the words in it, then return the board.
    The placement algorithm was made in such away to permit words
    to be place horizontaly, verticaly, in forward or backward
    directions, and with crosswards. It does not implement an
    re-organisation algorithm to replace previously placed letters
    very efficiently yet, but the random works fine with several iterations.
    :arg words: The
    """
    words[:] = [word[:10].upper() for word in words]  # in place updating of words
    board = Board(10, 10)
    for _ in range(1000):  # try several random placements, reduce error risks
        random.shuffle(words)  # why just am I doing this? :D
        with board.reset_on_noplace():  # to original state if placing fails
            for word in words:
                board.placeword(word)
            board.fill_empty_spaces()
            return list(
                board
            )  # board is already an instance of list, but just in case.
    raise Board.CanNotPlace(
        "Sorry, the words could not be efficiently placed."
        "May be placing several words get's not so easy"
    )


def test():
    test_words = list(
        map(
            str.upper,
            [
                "banana",
                "orange",
                "blue",
                "purple",
                "ken-morel",
                "ama",
                "upper",
                "sixth",
                "julia",
                "language",
                "python",
                "bad",
            ],
        )
    )
    board = create_crossward(test_words)
    print(Board.frommatrix(board).textify())  # sorry lsp
    print("To make it easy, try to locate ken-morel (look for the hyphen)")
    print("The hidden words are")
    [print(f" - {w}") for w in test_words]


if __name__ == "__main__":
    test()
