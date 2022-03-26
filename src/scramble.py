from random import choice
from typing import List, Dict

from twophase import cubie
from twophase import solver

from src.move import STR_2_MOVE, inverse_move_string
from src.rotation import get_random_cube_rotation


DR_MOVES = ["U", "U'", "D", "D'",  "U2", "D2",
            "L2", "R2", "F2", "B2"]

MOVES_4e4c = [# "R",
              "B2 L",
              "F2 D2 R",
              "B2 U L",
              "L2 D R",
              "F2 D R",
              "R2 U R",
              "R2 F2 R",
              "R2 U2 R",
              "F2 B2 L",
              "L2 U' D R",
              "B2 U2 D2 R",
              "B2 U' D2 R",
              "F2 U2 D' L",
              "R2 F2 U2 R",
              "F2 U D R",
              "L2 B2 D R",
              "B2 R2 U L",
              "R2 F2 U R",
              "F2 L2 D R",
              "L2 F2 U L",
              "B2 L2 D L",
              "R2 B2 D L",
              "F2 R2 U R",
              "R2 U2 B2 L",
              "F2 R2 D2 R",
              "R2 D' F2 R",
              "F2 U' F2 R",
              "L2 D' F2 L",
              "B2 U' F2 L",
              "L2 U' B2 R",
              "B2 D' F2 L",
              "L2 U B2 R",
              "B2 D B2 R",
              "R2 L2 D' R",
              "F2 U2 F2 R",
              "R' D2 F2 R",
              "R' U2 F2 R"]


def gen_dr_moves(n=15):
    return [choice(DR_MOVES) for _ in range(n)]


def get_trigger_moves(trigger_type='4e4c') -> (List, str):
    dr_moves = gen_dr_moves()
    if trigger_type == '4e4c':
        trigger_str = choice(MOVES_4e4c)
        return dr_moves + list(inverse_move_string(trigger_str)), trigger_str
    else:
        raise ValueError(f'Unsupported trigger type {trigger_type}')


def get_training_scramble(trigger_type='4e4c') -> Dict:
    destination_cube = cubie.CubieCube()
    dr_moves, trigger_string = get_trigger_moves(trigger_type)
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
