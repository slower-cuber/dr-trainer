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
        if m:
            c.multiply(
                cubie.moveCube[STR_2_MOVE[m]]
            )


# TODO: cancel more than 1 pair of moves
def concat_moves(moves_1: list, moves_2: list):
    def _get_qt(move_word):
        qt = 0
        if len(move_word) == 1:
            qt = 1
        elif move_word[1] == "2":
            qt = 2
        elif move_word[1] == "'":
            qt = 3
        return qt

    if not moves_1:
        return moves_2
    if not moves_2:
        return moves_1

    former_tail = moves_1[-1]
    latter_head = moves_2[0]
    if former_tail[0] != latter_head[0]:
        return moves_1 + moves_2

    sum_qt = (_get_qt(former_tail) + _get_qt(latter_head)) % 4
    if sum_qt == 0:
        return moves_1[:-1] + moves_2[1:]
    else:
        if sum_qt == 1:
            qt_suffix = ""
        elif sum_qt == 2:
            qt_suffix = "2"
        else:
            qt_suffix = "'"

        combined_move = former_tail[0] + qt_suffix

        return moves_1[:-1] + [combined_move] + moves_2[1:]


def inverse_move_string(move_string: str) -> List:
    moves = [t for t in move_string.split(' ') if t]
    for m in reversed(moves):
        if len(m) == 1 or m[1] == '1':
            yield m[0] + "'"
        elif m[1] == '3' or m[1] == "'":
            yield m[0]
        else:
            yield m


if __name__ == '__main__':
    print(concat_moves(["R", "U"], ["R'", "U'"]))
    print(concat_moves(["R", "U"], ["U'", "R'"]))
    print(concat_moves(["R", "U2"], ["U2", "R'"]))
    print(concat_moves(["R", "U'"], ["U", "R'"]))
    print(concat_moves(["R", "U'"], ["U'", "R'"]))
    print(concat_moves(["R", "U2"], ["U'", "R'"]))
    print(concat_moves(["R", "U2"], ["U", "R'"]))
