from random import choice
from typing import List, Dict

from twophase import cubie
from twophase import solver

from src.move import STR_2_MOVE, inverse_move_string
from src.rotation import get_random_cube_rotation


DR_MOVES = ["U", "U'", "D", "D'",
            "U2", "D2",
            "L2", "R2", "F2", "B2"]

MOVES_4e4c = [# "R",
    "B2 L",
    "B2 U L",
    "F2 B2 L",
    "L2 D R",
    "F2 D R",
    "F2 D2 R",
    "R2 U R",
    "R2 U2 R",
    "R2 F2 R",
    "B2 R2 U L",
    "L2 F2 U L",
    "B2 L2 D L",
    "R2 B2 D L",
    "F2 U2 D' L",
    "R2 U2 B2 L",
    "B2 U' F2 L",
    "L2 D' F2 L",
    "B2 D' F2 L",
    "F2 L2 D R",
    "L2 U' D R",
    "F2 U D R",
    "L2 B2 D R",
    "R2 L2 D' R",
    "B2 U2 D2 R",
    "B2 U' D2 R",
    "F2 R2 D2 R",
    "R2 F2 U R",
    "F2 R2 U R",
    "R2 F2 U2 R",
    "R2 D' F2 R",
    "F2 U' F2 R",
    "F2 U2 F2 R",
    "R' D2 F2 R",
    "R' U2 F2 R",
    "L2 U' B2 R",
    "L2 U B2 R",
    "B2 D B2 R",
]

MOVES_4e4c_5 = MOVES_4e4c + [
    "U B2 R2 U L",
    "U2 B2 R2 U L",
    "U' B2 R2 U L",
    "D B2 R2 U L",
    "D2 B2 R2 U L",
    "D' B2 R2 U L",
    "L2 B2 R2 U L",
    "U L2 F2 U L",
    "U2 L2 F2 U L",
    "U' L2 F2 U L",
    "D L2 F2 U L",
    "D2 L2 F2 U L",
    "D' L2 F2 U L",
    "F2 L2 F2 U L",
    "B2 L2 F2 U L",
    "U B2 L2 D L",
    "U2 B2 L2 D L",
    "U' B2 L2 D L",
    "D B2 L2 D L",
    "D2 B2 L2 D L",
    "D' B2 L2 D L",
    "L2 B2 L2 D L",
    "U R2 B2 D L",
    "U2 R2 B2 D L",
    "U' R2 B2 D L",
    "D R2 B2 D L",
    "D2 R2 B2 D L",
    "D' R2 B2 D L",
    "F2 R2 B2 D L",
    "B2 R2 B2 D L",
    "U F2 U2 D' L",
    "U2 F2 U2 D' L",
    "U' F2 U2 D' L",
    "D F2 U2 D' L",
    "D2 F2 U2 D' L",
    "D' F2 U2 D' L",
    "L2 F2 U2 D' L",
    "U R2 U2 B2 L",
    "U2 R2 U2 B2 L",
    "U' R2 U2 B2 L",
    "D R2 U2 B2 L",
    "D2 R2 U2 B2 L",
    "D' R2 U2 B2 L",
    "F2 R2 U2 B2 L",
    "B2 R2 U2 B2 L",
    "U B2 U' F2 L",
    "U2 B2 U' F2 L",
    "U' B2 U' F2 L",
    "D B2 U' F2 L",
    "D2 B2 U' F2 L",
    "D' B2 U' F2 L",
    "L2 B2 U' F2 L",
    "U L2 D' F2 L",
    "U2 L2 D' F2 L",
    "U' L2 D' F2 L",
    "D L2 D' F2 L",
    "D2 L2 D' F2 L",
    "D' L2 D' F2 L",
    "F2 L2 D' F2 L",
    "B2 L2 D' F2 L",
    "U B2 D' F2 L",
    "U2 B2 D' F2 L",
    "U' B2 D' F2 L",
    "D B2 D' F2 L",
    "D2 B2 D' F2 L",
    "D' B2 D' F2 L",
    "L2 B2 D' F2 L",
    "U F2 L2 D R",
    "U2 F2 L2 D R",
    "U' F2 L2 D R",
    "D F2 L2 D R",
    "D2 F2 L2 D R",
    "D' F2 L2 D R",
    "R2 F2 L2 D R",
    "U L2 U' D R",
    "U2 L2 U' D R",
    "U' L2 U' D R",
    "D L2 U' D R",
    "D2 L2 U' D R",
    "D' L2 U' D R",
    "F2 L2 U' D R",
    "B2 L2 U' D R",
    "U F2 U D R",
    "U2 F2 U D R",
    "U' F2 U D R",
    "D F2 U D R",
    "D2 F2 U D R",
    "D' F2 U D R",
    "R2 F2 U D R",
    "U L2 B2 D R",
    "U2 L2 B2 D R",
    "U' L2 B2 D R",
    "D L2 B2 D R",
    "D2 L2 B2 D R",
    "D' L2 B2 D R",
    "F2 L2 B2 D R",
    "B2 L2 B2 D R",
    "U R2 L2 D' R",
    "U2 R2 L2 D' R",
    "U' R2 L2 D' R",
    "D R2 L2 D' R",
    "D2 R2 L2 D' R",
    "D' R2 L2 D' R",
    "F2 R2 L2 D' R",
    "B2 R2 L2 D' R",
    "U B2 U2 D2 R",
    "U2 B2 U2 D2 R",
    "U' B2 U2 D2 R",
    "D B2 U2 D2 R",
    "D2 B2 U2 D2 R",
    "D' B2 U2 D2 R",
    "R2 B2 U2 D2 R",
    "U B2 U' D2 R",
    "U2 B2 U' D2 R",
    "U' B2 U' D2 R",
    "D B2 U' D2 R",
    "D2 B2 U' D2 R",
    "D' B2 U' D2 R",
    "R2 B2 U' D2 R",
    "U F2 R2 D2 R",
    "U2 F2 R2 D2 R",
    "U' F2 R2 D2 R",
    "D F2 R2 D2 R",
    "D2 F2 R2 D2 R",
    "D' F2 R2 D2 R",
    "R2 F2 R2 D2 R",
    "U R2 F2 U R",
    "U2 R2 F2 U R",
    "U' R2 F2 U R",
    "D R2 F2 U R",
    "D2 R2 F2 U R",
    "D' R2 F2 U R",
    "F2 R2 F2 U R",
    "B2 R2 F2 U R",
    "U F2 R2 U R",
    "U2 F2 R2 U R",
    "U' F2 R2 U R",
    "D F2 R2 U R",
    "D2 F2 R2 U R",
    "D' F2 R2 U R",
    "R2 F2 R2 U R",
    "U R2 F2 U2 R",
    "U2 R2 F2 U2 R",
    "U' R2 F2 U2 R",
    "D R2 F2 U2 R",
    "D2 R2 F2 U2 R",
    "D' R2 F2 U2 R",
    "F2 R2 F2 U2 R",
    "B2 R2 F2 U2 R",
    "U R2 D' F2 R",
    "U2 R2 D' F2 R",
    "U' R2 D' F2 R",
    "D R2 D' F2 R",
    "D2 R2 D' F2 R",
    "D' R2 D' F2 R",
    "F2 R2 D' F2 R",
    "B2 R2 D' F2 R",
    "U F2 U' F2 R",
    "U2 F2 U' F2 R",
    "U' F2 U' F2 R",
    "D F2 U' F2 R",
    "D2 F2 U' F2 R",
    "D' F2 U' F2 R",
    "R2 F2 U' F2 R",
    "U F2 U2 F2 R",
    "U2 F2 U2 F2 R",
    "U' F2 U2 F2 R",
    "D F2 U2 F2 R",
    "D2 F2 U2 F2 R",
    "D' F2 U2 F2 R",
    "R2 F2 U2 F2 R",
    "U L2 U' B2 R",
    "U2 L2 U' B2 R",
    "U' L2 U' B2 R",
    "D L2 U' B2 R",
    "D2 L2 U' B2 R",
    "D' L2 U' B2 R",
    "F2 L2 U' B2 R",
    "B2 L2 U' B2 R",
    "U L2 U B2 R",
    "U2 L2 U B2 R",
    "U' L2 U B2 R",
    "D L2 U B2 R",
    "D2 L2 U B2 R",
    "D' L2 U B2 R",
    "F2 L2 U B2 R",
    "B2 L2 U B2 R",
    "U B2 D B2 R",
    "U2 B2 D B2 R",
    "U' B2 D B2 R",
    "D B2 D B2 R",
    "D2 B2 D B2 R",
    "D' B2 D B2 R",
    "R2 B2 D B2 R",
]


