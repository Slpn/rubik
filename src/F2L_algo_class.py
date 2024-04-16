

from face_class import Corner


class F2L_algo:

    def is_cube_well_placed(self, cube: Corner):

        if (cube["corner_j"]["color"] == cube["corner"]["face"].color)\
                and (cube["corner_i"]["color"] == cube["corner_i"]["face"].color):
            return True

        if (cube["corner_i"]["color"] == cube["corner"]["face"].color)\
                and (cube["corner_j"]["color"] == cube["corner_j"]["face"].color):
            return True

        return False

    def is_cube_on_top(self, cube: Corner) -> bool:
        if (cube['corner']['face'].dir == 'Up' or cube['face'].dir == 'Down'):
            return False
        if (cube['corner']['index'][0] == 2):
            return True
        return False

    def is_cube_on_left(self, cube: Corner) -> bool:
        if (cube['corner']['index'][1] == 2):
            return True
        return False

    def is_cube_on_right(self, cube: Corner) -> bool:
        if (cube['corner']['index'][1] == 0):
            return True
        return False

    def is_corner_i_equals_color(self, cube: Corner) -> bool:
        if (cube["corner"]["face"].color == cube["corner_i"]["color"]):
            return True
        return False

    def is_corner_j_equals_j_color(self, cube: Corner) -> bool:
        if (cube["corner_j"]["face"].color == cube["corner_j"]["color"]):
            return True
        return False

    def is_adjacent_well_placed(self, cube: Corner) -> bool:
        adjacent_corner_i = (cube["corner_i"]["index"][0], 1)
        if (cube["corner_i"]["color"] == cube["corner_i"]["face"][adjacent_corner_i]):
            return True

        adjacent_corner_i = (1, cube["corner_i"]["index"][1])
        if (cube["corner_i"]["color"] == cube["corner_i"]["face"][adjacent_corner_i]):
            return True
        return False
