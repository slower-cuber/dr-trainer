from typing import Union, List

class CubeRotation:
    # front+up color: moves in space -> moves on color
    face_maps = {
        'FU': {'F': 'F', 'B': 'B', 'U': 'U', 'D': 'D', 'L': 'L', 'R': 'R'},
        'FD': {'F': 'F', 'B': 'B', 'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'},
        'FL': {'F': 'F', 'B': 'B', 'U': 'L', 'D': 'R', 'L': 'D', 'R': 'U'},
        'FR': {'F': 'F', 'B': 'B', 'U': 'R', 'D': 'L', 'L': 'U', 'R': 'D'},
        'BU': {'F': 'B', 'B': 'F', 'U': 'U', 'D': 'D', 'L': 'R', 'R': 'L'},
        'BD': {'F': 'B', 'B': 'F', 'U': 'D', 'D': 'U', 'L': 'L', 'R': 'R'},
        'BL': {'F': 'B', 'B': 'F', 'U': 'L', 'D': 'R', 'L': 'U', 'R': 'D'},
        'BR': {'F': 'B', 'B': 'F', 'U': 'R', 'D': 'L', 'L': 'D', 'R': 'U'},
        'LU': {'F': 'L', 'B': 'R', 'U': 'U', 'D': 'D', 'L': 'B', 'R': 'F'},
        'LD': {'F': 'L', 'B': 'R', 'U': 'D', 'D': 'U', 'L': 'F', 'R': 'B'},
        'LF': {'F': 'L', 'B': 'R', 'U': 'F', 'D': 'B', 'L': 'U', 'R': 'D'},
        'LB': {'F': 'L', 'B': 'R', 'U': 'B', 'D': 'F', 'L': 'D', 'R': 'U'},
        'RU': {'F': 'R', 'B': 'L', 'U': 'U', 'D': 'D', 'L': 'F', 'R': 'B'},
        'RD': {'F': 'R', 'B': 'L', 'U': 'D', 'D': 'U', 'L': 'B', 'R': 'F'},
        'RF': {'F': 'R', 'B': 'L', 'U': 'F', 'D': 'B', 'L': 'D', 'R': 'U'},
        'RB': {'F': 'R', 'B': 'L', 'U': 'B', 'D': 'F', 'L': 'U', 'R': 'D'},
        'UF': {'F': 'U', 'B': 'D', 'U': 'F', 'D': 'B', 'L': 'R', 'R': 'L'},
        'UB': {'F': 'U', 'B': 'D', 'U': 'B', 'D': 'F', 'L': 'L', 'R': 'R'},
        'UL': {'F': 'U', 'B': 'D', 'U': 'L', 'D': 'R', 'L': 'F', 'R': 'B'},
        'UR': {'F': 'U', 'B': 'D', 'U': 'R', 'D': 'L', 'L': 'B', 'R': 'F'},
        'DF': {'F': 'D', 'B': 'U', 'U': 'F', 'D': 'B', 'L': 'L', 'R': 'R'},
        'DB': {'F': 'D', 'B': 'U', 'U': 'B', 'D': 'F', 'L': 'R', 'R': 'L'},
        'DL': {'F': 'D', 'B': 'U', 'U': 'L', 'D': 'R', 'L': 'B', 'R': 'F'},
        'DR': {'F': 'D', 'B': 'U', 'U': 'R', 'D': 'L', 'L': 'F', 'R': 'B'},
    }
    def __init__(self, front_color: str, up_color: str):
        self.front_color = front_color
        self.up_color = up_color
        self.face_map = self.face_maps[front_color+up_color]

    def to_face_moves(self, moves: Union[str, List[str]]) -> List[str]:
        if isinstance(moves, str):
            _moves = [t for t in moves.split(' ') if t]
        else:
            _moves = moves

        for _move in _moves:
            yield self.face_map[_move[0]] + _move[1:]


cube_rotation_list: List[CubeRotation] = []
for fu in CubeRotation.face_maps.keys():
    _front_color, _up_color = fu[0], fu[1]
    cube_rotation_list.append(CubeRotation(_front_color, _up_color))
