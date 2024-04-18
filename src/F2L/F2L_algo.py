from rubik_class import Opposite_mouves, RubiksCube
from face_class import Edge, Face, check_edge_color, dir_nodes, Corner
import numpy as np
from utils import CircularChainedList, get_face_to_mouve, mouves_dir, get_new_idx, inverse_mouves_dir, y_prime_mouve_dir
from vizualize import RubixVisualiser


def three(cube: Corner):
    print("3")
    R = cube['corner']["face"].dir
    # 3
    # mouves = y' (R' U' R)
    return [y_prime_mouve_dir[mouves_dir[R]["-"]],
            "U'", y_prime_mouve_dir[mouves_dir[R]["+"]]]


def four(cube: Corner):
    print("4")
    R = cube['corner']["face"].dir
    # 4
    # mouves = (R U R')
    return [mouves_dir[R]["+"],
            "U", mouves_dir[R]["-"]]


def nine(cube: Corner):
    print("9")
    R = cube['corner_j']["face"].dir
    # 9
    # mouve = U' (R U' R' U) y' (R' U' R)
    return ["U'", mouves_dir[R]["+"], "U'", mouves_dir[R]["-"],
            "U", y_prime_mouve_dir[mouves_dir[R]["-"]],
            y_prime_mouve_dir["U'"], y_prime_mouve_dir[mouves_dir[R]["+"]]]


def fourteen(cube: Corner):
    print("14")
    # 14
    # mouve = U' (R U' R' U) (R U R')
    return ["U'", mouves_dir[cube["corner"]]["+"], "U'", mouves_dir[cube["corner"]]["-"],
            "U", mouves_dir[cube["corner"]]["+"], "U", mouves_dir[cube["corner"]]["-"]]


def thirteen(cube: Corner):
    print("13")
    R = cube['corner_j']["face"].dir
    # 13
    # mouve = y' U (R' U R U') (R' U' R)
    return [y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["-"]], y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["+"]],
            y_prime_mouve_dir["U'"], y_prime_mouve_dir[mouves_dir[R]["-"]], y_prime_mouve_dir["U'"], y_prime_mouve_dir[mouves_dir[R]["+"]]]


def seventeen(cube: Corner):
    print("17")
    R = cube["corner_i"]["face"].dir
    # 17
    # mouves = 	(R U2 R') U' (R U R')
    return [mouves_dir[R]['+'], "U2", mouves_dir[R]['-'],
            "U'", mouves_dir[R]['+'], "U", mouves_dir[R]['-']]


def eighteen(cube: Corner):
    print("18")
    R = cube["corner_i"]["face"].dir
    # 18
    # mouves = 	y' (R' U2 R) U (R' U' R)
    return [y_prime_mouve_dir[mouves_dir[R]["-"]],  y_prime_mouve_dir["U2"],
            y_prime_mouve_dir[mouves_dir[R]
                              ["+"]], y_prime_mouve_dir["U"],
            y_prime_mouve_dir[mouves_dir[R]
                              ["-"]], y_prime_mouve_dir["U'"],
            y_prime_mouve_dir[mouves_dir[R]["-"]]]


def twenty_four(cube: Corner):
    print("24")
    R = cube["corner_i"]["face"].dir
    # 24
    # mouves = 	y' U2 R2 U2 (R U R' U) R2
    return [y_prime_mouve_dir["U2"], y_prime_mouve_dir[mouves_dir[R]["opposite"]],
            y_prime_mouve_dir["U2"], y_prime_mouve_dir[mouves_dir[R]["+"]],
            y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["-"]],
            y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["opposite"]],]


def twenty_six(face_dir: str, adjacent_face_dir: str):
    R = adjacent_face_dir
    F = face_dir
    print("26", face_dir)
    # 26
    # mouves = U (R U' R') (F R' F' R)
    mouves = ["U", mouves_dir[R]["+"], "U'",  mouves_dir[R]["-"],
              mouves_dir[F]["+"],  mouves_dir[R]["-"],
              mouves_dir[F]["-"],  mouves_dir[R]["+"]]


def twenty_seven(adjacent_face_dir: str):
    R = adjacent_face_dir
    print("27")
    # 27
    # mouves =(R U' R' U)(R U' R')
    mouves = [mouves_dir[R]["+"], "U'", mouves_dir[R]["-"],
              "U", mouves_dir[R]["+"], "U'", mouves_dir[R]["-"]]


def thirty_one(cube: Corner):
    print("31")
    R = cube["corner_j"]["face"].dir
    # 31
    # mouves = 	(R U' R' U) y' (R' U R)
    return [mouves_dir[R]["+"], "U'", mouves_dir[R]["-"], "U",
            y_prime_mouve_dir[mouves_dir[R]["-"]], y_prime_mouve_dir["U"], y_prime_mouve_dir[mouves_dir[R]["+"]]]
