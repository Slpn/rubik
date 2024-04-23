from rubik_class import Opposite_mouves, RubiksCube
from face_class import Edge, Face, check_edge_color, dir_nodes, Corner
import numpy as np
from utils import CircularChainedList, get_face_to_mouve, mouves_dir, get_new_idx, inverse_mouves_dir, y_prime_mouve_dir
from vizualize import RubixVisualiser


def one(cube: Corner):
    print("1")
    R = cube['corner_j']["face"].dir
    # 1
    # mouves = U (R U' R')
    return ["U", mouves_dir[R]["+"], "U'", mouves_dir[R]["-"]]


def two(cube: Corner):
    print("2")
    R = cube['corner']["face"].dir
    # 2
    # mouves = y' U' (R' U R)
    return [y_prime_mouve_dir["U'"], y_prime_mouve_dir[mouves_dir[R]["-"]],
            y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["+"]]]


def three(cube: Corner):
    print("3")
    R = cube['corner_j']["face"].dir
    # 3
    # mouves = y' (R' U' R)
    return [y_prime_mouve_dir[mouves_dir[R]["-"]],
            y_prime_mouve_dir["U'"], y_prime_mouve_dir[mouves_dir[R]["+"]]]


def four(cube: Corner):
    print("4")
    R = cube['corner_j']["face"].dir
    # 4
    # mouves = (R U R')
    return [mouves_dir[R]["+"],
            "U", mouves_dir[R]["-"]]


def five(cube: Corner):
    print("5")
    R = cube['corner_j']["face"].dir
    # 5
    # mouve = (U' R U R') U2 (R U' R')
    return ["U'", mouves_dir[R]["+"], "U", mouves_dir[R]["-"],
            "U2",  mouves_dir[R]["+"], "U'",  mouves_dir[R]["-"]]


def six(cube: Corner):
    print("6")
    R = cube['corner']["face"].dir
    # 6
    # mouve = y' U' (R' U R) U2 (R' U' R)
    return [y_prime_mouve_dir["U'"], y_prime_mouve_dir[mouves_dir[R]["-"]],
            y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["+"]],
            "U2", y_prime_mouve_dir[mouves_dir[R]["-"]],
            y_prime_mouve_dir["U'"], y_prime_mouve_dir[mouves_dir[R]["+"]]]


def seven(cube: Corner):
    print("7")
    R = cube['corner_j']["face"].dir
    # 7
    # mouve = U' (R U2' R') U2 (R U' R')
    return ["U'", mouves_dir[R]["+"], "U2", mouves_dir[R]["-"],
            "U2", mouves_dir[R]["+"], "U'", mouves_dir[R]["-"]]


def eight(cube: Corner):
    print("8")
    R = cube['corner']["face"].dir
    # 8
    # mouve = y' U (R' U2 R) U2' (R' U R)
    return [y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["-"]],
            y_prime_mouve_dir["U2"], y_prime_mouve_dir[mouves_dir[R]["+"]],
            y_prime_mouve_dir["U2"], y_prime_mouve_dir[mouves_dir[R]["-"]],
            y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["+"]]]


def nine(cube: Corner):
    print("9")
    R = cube['corner_j']["face"].dir
    # 9
    # mouve = U' (R U' R' U) y' (R' U' R)
    return ["U'", mouves_dir[R]["+"], "U'", mouves_dir[R]["-"],
            "U", y_prime_mouve_dir[mouves_dir[R]["-"]],
            y_prime_mouve_dir["U'"], y_prime_mouve_dir[mouves_dir[R]["+"]]]


def ten(cube: Corner):
    print("10")
    R = cube['corner']["face"].dir
    # 10
    # mouve = U' (R U R' U)(R U R')
    return ["U'", mouves_dir[R]["+"], "U", mouves_dir[R]["-"],
            "U", mouves_dir[R]["+"], "U", mouves_dir[R]["-"]]


def eleven(cube: Corner):
    print("11")
    R = cube['corner_j']["face"].dir
    # 11
    # mouve =U' (R U2' R' U) y' (R' U' R)
    return ["U'", mouves_dir[R]['+'], "U2",
            mouves_dir[R]['-'], "U",
            y_prime_mouve_dir[mouves_dir[R]['-']], y_prime_mouve_dir["U'"],
            y_prime_mouve_dir[mouves_dir[R]['+']]]


