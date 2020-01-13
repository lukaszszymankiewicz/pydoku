import numpy as np
import time

class Axis:
    row = 1
    column = 0
    number = 2


class Possibles:
    def __init__(self, sudoku):
        self.side = sudoku.shape[0]
        self.square_size = np.sqrt(self.side).astype(np.int)
        self.array = np.mgrid[1: self.side + 1, 1: self.side + 1, 1: self.side + 1][2]
        self.cube_size = (self.side, self.side, self.side)
        self.squerify_size = self.side, self.square_size, self.square_size, self.side
        self.unsquerify_size = self.square_size, self.side, self.square_size, self.side

    def squerify(self):
        self.array = self.array.reshape(self.squerify_size).swapaxes(0, 1).reshape(self.cube_size)

    def resquerify(self):
        self.array = self.array.reshape(self.unsquerify_size).swapaxes(0, 1).reshape(self.cube_size)

    def cross_out_all_numbers_from_position(self, nonzeros):
        self.array[nonzeros.columns, nonzeros.rows, :] = 0

    def cross_out_numbers_from_columns(self, nonzeros):
        self.array[nonzeros.columns, :, nonzeros.numbers] = 0

    def cross_out_numbers_from_rows(self, nonzeros):
        self.array[:, nonzeros.rows, nonzeros.numbers] = 0

    def cross_out_numbers_from_squares(self, nonzeros):
        self.squerify()
        self.array[nonzeros.squares, :, nonzeros.numbers] = 0
        self.resquerify()

    def lonely_numbers(self, axis):
        mask = (self.array != 0).sum(axis=axis, keepdims=True) > 1
        return np.where(mask, 0, self.array).sum(axis=2)


class NonzeroNumbers:
    def __init__(self, sudoku):
        self.indices = np.nonzero(sudoku.array)
        self.nonzero_numbers = sudoku.array[self.indices] - 1
        self.square_size = np.sqrt(sudoku.array.shape[0]).astype(int)

    @property
    def rows(self):
        return self.indices[1]

    @property
    def columns(self):
        return self.indices[0]

    @property
    def numbers(self):
        return self.nonzero_numbers

    @property
    def squares(self):
        return self.columns // self.square_size + self.rows // self.square_size * self.square_size


class Sudoku:
    def __init__(self, array):
        self.array = array

    @property
    def is_not_solved(self):
        return 0 in self.array

    def add_numbers(self, numbers):
        self.array |= numbers


def solve(array: np.ndarray):
    possibles = Possibles(array)
    sudoku = Sudoku(array)
    st = time.time()

    while sudoku.is_not_solved:
        nonzeros = NonzeroNumbers(sudoku)

        possibles.cross_out_all_numbers_from_position(nonzeros)
        possibles.cross_out_numbers_from_columns(nonzeros)
        possibles.cross_out_numbers_from_rows(nonzeros)
        possibles.cross_out_numbers_from_squares(nonzeros)

        sudoku.add_numbers(possibles.lonely_numbers(Axis.number))
        sudoku.add_numbers(possibles.lonely_numbers(Axis.row))
        sudoku.add_numbers(possibles.lonely_numbers(Axis.column))
    end = time.time()
    print(f"Solving sudoku took: {end-st} s.")
    return sudoku.array
