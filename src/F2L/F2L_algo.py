from rubik_class import Opposite_mouves, RubiksCube
from face_class import Edge, Face, check_edge_color, dir_nodes, Corner
import numpy as np
from utils import CircularChainedList, get_F_corner_bottom, get_R_corner_bottom, get_face_to_mouve, mouves_dir, get_new_idx, inverse_mouves_dir, y_prime_mouve_dir, get_R_corner_top
from vizualize import RubixVisualiser


def one(cube: Corner):
    print("1")
    R = cube['corner_j']["face"].dir
    # 1
    # mouves = U (R U' R')
    return ["U", mouves_dir[R]["+"], "U'", mouves_dir[R]["-"]], 1


def two(cube: Corner):
    print("2")
    R = cube['corner']["face"].dir
    # 2
    # mouves = y' U' (R' U R)
    return [y_prime_mouve_dir["U'"], y_prime_mouve_dir[mouves_dir[R]["-"]],
            y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["+"]]], 2


def three(cube: Corner):
    print("3")
    R = cube['corner_j']["face"].dir
    # 3
    # mouves = y' (R' U' R)
    return [y_prime_mouve_dir[mouves_dir[R]["-"]],
            y_prime_mouve_dir["U'"], y_prime_mouve_dir[mouves_dir[R]["+"]]], 3


def four(cube: Corner):
    print("4")
    R = cube['corner']["face"].dir
    # 4
    # mouves = (R U R')
    return [mouves_dir[R]["+"],
            "U", mouves_dir[R]["-"]], 4


def five(cube: Corner):
    print("5")
    R = cube['corner_j']["face"].dir
    # 5
    # mouve = (U' R U R') U2 (R U' R')
    return ["U'", mouves_dir[R]["+"], "U", mouves_dir[R]["-"],
            "U2",  mouves_dir[R]["+"], "U'",  mouves_dir[R]["-"]], 5


def six(cube: Corner):
    print("6")
    R = cube['corner']["face"].dir
    # 6
    # mouve = y' (U R' U' R) U2' (R' U R)

    return ["U", y_prime_mouve_dir[mouves_dir[R]["-"]],
            "U'", y_prime_mouve_dir[mouves_dir[R]["+"]],
            "U2", y_prime_mouve_dir[mouves_dir[R]["-"]],
            "U", y_prime_mouve_dir[mouves_dir[R]["+"]]], 6


def seven(cube: Corner):
    print("7")
    R = cube['corner_j']["face"].dir
    # 7
    # mouve = U' (R U2' R') U2 (R U' R')
    return ["U'", mouves_dir[R]["+"], "U2", mouves_dir[R]["-"],
            "U2", mouves_dir[R]["+"], "U'", mouves_dir[R]["-"]], 7


def eight(cube: Corner):
    print("8")
    R = cube['corner']["face"].dir
    # 8
    # mouve = y' U (R' U2 R) U2' (R' U R)
    return [y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["-"]],
            y_prime_mouve_dir["U2"], y_prime_mouve_dir[mouves_dir[R]["+"]],
            y_prime_mouve_dir["U2"], y_prime_mouve_dir[mouves_dir[R]["-"]],
            y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["+"]]], 8


def nine(cube: Corner):
    print("9")
    R = cube['corner_j']["face"].dir
    # 9
    # mouve = U' (R U' R' U) y' (R' U' R)
    return ["U'", mouves_dir[R]["+"], "U'", mouves_dir[R]["-"],
            "U", y_prime_mouve_dir[mouves_dir[R]["-"]],
            y_prime_mouve_dir["U'"], y_prime_mouve_dir[mouves_dir[R]["+"]]], 9


def ten(cube: Corner):
    print("10")
    R = cube['corner']["face"].dir
    # 10
    # mouve = U' (R U R' U)(R U R')
    return ["U'", mouves_dir[R]["+"], "U", mouves_dir[R]["-"],
            "U", mouves_dir[R]["+"], "U", mouves_dir[R]["-"]], 10


def eleven(cube: Corner):
    print("11")
    R = cube['corner_j']["face"].dir
    # 11
    # mouve =U' (R U2' R' U) y' (R' U' R)
    return ["U'", mouves_dir[R]['+'], "U2",
            mouves_dir[R]['-'], "U",
            y_prime_mouve_dir[mouves_dir[R]['-']], y_prime_mouve_dir["U'"],
            y_prime_mouve_dir[mouves_dir[R]['+']]], 11