def twelve(cube: Corner):
    print("12")
    R = cube['corner']["face"].dir
    # 12
    # mouve = R' U2' R2 U R2' U R
    return [mouves_dir[R]['-'], "U2", mouves_dir[R]['opposite'],
            "U", mouves_dir[R]['opposite'], "U", mouves_dir[R]['+']]


def thirteen(cube: Corner):
    print("13")
    R = cube['corner_j']["face"].dir
    # 13
    # mouve = y' U (R' U R U') (R' U' R)
    return [y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["-"]], y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["+"]],
            y_prime_mouve_dir["U'"], y_prime_mouve_dir[mouves_dir[R]["-"]], y_prime_mouve_dir["U'"], y_prime_mouve_dir[mouves_dir[R]["+"]]]


def fourteen(cube: Corner):
    print("14")
    R = cube["corner"]["face"].dir
    # 14
    # mouve = U' (R U' R' U) (R U R')
    return ["U'", mouves_dir[R]["+"], "U'", mouves_dir[R]["-"],
            "U", mouves_dir[R]["+"], "U", mouves_dir[R]["-"]]


def fifteen(cube: Corner):
    print("15")
    R = cube["corner_j"]["face"].dir
    # 15
    # mouves = 	y' (R' U R) U2' y (R U R')
    return [y_prime_mouve_dir[mouves_dir[R]['-']], y_prime_mouve_dir["U"],
            y_prime_mouve_dir[mouves_dir[R]['+']], y_prime_mouve_dir["U2"],
            mouves_dir[R]['+'], "U", mouves_dir[R]['-']]


def sixteen(cube: Corner):
    print("16")
    R = cube["corner"]["face"].dir
    F = cube["corner_j"]["face"].dir
    # 16
    # mouves = 	(R U' R') U2 (F' U' F)
    return [mouves_dir[R]["+"], "U'", mouves_dir[R]["-"],
            "U2", mouves_dir[F]["-"], "U'", mouves_dir[F]["+"]]


def seventeen(cube: Corner):
    print("17")
    R = get_R_corner_top(cube['corner']["index"])
    # 17
    # mouves = 	(R U2 R') U' (R U R')
    return [mouves_dir[R]['+'], "U2", mouves_dir[R]['-'],
            "U'", mouves_dir[R]['+'], "U", mouves_dir[R]['-']]


def eighteen(cube: Corner):
    print("18")
    R = get_R_corner_top(cube['corner']["index"])
    # 18
    # mouves = 	y' (R' U2 R) U (R' U' R)
    return [y_prime_mouve_dir[mouves_dir[R]["-"]],  y_prime_mouve_dir["U2"],
            y_prime_mouve_dir[mouves_dir[R]
                              ["+"]], y_prime_mouve_dir["U"],
            y_prime_mouve_dir[mouves_dir[R]
                              ["-"]], y_prime_mouve_dir["U'"],
            y_prime_mouve_dir[mouves_dir[R]["+"]]]


def nineteen(cube: Corner):
    print("19")
    R = get_R_corner_top(cube['corner']["index"])
    # 19
    # mouves = U (R U2 R') U (R U' R')
    return ["U", mouves_dir[R]["+"], "U2", mouves_dir[R]["-"],
            "U", mouves_dir[R]["+"],  "U'", mouves_dir[R]["-"]]


def twenty(cube: Corner):
    print("20")
    R = get_R_corner_top(cube['corner']["index"])
    # 20
    # mouves = y' U' (R' U2 R) U' (R' U R)
    return [y_prime_mouve_dir["U'"], y_prime_mouve_dir[mouves_dir[R]["-"]], y_prime_mouve_dir["U2"],
            y_prime_mouve_dir[mouves_dir[R]["+"]], y_prime_mouve_dir["U'"],
            y_prime_mouve_dir[mouves_dir[R]["-"]], y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["+"]]]


