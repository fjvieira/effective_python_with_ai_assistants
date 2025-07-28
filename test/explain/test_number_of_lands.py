from src.explain.number_of_lands import find_number_of_lands
import pytest


def test_empty_map():
    assert find_number_of_lands(
        None,
        [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]) == 0


def test_full_map():
    assert find_number_of_lands(
        None,
        [[1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1]]) == 1


def test_not_continuous_diagonal_land():
    assert find_number_of_lands(
        None,
        [[1, 0, 0, 0, 0],
         [0, 1, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 1, 1]]) == 4


def test_alternating_horizontal_land():
    assert find_number_of_lands(
        None,
        [[0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1]]) == 2

    assert find_number_of_lands(
        None,
        [[1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0]]) == 2


def test_chessboard_land():
    assert find_number_of_lands(
        None,
        [[0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0]]) == 32

    assert find_number_of_lands(
        None,
        [[1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1]]) == 32


def test_u_shaped_land():
    assert find_number_of_lands(
        None,
        [[1, 0, 1],
         [1, 1, 1]]) == 1
