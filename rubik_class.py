# color codes: W=White, R=Red, B=Blue, O=Orange, G=Green, Y=Yellow
class RubiksCube:
    def __init__(self):
        self.cube = self.reset_cube()

    def reset_cube(self):
        return {
            'U': [['W']*3 for _ in range(3)],
            'D': [['Y']*3 for _ in range(3)],
            'F': [['R']*3 for _ in range(3)],
            'B': [['O']*3 for _ in range(3)],
            'L': [['G']*3 for _ in range(3)],
            'R': [['B']*3 for _ in range(3)]
        }
    
    def rotate_face_counterclockwise(self, face):
        if face == 'F':
            old_state = self.cube[face]
            new_state = [[None]*3 for _ in range(3)]

            for i in range(3):
                for j in range(3):
                    new_state[j][2-i] = old_state[i][j]
            self.cube[face] = new_state

            temp_top = self.cube['U'][2]
            temp_left = [self.cube['L'][i][2] for i in range(3)]
            temp_bottom = self.cube['D'][0]
            temp_right = [self.cube['R'][i][0] for i in range(3)]

            self.cube['U'][2] = temp_left[::-1]
            self.cube['D'][0] = temp_right[::-1]
            for i in range(3):
                self.cube['L'][i][2] = temp_bottom[2-i]
                self.cube['R'][i][0] = temp_top[i]

        self.cube[face] = new_state
    def rotate_face_clockwise(self, face):
        old_state = self.cube[face]
        new_state = [[None]*3 for _ in range(3)]

        # Rotate the face itself
        for i in range(3):
            for j in range(3):
                new_state[j][2-i] = old_state[i][j]

        self.cube[face] = new_state

        # Now handle the adjacent edges for the 'F' face clockwise rotation
        if face == 'F':
            temp_top = self.cube['U'][2]
            self.cube['U'][2] = [self.cube['L'][i][2] for i in reversed(range(3))]
            self.cube['L'][0][2], self.cube['L'][1][2], self.cube['L'][2][2] = self.cube['D'][0]
            self.cube['D'][0] = [self.cube['R'][i][0] for i in range(3)]
            self.cube['R'][0][0], self.cube['R'][1][0], self.cube['R'][2][0] = temp_top[::-1]

        

    def check_solved(self):
        for face in self.cube:
            for row in self.cube[face]:
                for color in row:
                    if color != row[0]:
                        return False
        return True

    def pretty_print(self):
        print("U face:")
        for i in range(3):
            print(' '*3, end='')
            for j in range(3):
                print(self.cube['U'][i][j], end=' ')
            print()
        print("F face surrounded by L, R, and B:")
        for i in range(3):
            for face in ['L', 'F', 'R', 'B']:
                for j in range(3):
                    print(self.cube[face][i][j], end=' ')
                print(' ', end='')
            print()
        print("D face:")
        for i in range(3):
            print(' '*3, end='')
            for j in range(3):
                print(self.cube['D'][i][j], end=' ')
            print()
        print("\n")

    # def solve_cross(self):
    #     target_color = 'W'
    #     for edge in find_edges(target_color):
    #         position_edge_correctly(edge)


    def solve_f2l(self):
        pass

    def solve_oll(self):
        pass

    def solve_pll(self):
        pass