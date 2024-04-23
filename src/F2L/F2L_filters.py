

import time
from face_class import Corner, Edge, Face
from rubik_class import RubiksCube


def is_chunck_resolved(face_dir: str, sense: str, rubik: RubiksCube):
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
    if len(list(filter(lambda elem: not is_final_pos(elem), corners))):
        print('return false', face_dir, sense)
        return False
    edge = rubik.cube[face_dir].get_edge(index_edge, rubik)
    print(face_dir, sense, is_final_pos_edge(rubik.cube[face_dir], edge))
    return is_final_pos_edge(rubik.cube[face_dir], edge)


def is_final_pos(cube: Corner):
    if (cube["corner"]["color"] == cube["corner"]["face"].color)\
            and (cube["corner_i"]["color"] == cube["corner_i"]["face"].color)\
            and (cube["corner_j"]["color"] == cube["corner_j"]["face"].color):
        return True
    return False


def is_final_pos_edge(face: Face, edge: Edge):
    if face[(1, 2)] == face.color\
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
    print("in adjacent left",
          cube["corner_i"]["face"].color, adjacent_corner_i, adjacent_edge)
    if (cube["corner_i"]["color"] == cube["corner_i"]["face"][adjacent_corner_i]
            and adjacent_edge["color"] == cube["corner_j"]["face"].color):
        return True
    return False


def is_adjacent_well_placed(cube: Corner, rubik) -> dict | None:
    adjacent = (cube["corner"]["index"][0], 1)
    adjacent_edge = cube["corner"]["face"].get_edge(
        adjacent, rubik)
    print("is_adjacent_i_well_placed",
          cube["corner"]["face"][adjacent], adjacent_edge)
    if (cube["corner"]["face"][adjacent] == cube['corner_i']["color"])\
            and (adjacent_edge["color"] == cube['corner_j']["color"]):
        return {"case": 1, "edge": adjacent_edge, "idx": adjacent}
    if (cube["corner"]["face"][adjacent] == cube['corner_j']["color"])\
            and (adjacent_edge["color"] == cube['corner_i']["color"]):
        return {"case": 2, "edge": adjacent_edge, "idx": adjacent}
    return None


def is_adjacent_j_well_placed(cube: Corner, rubik) -> dict | None:
    adjacent = (cube["corner_j"]["index"][0], 1)
    adjacent_edge = cube["corner_j"]["face"].get_edge(
        adjacent, rubik)
    print("adj j")
    print(cube["corner_j"]["face"][adjacent], cube['corner_j']["color"])
    print()
    print(adjacent_edge["color"], cube['corner_i']["color"])
    if (cube["corner_j"]["face"][adjacent] == cube['corner_j']["color"])\
            and (adjacent_edge["color"] == cube['corner_i']["color"]):
        return {"case": 1, "edge": adjacent_edge, "idx": adjacent}
    if (cube["corner_j"]["face"][adjacent] == cube['corner_i']["color"])\
            and (adjacent_edge["color"] == cube['corner_j']["color"]):
        return {"case": 2, "edge": adjacent_edge, "idx": adjacent}
    return None


def is_adjacent_bottom_well_placed(cube: Corner, rubik):
    adjacent = (1, cube["corner_j"]["index"][1])
    adjacent_edge = cube["corner_j"]["face"].get_edge(
        adjacent, rubik)
    if (cube["corner_j"]["face"][adjacent] == cube['corner_j']["color"])\
            and (adjacent_edge["color"] == cube['corner_i']["color"]):
        return {"case": 1, "edge": adjacent_edge, "idx": adjacent}
    if (cube["corner_j"]["face"][adjacent] == cube['corner_i']["color"])\
            and (adjacent_edge["color"] == cube['corner_j']["color"]):
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

    print("corner_i", corner2, up_corner, cube["corner_i"]["color"])
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


def is_left_edge_well_placed(face_dir: str, edge: Edge, rubik: RubiksCube):
    adjacent_face = rubik.cube[face_dir].get_corners((2, 2), rubik)[
        "corner_j"]["face"]
    print("adj face dir", adjacent_face.dir, "\n",
          rubik.cube[face_dir].color, rubik.cube[face_dir][(2, 1)], "\n",
          adjacent_face.color, edge["color"])
    if (rubik.cube[face_dir].color == rubik.cube[face_dir][(2, 1)]
            and adjacent_face.color == edge["color"]):
        return adjacent_face

    return None


def is_right_edge_well_placed(face_dir: str, edge: Edge, rubik: RubiksCube):
    adjacent_face = rubik.cube[face_dir].get_corners((2, 0), rubik)[
        "corner_j"]["face"]
    print("adj face dir", adjacent_face.dir, "\n",
          rubik.cube[face_dir].color, rubik.cube[face_dir][(2, 1)], "\n",
          adjacent_face.color, edge["color"])
    if (rubik.cube[face_dir].color == rubik.cube[face_dir][(2, 1)]
            and adjacent_face.color == edge["color"]):
        return adjacent_face

    return None


def right_edge_well_placed(cube: Corner, rubik: RubiksCube):

    face: Face | None = None
    if (cube["corner"]["index"][1] == 0):
        face = cube["corner"]["face"]
    elif (cube["corner"]["index"][1] == 2):
        face = cube["corner_j"]["face"]

    print('in right_edge_well_placed')
    print(face.dir)
    print(cube['corner_i']['color'])

    edge = face.get_edge((2, 1), rubik)
    if (face[2, 1] == cube['corner_j']["color"]) and \
            edge['color'] == cube['corner_i']["color"]:
        return 1 if cube["corner"]["index"][1] == 2 \
            else 2


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
                if is_adjacent_bottom_well_placed(corner, rubik):
                    return True
    return False

# Define similar helper functions for algorithms 39 to 42...

# Function to select the appropriate algorithm
def select_f2l_algorithm(corner: Corner, rubik: RubiksCube):
    print("in select_f2l_algorithm")
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