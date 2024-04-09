from enum import Enum


class CubeType(Enum):
    EDGE = 'edge'
    CORNER = 'corner'
    CENTER = 'center'


# class Cube:
#     def __init__(self, cube_type: CubeType, main: str, edge: str = None, corner: str = None) -> None:
#         if cube_type == "corner" and corner == None:
#             raise Exception('Corner cubes should have corner color')

#         if cube_type != "corner" and corner != None:
#             raise Exception('Not corners cubes should not have corner color')

#         if cube_type == "edge" and edge == None:
#             raise Exception('Edge cubes should have edge color')

#         if cube_type == "center" and (corner != None or edge != None):
#             raise Exception(
#                 'Center cubee should not have edge or corner color')

#         self.type = type
#         self.main = main
#         self.edge = edge
#         self.corner = corner