def twelve(cube: Corner):
    print("12")
    R = cube['corner']["face"].dir
    # 12
    # mouve = R' U2' R2 U R2' U R
    return [mouves_dir[R]['-'], "U2", mouves_dir[R]['opposite'],
            "U", mouves_dir[R]['opposite'], "U", mouves_dir[R]['+']], 12


def thirteen(cube: Corner):
    print("13")
    R = cube['corner_j']["face"].dir
    # 13
    # mouve = y' U (R' U R U') (R' U' R)
    return [y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["-"]], y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["+"]],
            y_prime_mouve_dir["U'"], y_prime_mouve_dir[mouves_dir[R]["-"]], y_prime_mouve_dir["U'"], y_prime_mouve_dir[mouves_dir[R]["+"]]], 13


def fourteen(cube: Corner):
    print("14")
    R = cube["corner"]["face"].dir
    # 14
    # mouve = U' (R U' R' U) (R U R')
    return ["U'", mouves_dir[R]["+"], "U'", mouves_dir[R]["-"],
            "U", mouves_dir[R]["+"], "U", mouves_dir[R]["-"]], 14


def fifteen(cube: Corner):
    print("15")
    R = cube["corner_j"]["face"].dir
    # 15
    # mouves = 	y' (R' U R) U2' y (R U R')
    return [y_prime_mouve_dir[mouves_dir[R]['-']], y_prime_mouve_dir["U"],
            y_prime_mouve_dir[mouves_dir[R]['+']], y_prime_mouve_dir["U2"],
            mouves_dir[R]['+'], "U", mouves_dir[R]['-']], 15


def sixteen(cube: Corner):
    print("16")
    R = cube["corner"]["face"].dir
    F = cube["corner_j"]["face"].dir
    # 16
    # mouves = 	(R U' R') U2 (F' U' F)
    return [mouves_dir[R]["+"], "U'", mouves_dir[R]["-"],
            "U2", mouves_dir[F]["-"], "U'", mouves_dir[F]["+"]], 16


def seventeen(cube: Corner):
    print("17")
    R = get_R_corner_top(cube['corner']["index"])
    # 17
    # mouves = 	(R U2 R') U' (R U R')
    return [mouves_dir[R]['+'], "U2", mouves_dir[R]['-'],
            "U'", mouves_dir[R]['+'], "U", mouves_dir[R]['-']], 17


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
            y_prime_mouve_dir[mouves_dir[R]["+"]]], 18


def nineteen(cube: Corner):
    print("19")
    R = get_R_corner_top(cube['corner']["index"])
    # 19
    # mouves = U (R U2 R') U (R U' R')
    return ["U", mouves_dir[R]["+"], "U2", mouves_dir[R]["-"],
            "U", mouves_dir[R]["+"],  "U'", mouves_dir[R]["-"]], 19


def twenty(cube: Corner):
    print("20")
    R = get_R_corner_top(cube['corner']["index"])
    # 20
    # mouves = y' U' (R' U2 R) U' (R' U R)
    return [y_prime_mouve_dir["U'"], y_prime_mouve_dir[mouves_dir[R]["-"]], y_prime_mouve_dir["U2"],
            y_prime_mouve_dir[mouves_dir[R]["+"]], y_prime_mouve_dir["U'"],
            y_prime_mouve_dir[mouves_dir[R]["-"]], y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["+"]]], 20


def twenty_one(cube: Corner):
    print("21")
    R = get_R_corner_top(cube['corner']["index"])
    # 21
    # mouves = U2 (R U R' U)(R U' R')
    return ["U2", mouves_dir[R]["+"], "U", mouves_dir[R]["-"],
            "U", mouves_dir[R]["+"], "U'", mouves_dir[R]["-"]], 21


def twenty_two(cube: Corner):
    print("22")
    R = get_R_corner_top(cube['corner']["index"])
    # 22
    # mouves = y' U2 (R' U' R U')(R' U R)
    return [y_prime_mouve_dir["U2"], y_prime_mouve_dir[mouves_dir[R]['-']],
            y_prime_mouve_dir["U'"],  y_prime_mouve_dir[mouves_dir[R]['+']],
            y_prime_mouve_dir["U'"],  y_prime_mouve_dir[mouves_dir[R]['-']],
            y_prime_mouve_dir["U"],  y_prime_mouve_dir[mouves_dir[R]['+']]], 22


