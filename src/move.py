from typing import List, Union

from twophase import cubie
from twophase.enums import Move

STR_2_MOVE = {
    "U": Move.U1, "U2": Move.U2, "U'": Move.U3,
    "R": Move.R1, "R2": Move.R2, "R'": Move.R3,
    "F": Move.F1, "F2": Move.F2, "F'": Move.F3,
    "D": Move.D1, "D2": Move.D2, "D'": Move.D3,
    "L": Move.L1, "L2": Move.L2, "L'": Move.L3,
    "B": Move.B1, "B2": Move.B2, "B'": Move.B3,
}


def move_cubie(c: cubie.CubieCube, moves: Union[str, list]):
    if isinstance(moves, list):
        _moves = moves
    elif isinstance(moves, str):
        _moves = moves.split(" ")
    else:
        raise ValueError("moves is either one string or a list of moves")

    for m in _moves:
        m = m.strip()
        c.multiply(
            cubie.moveCube[STR_2_MOVE[m]]
        )


def inverse_move_string(move_string: str) -> List:
    moves = [t for t in move_string.split(' ') if t]
    for m in reversed(moves):
        if len(m) == 1 or m[1] == '1':
            yield m[0] + "'"
        elif m[1] == '3' or m[1] == "'":
            yield m[0]
        else:
            yield m
