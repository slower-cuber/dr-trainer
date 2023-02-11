import pickle
from collections import defaultdict
from typing import Union

from twophase import cubie
from twophase.enums import Color
from twophase.face import FaceCube

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


def save_htr_cubie():
    for qtm, moves_set in moves_set_of_depth.items():
        corner_cases = []
        for moves in moves_set:
            c = cubie.CubieCube()
            move_cubie(c, moves)
            corner_cases.append((moves,c))
        with open(f"corner_case_{qtm}.pkl", "wb") as f:
            pickle.dump(corner_cases, f)


def build_corner_cases():
    bfs_htr(0)
    print(len(cp2moves))
    bfs_htr(1)
    print(len(cp2moves))
    bfs_htr(2)
    print(len(cp2moves))
    bfs_htr(3)
    print(len(cp2moves))
    bfs_htr(4)
    print(len(cp2moves))
    bfs_htr(5)
    print(len(cp2moves))
    save_htr_cubie()


def get_stickers(cube: Union[cubie.CubieCube, FaceCube]):
    if isinstance(cube, cubie.CubieCube):
        fb: FaceCube = cube.to_facelet_cube()
    else:
        fb: FaceCube = cube

    return {
        "up": (fb.f[0], fb.f[2], fb.f[8], fb.f[6]),
        "up_side": (fb.f[36], fb.f[47], fb.f[45], fb.f[11], fb.f[9], fb.f[20], fb.f[18], fb.f[38]),
        "down": (fb.f[27], fb.f[29], fb.f[35], fb.f[33]),
        "down_side": (fb.f[44], fb.f[24], fb.f[26], fb.f[15], fb.f[17], fb.f[51], fb.f[53], fb.f[42])
    }


def expanded_sticker_circles(ud_stickers, side_stickers):
    _u = ud_stickers
    _s = side_stickers
    return [
        [(_u[0], _u[1], _u[2], _u[3]), (_s[0], _s[1], _s[2], _s[3], _s[4], _s[5], _s[6], _s[7])],
        [(_u[1], _u[2], _u[3], _u[0]), (_s[2], _s[3], _s[4], _s[5], _s[6], _s[7], _s[0], _s[1])],
        [(_u[2], _u[3], _u[0], _u[1]), (_s[4], _s[5], _s[6], _s[7], _s[0], _s[1], _s[2], _s[3])],
        [(_u[3], _u[0], _u[1], _u[2]), (_s[6], _s[7], _s[0], _s[1], _s[2], _s[3], _s[4], _s[5])]
    ]


def pair_case(color1, color2):
    if color1 == color2:
        return "same"
    elif abs(color1 - color2) == 3:
        return "opp"
    else:
        return "adj"


def analyze(cb: cubie.CubieCube):
    stickers = get_stickers(cb)
    u_l_pair1 = u_l_pair2 = None
    d_l_pair1 = d_l_pair2 = None
    u_case = None
    d_case = None

    for u_face, u_side in expanded_sticker_circles(stickers["up"], stickers["up_side"]):
        if u_face == (Color.U, Color.U, Color.U, Color.D):
            u_case = "L"
            u_l_pair1 = pair_case(u_side[1], u_side[2])
            u_l_pair2 = pair_case(u_side[3], u_side[4])
    for d_face, d_side in expanded_sticker_circles(stickers["down"], stickers["down_side"]):
        if d_face == (Color.D, Color.D, Color.D, Color.U):
            d_case = "L"
            d_l_pair1 = pair_case(d_side[1], d_side[2])
            d_l_pair2 = pair_case(d_side[3], d_side[4])
    return u_case, d_case, u_l_pair1, u_l_pair2, d_l_pair1, d_l_pair2


## build_corner_cases()
for qtm in range(6):
    print(qtm)
    with open(f"data/corner_case_{qtm}.pkl", "rb") as f:
        corner_cases = pickle.load(f)
        for moves, cb in corner_cases:
            u_case, d_case, u_l_pair1, u_l_pair2, d_l_pair1, d_l_pair2 = analyze(cb)
            if u_case == "L" and d_case == "L":
                print(moves)
                print(f"{u_l_pair1}/{u_l_pair2} {d_l_pair1}/{d_l_pair2}")
