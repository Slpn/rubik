

import time
from face_class import Corner, Edge, Face
from rubik_class import RubiksCube
from rubik_utils import get_F_corner_bottom, get_R_corner_bottom


def is_chunck_resolved(face_dir: str, sense: str, rubik: RubiksCube, is_not_found: False):
    index_corner = None
    index_edge = None
    if (sense == "+"):
        index_edge = (1, 0)
        index_corner = [(0, 0)]
    elif (sense == "-"):
        index_edge = (1, 2)
        index_corner = [(0, 2)]

    corners = [rubik.cube[face_dir].get_corners(
        index, rubik) for index in index_corner]
    edge = rubik.cube[face_dir].get_edge(index_edge, rubik)
    if not is_not_found:
        if len(list(filter(lambda elem: not is_final_pos(elem), corners)))\
                and not is_final_pos_edge(rubik.cube[face_dir], edge):
            return False
        return True
    else:
        if len(list(filter(lambda elem: not is_final_pos(elem), corners))):
            return False
        return is_final_pos_edge(rubik.cube[face_dir], edge)


def is_final_pos(cube: Corner):
    if (cube["corner"]["color"] == cube["corner"]["face"].color)\
            and (cube["corner_i"]["color"] == cube["corner_i"]["face"].color)\
            and (cube["corner_j"]["color"] == cube["corner_j"]["face"].color):
        return True
    return False


def is_final_pos_edge(face: Face, edge: Edge):
    if face[(1, 0)] == face.color\
            and edge["color"] == edge["face"].color:
        return True
    return False


def is_cube_well_placed(cube: Corner):

    if (cube["corner_j"]["color"] == cube["corner"]["face"].color)\
            and\
        ((cube["corner_i"]["color"] == cube["corner_i"]["face"].color)
            or
            (cube["corner_i"]["color"] == cube["corner_j"]["face"].color)):
        return True

    if (cube["corner_i"]["color"] == cube["corner"]["face"].color)\
            and\
            ((cube["corner_j"]["color"] == cube["corner_j"]["face"].color)
                or
                (cube["corner_j"]["color"] == cube["corner_i"]["face"].color)):
        return True

    if (cube["corner_i"]["color"] == cube["corner_j"]["face"].color)\
            and (cube["corner_j"]["color"] == cube["corner_i"]["face"].color):
        return True

    return False


def is_i_corner_equals_color(cube: Corner):
    if (cube["corner_i"]["color"] == cube["corner"]["face"].color)\
            and\
            (cube["corner_j"]["color"] == cube["corner_j"]["face"].color):
        return True

    return False


def is_i_corner_equals_j_color(cube: Corner):
    if (cube["corner_i"]["color"] == cube["corner_j"]["face"].color)\
            and\
            (cube["corner_j"]["color"] == cube["corner_i"]["face"].color):
        return True

    return False


def is_cube_on_top(cube: Corner) -> bool:
    if (cube['corner']['face'].dir == 'Up' or cube['corner']['face'].dir == 'Down'):
        return False
    if (cube['corner']['index'][0] == 2):
        return True
    return False


def is_cube_on_bottom(cube: Corner) -> bool:
    if (cube['corner']['face'].dir == 'Up' or cube['corner']['face'].dir == 'Down'):
        return False
    if (cube['corner']['index'][0] == 0):
        return True
    return False


def is_cube_up_face(cube: Corner) -> bool:
    if (cube['corner']['face'].dir == 'Down'):
        return True
    return False


def is_cube_on_left(cube: Corner) -> bool:
    if (cube['corner']['index'][1] == 2):
        return True
    return False


def is_cube_on_right(cube: Corner) -> bool:
    if (cube['corner']['index'][1] == 0):
        return True
    return False


def is_corner_i_equals_color(cube: Corner) -> bool:
    if (cube["corner"]["face"].color == cube["corner_i"]["color"]):
        return True
    return False


def is_corner_j_equals_j_color(cube: Corner) -> bool:
    if (cube["corner_j"]["face"].color == cube["corner_j"]["color"]):
        return True
    return False


def is_adjacent_left_well_placed(cube: Corner, rubik: RubiksCube) -> bool:

    adjacent_corner_i = (1, cube["corner_i"]["index"][1])
    adjacent_edge = cube["corner_i"]["face"].get_edge(
        adjacent_corner_i, rubik)
    if (cube["corner_i"]["color"] == cube["corner_i"]["face"][adjacent_corner_i]
            and adjacent_edge["color"] == cube["corner_j"]["face"].color):
        return True
    return False