def gen_dr_moves(n=20):
    moves = []
    prev_move_face = None

    while True:
        m = choice(DR_MOVES)
        if m[0] == prev_move_face:
            continue
        moves.append(m)
        prev_move_face = m[0]
        if len(moves) >= n:
            print(moves)
            return moves


def get_trigger_moves(trigger_type='4e4c', mode: str = None) -> (List, str):
    dr_moves = gen_dr_moves()
    if trigger_type == '4e4c':
        trigger_str = choice(MOVES_4e4c_5)
        print(trigger_str)
        if mode == 'easy':
            return list(inverse_move_string(trigger_str)), trigger_str
        else:
            return dr_moves + list(inverse_move_string(trigger_str)), trigger_str
    else:
        raise ValueError(f'Unsupported trigger type {trigger_type}')


def get_training_scramble(trigger_type='4e4c', scramble_mode: str = None) -> Dict:
    destination_cube = cubie.CubieCube()
    dr_moves, trigger_string = get_trigger_moves(trigger_type, scramble_mode)
    for dr_move in dr_moves:
        destination_cube.multiply(
            cubie.moveCube[STR_2_MOVE[dr_move]]
        )

    ans_string = solver.solve(destination_cube.to_facelet_cube().to_string(),
                              max_length=21)
    clear_ans_string = ans_string.rsplit(' (', 1)[0]

    scramble = list(inverse_move_string(clear_ans_string))

    cube_rotation = get_random_cube_rotation()
    rotated_scramble = cube_rotation.to_face_moves(scramble)
    rotated_trigger = cube_rotation.to_face_moves(trigger_string)

    return {
        'scramble': rotated_scramble,
        'trigger': rotated_trigger,
        'cube_rotation': cube_rotation
    }