def twenty_one(cube: Corner):
    print("21")
    R = get_R_corner_top(cube['corner']["index"])
    # 21
    # mouves = U2 (R U R' U)(R U' R')
    return ["U2", mouves_dir[R]["+"], "U", mouves_dir[R]["-"],
            "U", mouves_dir[R]["+"], "U'", mouves_dir[R]["-"]]


def twenty_two(cube: Corner):
    print("22")
    R = get_R_corner_top(cube['corner']["index"])
    # 22
    # mouves = y' U2 (R' U' R U')(R' U R)
    return [y_prime_mouve_dir["U2"], y_prime_mouve_dir[mouves_dir[R]['-']],
            y_prime_mouve_dir["U'"],  y_prime_mouve_dir[mouves_dir[R]['+']],
            y_prime_mouve_dir["U'"],  y_prime_mouve_dir[mouves_dir[R]['-']],
            y_prime_mouve_dir["U"],  y_prime_mouve_dir[mouves_dir[R]['+']]]


def twenty_three(cube: Corner):
    print("23")
    R = get_R_corner_top(cube['corner']["index"])
    # 23
    # mouves = U2 R2 U2 (R' U' R U') R2
    return ["U2", mouves_dir[R]["opposite"], "U2",
            mouves_dir[R]["-"], "U'", mouves_dir[R]["+"],
            "U'", mouves_dir[R]["opposite"]]


def twenty_four(cube: Corner):
    print("24")
    R = get_R_corner_top(cube['corner']["index"])
    # 24
    # mouves = 	y' U2 R2 U2 (R U R' U) R2
    return [y_prime_mouve_dir["U2"], y_prime_mouve_dir[mouves_dir[R]["opposite"]],
            y_prime_mouve_dir["U2"], y_prime_mouve_dir[mouves_dir[R]["+"]],
            y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["-"]],
            y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["opposite"]],]


def twenty_five(face_dir: str, adjacent_face_dir: str):
    R = face_dir
    F = adjacent_face_dir
    print("25")
    # 25
    # mouves =U' (R F R' F') (R U R')
    return ["U'", mouves_dir[R]['+'], mouves_dir[F]['+'],
            mouves_dir[R]['-'], mouves_dir[F]['-'],
            mouves_dir[R]['+'], "U", mouves_dir[R]['-']]


def twenty_six(face_dir: str, adjacent_face_dir: str):
    R = adjacent_face_dir
    F = face_dir
    print("26")
    # 26
    # mouves = U (R U' R') (F R' F' R)
    return ["U", mouves_dir[R]["+"], "U'",  mouves_dir[R]["-"],
            mouves_dir[F]["+"],  mouves_dir[R]["-"],
            mouves_dir[F]["-"],  mouves_dir[R]["+"]]


def twenty_seven(adjacent_face_dir: str):
    R = adjacent_face_dir
    print("27")
    # 27
    # mouves =(R U' R' U)(R U' R')
    return [mouves_dir[R]["+"], "U'", mouves_dir[R]["-"],
            "U", mouves_dir[R]["+"], "U'", mouves_dir[R]["-"]]


def thirty(cube: Corner):
    print("30")
    R = cube["corner"]["face"].dir
    # 30
    # mouves = 	(R U R' U')(R U R')
    return [mouves_dir[R]['+'], "U", mouves_dir[R]['-'], "U'",
            mouves_dir[R]['+'], "U", mouves_dir[R]['-']]


def thirty_one(cube: Corner):
    print("31")
    R = get_R_corner_top(cube['corner']["index"])
    # 31
    # mouves = 	(R U' R' U) y' (R' U R)
    return [mouves_dir[R]["+"], "U'", mouves_dir[R]["-"], "U",
            y_prime_mouve_dir[mouves_dir[R]["-"]], y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["+"]]]


def thirty_two(cube: Corner):
    print("32")
    R = get_R_corner_top(cube['corner']["index"])
    # 32
    # mouves = (R U R' U')(R U R' U')(R U R')
    return [mouves_dir[R]["+"], "U", mouves_dir[R]["-"], "U'",
            mouves_dir[R]["+"], "U", mouves_dir[R]["-"], "U'",
            mouves_dir[R]["+"], "U", mouves_dir[R]["-"]]