def is_adjacent_well_placed(cube: Corner, rubik, on_top=False) -> dict | None:
    adjacent_idx, corner1, corner2 = None, None, None
    if not on_top:
        adjacent_idx = (cube["corner"]["index"][0], 1)
        corner1 = cube["corner_i"]
        corner2 = cube["corner_j"]

    else:
        idx = cube["corner"]["index"]
        match idx:
            case (0, 2) | (2, 0):
                corner1 = cube["corner_i"]
                corner2 = cube["corner_j"]
                adjacent_idx = (1, 2) if idx == (0, 2) else (1, 0)
            case (0, 0) | (2, 2):
                corner1 = cube["corner_j"]
                corner2 = cube["corner_i"]
                adjacent_idx = (0, 1) if idx == (0, 0) else (2, 1)

    adjacent_edge = cube["corner"]["face"].get_edge(
        adjacent_idx, rubik)

    if (cube["corner"]["face"][adjacent_idx] == corner1["color"])\
            and (adjacent_edge["color"] == corner2["color"]):
        return {"case": 1, "edge": adjacent_edge, "idx": adjacent_idx}
    if (cube["corner"]["face"][adjacent_idx] == corner2["color"])\
            and (adjacent_edge["color"] == corner1["color"]):
        return {"case": 2, "edge": adjacent_edge, "idx": adjacent_idx}
    return None


def is_adjacent_j_well_placed(cube: Corner, rubik, on_top=False) -> dict | None:
    adjacent_idx, corner1, corner2, adjacent_edge = None, None, None, None
    if not on_top:
        adjacent_idx = (2, 1)
        corner1 = cube["corner_i"]
        corner2 = cube["corner_j"]
        corner = cube["corner_j"]

    else:
        idx = cube["corner"]["index"]
        corner = cube["corner"]
        match idx:
            case (0, 2) | (2, 0):
                corner1 = cube["corner_i"]
                corner2 = cube["corner_j"]
                adjacent_idx = (0, 1) if idx == (0, 2) else (2, 1)

            case (0, 0) | (2, 2):
                corner1 = cube["corner_j"]
                corner2 = cube["corner_i"]
                adjacent_idx = (1, 0) if idx == (0, 0) else (1, 2)

    adjacent_edge = corner["face"].get_edge(
        adjacent_idx, rubik)

    if (corner["face"][adjacent_idx] == corner2["color"])\
            and (adjacent_edge["color"] == corner1["color"]):
        return {"case": 1, "edge": adjacent_edge, "idx": adjacent_idx}
    if (corner["face"][adjacent_idx] == corner1["color"])\
            and (adjacent_edge["color"] == corner2["color"]):
        return {"case": 2, "edge": adjacent_edge, "idx": adjacent_idx}
    return None


def is_adjacent_mid_well_placed(cube: Corner, rubik):
    adjacent = (1, cube["corner_j"]["index"][1])
    adjacent_edge = cube["corner_j"]["face"].get_edge(
        adjacent, rubik)
    if (cube["corner_j"]["color"] == cube["corner_j"]["face"][adjacent]
            and adjacent_edge["color"] == cube["corner_i"]["color"]):
        return {"case": 1, "edge": adjacent_edge, "idx": adjacent}
    if (cube["corner_i"]["color"] == cube["corner_j"]["face"][adjacent]
            and adjacent_edge["color"] == cube["corner_j"]["color"]):
        return {"case": 2, "edge": adjacent_edge, "idx": adjacent}
    return None


def is_opposite_right_well_placed(cube: Corner, rubik, on_top=False) -> bool:
    opposite_idx, up_corner, up_idx, corner1, corner2 = None, None, None, None, None

    if not on_top:
        up_corner = cube["corner_i"]
        up_idx = cube["corner_i"]["index"]
        corner1 = cube["corner_i"]
        corner2 = cube["corner_j"]

    else:
        up_corner = cube["corner"]
        up_idx = cube["corner"]["index"]
        match up_corner["index"]:
            case (0, 2) | (2, 0):
                corner1 = cube["corner_i"]
                corner2 = cube["corner_j"]
            case (0, 0) | (2, 2):
                corner1 = cube["corner_j"]
                corner2 = cube["corner_i"]

    match up_idx:
        case (0, 2):
            opposite_idx = (2, 1)
        case (0, 0):
            opposite_idx = (1, 2)
        case (2, 0):
            opposite_idx = (0, 1)
        case (2, 2):
            opposite_idx = (1, 0)

    opposite_edge = up_corner["face"].get_edge(
        opposite_idx, rubik)

    if (corner2["color"] == opposite_edge["color"]
            and up_corner["face"][opposite_idx] == corner1["color"]):
        return 1
    if (corner2["color"] == up_corner["face"][opposite_idx]
            and opposite_edge["color"] == corner1["color"]):
        return 2
    return None


