from rubik_class import RubiksCube

valid_moves = ['U', 'D', 'F', 'B', 'L', 'R']



if __name__ == "__main__":

    cube = RubiksCube()

    
    cube.pretty_print()

    cube.rotate_face_clockwise('F')
    cube.pretty_print()

    cube.rotate_face_counterclockwise('F')
    cube.pretty_print()

    cube.rotate_face_clockwise('F')
    cube.pretty_print()

    cube.rotate_face_clockwise('F')
    cube.pretty_print()