def thirty_three(cube: Corner):
    print("33")
    R = cube["corner_j"]["face"].dir
    # 33
    # mouves = (U' R U' R') U2 (R U' R')
    return ["U'", mouves_dir[R]["+"], "U'", mouves_dir[R]["-"],
            "U2", mouves_dir[R]["+"], "U'", mouves_dir[R]["-"]]


def thirty_four(cube: Corner):
    print("34")
    R = cube["corner"]["face"].dir
    # 34
    # mouves = 	U (R U R') U2 (R U R')
    return ["U", mouves_dir[R]["+"], "U", mouves_dir[R]["-"], "U2", mouves_dir[R]["+"], "U", mouves_dir[R]["-"]]


def thirty_five(cube: Corner):
    print("35")
    R = cube["corner_j"]["face"].dir
    F = cube["corner"]["face"].dir
    # 35
    # mouves = U2 (R U' R') U' (F' U' F)
    return ["U2", mouves_dir[R]["+"], "U'",
            mouves_dir[R]["-"], "U'",
            mouves_dir[F]["-"], "U'", mouves_dir[F]["+"]]


def thirty_six(cube: Corner):
    print("36")
    R = cube["corner"]["face"].dir
    F = cube["corner_j"]["face"].dir
    # 36
    # mouves = U F' U' F U' (R U R')
    return ["U", mouves_dir[F]["-"], "U'",
            mouves_dir[F]["+"], "U'", mouves_dir[R]["+"],
            "U", mouves_dir[R]["-"]]


def thirty_eight(cube: Corner):
    print("38")
    R = cube["corner_j"]["face"].dir
    # 38
    # mouves = (R U' R') d (R' U2 R) U2' (R' U R)
    return [mouves_dir[R]["+"], "U'", mouves_dir[R]["-"], "d",
            mouves_dir[R]["-"], "U2", mouves_dir[R]["+"],
            "U2", mouves_dir[R]["-"], "U", mouves_dir[R]["+"]]


def thirty_nine(cube: Corner):
    print("39")
    R = cube["corner"]["face"].dir
    # 39
    # mouves = (R U' R') d (R' U' R)(U' R' U' R)
    return [mouves_dir[R]["+"], "U'", mouves_dir[R]["-"], "d",
            mouves_dir[R]["-"], "U'", mouves_dir[R]["+"],
            "U'", mouves_dir[R]["-"], "U'", mouves_dir[R]["+"]]


def forty(cube: Corner):
    print("40")
    R = cube["corner"]["face"].dir
    # 40
    # mouves = (R U R') U2 (R U' R' U)(R U R')
    return [mouves_dir[R]["+"], "U", mouves_dir[R]["-"], "U2",
            mouves_dir[R]["+"], "U'", mouves_dir[R]["-"], "U",
            mouves_dir[R]["+"], "U", mouves_dir[R]["-"]]


def forty_one(cube: Corner):
    print("41")
    R = cube["corner_j"]["face"].dir
    # 41
    # mouves = (R U' R') d (R' U' R U')(R' U' R)
    return [mouves_dir[R]["+"], "U'", mouves_dir[R]["-"], "d",
            mouves_dir[R]["-"], "U'", mouves_dir[R]["+"],
            "U'", mouves_dir[R]["-"], "U'", mouves_dir[R]["+"]]


def forty_two(cube: Corner):
    print("42")
    R = cube["corner_i"]["face"].dir
    # 42
    # mouves = (R U' R' U) d (R' U' R U') (R' U R)
    return [mouves_dir[R]["+"], "U'", mouves_dir[R]["-"], "U", "d",
            mouves_dir[R]["-"], "U'", mouves_dir[R]["+"],
            "U'", mouves_dir[R]["-"], "U'", mouves_dir[R]["+"]]


def get_R_corner_top(idx: tuple):
    match idx:
        case (0, 0):
            return 'Front'
        case (0, 2):
            return 'Right'
        case (2, 0):
            return 'Left'
        case (2, 2):
            return 'Bottom'