def twenty_three(cube: Corner):
    print("23")
    R = get_R_corner_top(cube['corner']["index"])
    # 23
    # mouves = U2 R2 U2 (R' U' R U') R2
    return ["U2", mouves_dir[R]["opposite"], "U2",
            mouves_dir[R]["-"], "U'", mouves_dir[R]["+"],
            "U'", mouves_dir[R]["opposite"]], 23


def twenty_four(cube: Corner):
    print("24")
    R = get_R_corner_top(cube['corner']["index"])
    # 24
    # mouves = 	y' U2 R2 U2 (R U R' U) R2
    return [y_prime_mouve_dir["U2"], y_prime_mouve_dir[mouves_dir[R]["opposite"]],
            y_prime_mouve_dir["U2"], y_prime_mouve_dir[mouves_dir[R]["+"]],
            y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["-"]],
            y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["opposite"]]], 24


def twenty_five(corner: Corner):
    R = get_R_corner_bottom(corner["corner"]["index"])
    F = get_F_corner_bottom(corner["corner"]["index"])
    print("25")
    # 25
    # mouves =R' F' R U (R U' R') F
    return [mouves_dir[R]['-'], mouves_dir[F]['-'], mouves_dir[R]['+'],
            "U", mouves_dir[R]['+'], "U'", mouves_dir[R]['-'],
            mouves_dir[F]['+']], 25


def twenty_six(corner: Corner):
    R = get_R_corner_bottom(corner["corner"]["index"])
    F = get_F_corner_bottom(corner["corner"]["index"])
    print("26")
    # 26
    # mouves = U (R U' R') (F R' F' R)
    return ["U", mouves_dir[R]["+"], "U'",  mouves_dir[R]["-"],
            mouves_dir[F]["+"],  mouves_dir[R]["-"],
            mouves_dir[F]["-"],  mouves_dir[R]["+"]], 26


def twenty_seven(cube: Corner):
    R = cube["corner_j"]["face"].dir
    print("27")
    # 27
    # mouves =(R U' R' U)(R U' R')
    return [mouves_dir[R]["+"], "U'", mouves_dir[R]["-"],
            "U", mouves_dir[R]["+"], "U'", mouves_dir[R]["-"]], 27


def twenty_eight(cube: Corner):
    R = cube["corner"]["face"].dir
    print("28")
    # 28
    # mouves =y' (R' U R U') (R' U R)
    return [y_prime_mouve_dir[mouves_dir[R]["-"]], "U", y_prime_mouve_dir[mouves_dir[R]["+"]],
            "U'", y_prime_mouve_dir[mouves_dir[R]["-"]], "U", y_prime_mouve_dir[mouves_dir[R]["+"]]], 28


def twenty_nine(cube: Corner):
    R = cube["corner_j"]["face"].dir
    print("29")
    # 29
    # mouves =y' (R' U' R U)(R' U' R)
    return [y_prime_mouve_dir[mouves_dir[R]["-"]], "U'", y_prime_mouve_dir[mouves_dir[R]["+"]],
            "U", y_prime_mouve_dir[mouves_dir[R]["-"]], "U'", y_prime_mouve_dir[mouves_dir[R]["+"]]], 29


def thirty(cube: Corner):
    print("30")
    R = cube["corner"]["face"].dir
    # 30
    # mouves = 	(R U R' U')(R U R')
    return [mouves_dir[R]['+'], "U", mouves_dir[R]['-'], "U'",
            mouves_dir[R]['+'], "U", mouves_dir[R]['-']], 30


def thirty_one(cube: Corner):
    print("31")
    R = get_R_corner_top(cube['corner']["index"])
    # 31
    # mouves = 	(R U' R' U) y' (R' U R)
    return [mouves_dir[R]["+"], "U'", mouves_dir[R]["-"], "U",
            y_prime_mouve_dir[mouves_dir[R]["-"]], y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["+"]]], 31