def is_opposite_left_well_placed(cube: Corner, rubik, on_top=False) -> bool:
    opposite_idx, up_corner, up_idx, corner1, corner2 = None, None, None, None, None

    if not on_top:
        up_corner = cube["corner_i"]
        up_idx = cube["corner_i"]["index"]
        corner1 = cube["corner_i"]
        corner2 = cube["corner_j"]
    else:
        up_corner = cube["corner"]
        up_idx = cube["corner"]["index"]
        match up_corner["index"]:
            case (0, 2) | (2, 0):
                corner1 = cube["corner_i"]
                corner2 = cube["corner_j"]
            case (0, 0) | (2, 2):
                corner1 = cube["corner_j"]
                corner2 = cube["corner_i"]

    match up_idx:
        case (0, 2):
            opposite_idx = (1, 0)
        case (0, 0):
            opposite_idx = (2, 1)
        case (2, 0):
            opposite_idx = (1, 2)
        case (2, 2):
            opposite_idx = (0, 1)

    opposite_edge = up_corner["face"].get_edge(
        opposite_idx, rubik)

    if (corner2["color"] == opposite_edge["color"]
            and up_corner["face"][opposite_idx] == corner1["color"]):
        return 1

    if (corner2["color"] == up_corner["face"][opposite_idx]
            and opposite_edge["color"] == corner1["color"]):
        return 2
    return None


def is_right_edge_well_placed(corner: Corner, rubik: RubiksCube):
    face = rubik.cube[get_R_corner_bottom(corner["corner"]["index"])]
    top_edges = face.get_edge((2, 1), rubik)
    adjacent_face = rubik.cube[get_F_corner_bottom(corner["corner"]["index"])]
    if (face.color == face[(2, 1)]
            and top_edges["color"] == adjacent_face.color):
        return corner

    return None


def is_left_edge_well_placed(corner: Corner,  rubik: RubiksCube):
    face = rubik.cube[get_F_corner_bottom(corner["corner"]["index"])]
    top_edges = face.get_edge((2, 1), rubik)
    adjacent_face = rubik.cube[get_R_corner_bottom(corner["corner"]["index"])]
    if (face.color == face[(2, 1)]
            and top_edges["color"] == adjacent_face.color):
        return corner

    return None


def right_up_edge_well_placed(cube: Corner, rubik: RubiksCube):

    face = rubik.cube[get_R_corner_bottom(cube["corner_i"]["index"])]
    adjacent_face = rubik.cube[get_F_corner_bottom(cube["corner_i"]["index"])]

    edge = face.get_edge((2, 1), rubik)
    if (face[2, 1] == face.color) and \
            (edge['color'] == adjacent_face.color):
        return {"face_dir": face.dir, "edge": edge, "case": 1 if cube["corner"]["index"][1] == 2
                else 2}


def left_up_edge_well_placed(cube: Corner, rubik: RubiksCube):
    face: Face | None = None

    face = rubik.cube[get_F_corner_bottom(cube["corner_i"]["index"])]
    adjacent_face = rubik.cube[get_R_corner_bottom(cube["corner_i"]["index"])]
    edge = face.get_edge((2, 1), rubik)

    if (face[2, 1] == face.color) and \
            edge['color'] == adjacent_face.color:
        return {"face_dir": face.dir, "edge": edge, "case": 1 if cube["corner"]["index"][1] == 2
                else 2}


def can_use_algo_38(corner: Corner, rubik: RubiksCube) -> bool:
    if is_cube_on_bottom(corner):
        if is_cube_well_placed(corner):
            if is_i_corner_equals_color(corner):
                if is_adjacent_left_well_placed(corner, rubik):
                    return True
    return False


def can_use_algo_39(corner: Corner, rubik: RubiksCube) -> bool:
    if is_cube_on_bottom(corner):
        if is_cube_well_placed(corner):
            if is_i_corner_equals_color(corner):
                if is_adjacent_well_placed(corner, rubik):
                    return True
    return False


def can_use_algo_40(corner: Corner, rubik: RubiksCube) -> bool:
    if is_cube_on_bottom(corner):
        if is_cube_well_placed(corner):
            if is_i_corner_equals_color(corner):
                if is_opposite_left_well_placed(corner, rubik):
                    return True
    return False


def can_use_algo_41(corner: Corner, rubik: RubiksCube) -> bool:
    if is_cube_on_bottom(corner):
        if is_cube_well_placed(corner):
            if is_i_corner_equals_color(corner):
                if is_opposite_right_well_placed(corner, rubik):
                    return True
    return False


def can_use_algo_42(corner: Corner, rubik: RubiksCube) -> bool:
    if is_cube_on_bottom(corner):
        if is_cube_well_placed(corner):
            if is_i_corner_equals_color(corner):
                if is_adjacent_mid_well_placed(corner, rubik):
                    return True
    return False

# Define similar helper functions for algorithms 39 to 42...

# Function to select the appropriate algorithm


def select_f2l_algorithm(corner: Corner, rubik: RubiksCube):
    if can_use_algo_38(corner, rubik):
        return 38
    if can_use_algo_39(corner, rubik):
        return 39
    if can_use_algo_40(corner, rubik):
        return 40
    if can_use_algo_41(corner, rubik):
        return 41
    if can_use_algo_42(corner, rubik):
        return 42

    return None
