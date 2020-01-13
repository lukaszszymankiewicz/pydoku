import time

import numpy as np

side, sqr = 9, 3


def squerify(array):
    return array.reshape(side, sqr, sqr, side).swapaxes(0, 1).reshape(side, side, side)


def resquerify(array):
    return array.reshape(sqr, side, sqr, side).swapaxes(0, 1).reshape(side, side, side)


def find_lonely_numbers(array, axis):
    mask = (array != 0).sum(axis=axis, keepdims=True) > 1
    return np.where(mask, 0, array)


def solve(sudoku: np.ndarray):
    st = time.time()
    possibles = np.mgrid[1: side + 1, 1: side + 1, 1: side + 1][2]

    while 0 in sudoku:
        idx = np.nonzero(sudoku)
        numbers = sudoku[idx] - 1

        possibles[idx[0], idx[1], :] = 0
        possibles[:, idx[1], numbers] = 0
        possibles[idx[0], :, numbers] = 0

        sudoku |= (find_lonely_numbers(array=possibles, axis=2).sum(axis=2))
        sudoku |= (find_lonely_numbers(array=possibles, axis=1).sum(axis=2))
        sudoku |= (find_lonely_numbers(array=possibles, axis=0).sum(axis=2))

        possibles_sq = squerify(possibles)
        possibles_sq[idx[0] // sqr + idx[1] // sqr * sqr, :, numbers] = 0
        possibles = resquerify(possibles_sq)

        sudoku |= (find_lonely_numbers(array=possibles, axis=1).sum(axis=2))
    end = time.time()
    print(sudoku)
    print(f"Solving sudoku took: {end - st} s.")
