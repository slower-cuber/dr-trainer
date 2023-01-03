from collections import defaultdict
from twophase import cubie

from src.move import move_cubie, concat_moves


HTR_MOVES_SET = [
    [],
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
                moves_set_of_depth[0].append(htr_moves)
        #moves_set_of_depth[0] = list(cp2moves.values())
    else:
        for base_moves in moves_set_of_depth[depth-1]:
            for u_moves in [["U"], ["U'"]]:
                for htr_moves in HTR_MOVES_SET:
                    moves = concat_moves(base_moves, u_moves)
                    moves = concat_moves(moves, htr_moves)
                    c = cubie.CubieCube()
                    move_cubie(c, moves)
                    cp = c.get_corners()
                    if cp not in cp2moves:
                        cp2moves[cp] = moves
                        moves_set_of_depth[depth].append(moves)



bfs_htr(0)
print(moves_set_of_depth)
print(len(cp2moves))

bfs_htr(1)
print(moves_set_of_depth)
print(len(cp2moves))

bfs_htr(2)
print(len(cp2moves))

bfs_htr(3)
print(len(cp2moves))

bfs_htr(4)
print(len(cp2moves))

bfs_htr(5)
print(len(cp2moves))

bfs_htr(6)
print(len(cp2moves))