def thirty_two(cube: Corner):
    print("32")
    R = get_R_corner_top(cube['corner']["index"])
    # 32
    # mouves = (R U R' U')(R U R' U')(R U R')
    return [mouves_dir[R]["+"], "U", mouves_dir[R]["-"], "U'",
            mouves_dir[R]["+"], "U", mouves_dir[R]["-"], "U'",
            mouves_dir[R]["+"], "U", mouves_dir[R]["-"]], 32


def thirty_three(cube: Corner):
    print("33")
    R = cube["corner_j"]["face"].dir
    # 33
    # mouves = (U' R U' R') U2 (R U' R')
    return ["U'", mouves_dir[R]["+"], "U'", mouves_dir[R]["-"],
            "U2", mouves_dir[R]["+"], "U'", mouves_dir[R]["-"]], 33


def thirty_four(cube: Corner):
    print("34")
    R = cube["corner"]["face"].dir
    # 34
    # mouves = 	U (R U R') U2 (R U R')
    return ["U", mouves_dir[R]["+"], "U", mouves_dir[R]["-"], "U2", mouves_dir[R]["+"], "U", mouves_dir[R]["-"]], 34


def thirty_five(cube: Corner):
    print("35")
    R = cube["corner_j"]["face"].dir
    F = cube["corner"]["face"].dir
    # 35
    # mouves = U2 (R U' R') U' (F' U' F)
    return ["U2", mouves_dir[R]["+"], "U'",
            mouves_dir[R]["-"], "U'",
            mouves_dir[F]["-"], "U'", mouves_dir[F]["+"]], 35


def thirty_six(cube: Corner):
    print("36")
    R = cube["corner"]["face"].dir
    F = cube["corner_j"]["face"].dir
    # 36
    # mouves = U F' U' F U' (R U R')
    return ["U", mouves_dir[F]["-"], "U'",
            mouves_dir[F]["+"], "U'", mouves_dir[R]["+"],
            "U", mouves_dir[R]["-"]], 36


def thirty_eight(R_face: Face):
    print("38")
    R = R_face.dir
    # 38
    # mouves = (R U' R') d (R' U2 R) U2' (R' U R)
    return [mouves_dir[R]["+"], "U'", mouves_dir[R]["-"], "U",
            y_prime_mouve_dir[mouves_dir[R]["-"]
                              ], "U2", y_prime_mouve_dir[mouves_dir[R]["+"]],
            "U2", y_prime_mouve_dir[mouves_dir[R]["-"]], "U", y_prime_mouve_dir[mouves_dir[R]["+"]]], 38


def thirty_nine(cube: Corner):
    print("39")
    R = cube["corner_j"]["face"].dir
    # 39
    # mouves = (R U' R' U') R U R' U2 (R U' R')
    return [mouves_dir[R]["+"], "U'", mouves_dir[R]["-"], "U'",
            mouves_dir[R]["+"], "U", mouves_dir[R]["-"],
            "U2", mouves_dir[R]["+"], "U'", mouves_dir[R]["-"]], 39


def forty(cube: Corner):
    print("40")
    R = cube["corner"]["face"].dir
    # 40
    # mouves = (R U R') U2 (R U' R' U)(R U R')
    return [mouves_dir[R]["+"], "U", mouves_dir[R]["-"], "U2",
            mouves_dir[R]["+"], "U'", mouves_dir[R]["-"], "U",
            mouves_dir[R]["+"], "U", mouves_dir[R]["-"]], 40


def forty_one(cube: Corner):
    print("41")
    R = cube["corner_j"]["face"].dir
    F = cube["corner"]["face"].dir
    # 41
    # mouves = (F' U F) U2 (R U R' U) (R U' R')
    return [mouves_dir[F]["-"], "U", mouves_dir[F]["+"], "U2",
            mouves_dir[R]["+"], "U", mouves_dir[R]["-"],
            "U", mouves_dir[R]["+"], "U'", mouves_dir[R]["-"]], 41


def forty_two(cube: Corner):
    print("42")
    R = cube["corner"]["face"].dir
    F = cube["corner_j"]["face"].dir
    # 42
    # mouves = (R U R' U')(R U' R') U2 (F' U' F)
    return [mouves_dir[R]["+"], "U", mouves_dir[R]["-"], "U'",
            mouves_dir[R]["+"], "U'", mouves_dir[R]["-"],
            "U2", mouves_dir[F]["-"], "U'", mouves_dir[F]["+"]], 42
