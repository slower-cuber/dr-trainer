from collections import defaultdict
from twophase import cubie

from src.move import move_cubie


HTR_MOVES_SET = [
    ["U2"],
    ["R2"],
    ["F2"],
    ["U2", "R2"],
    ["R2", "U2"],
    ["U2", "F2"],
    ["F2", "U2"],
    ["R2", "F2"],
    ["F2", "R2"],
    ["U2", "R2", "U2"],
    ["U2", "F2", "U2"],
    ["U2", "R2", "F2"],
    ["U2", "F2", "R2"],
    ["R2", "F2", "U2"],
    ["F2", "R2", "U2"],
    ["R2", "U2", "F2"],
    ["F2", "U2", "R2"],
    ["F2", "R2", "F2"],
    ["U2", "R2", "F2", "U2"],
    ["U2", "F2", "R2", "U2"],
    ["F2", "U2", "R2", "U2"],
    ["R2", "U2", "F2", "U2"],
    ["F2", "R2", "F2", "U2"],
]


moves_set_of_depth = defaultdict(list)
cp2moves = dict()


def bfs_htr(depth: int):
    if depth == 0:
        for htr_moves in HTR_MOVES_SET:
            c = cubie.CubieCube()
            move_cubie(c, htr_moves)
            cp = c.get_corners()
            if cp not in cp2moves:
                cp2moves[cp] = htr_moves
        moves_set_of_depth[0] = list(cp2moves.values())


bfs_htr(0)
print(moves_set_of_depth)
print(len(cp2moves))

