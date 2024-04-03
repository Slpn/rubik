

from faceClass import BottomSlice, DownSlice, FrontSlice, LeftSlice, RightSlice, UpSlice, Slice
from types_1 import Color, Direction
import numpy as np


class Rubik:

    def __init__(self):
        self.upSlice = UpSlice()
        self.downSlice = DownSlice()
        self.rightSlice = RightSlice()
        self.leftSlice = LeftSlice()
        self.frontSlice = FrontSlice()
        self.bottomSlice = BottomSlice()

        up_down_edges = {
            Direction.LEFT: self.leftSlice,
            Direction.RIGHT: self.rightSlice,
            Direction.FRONT: self.frontSlice,
            Direction.BOTTOM: self.bottomSlice
        }
        self.upSlice.define_edge(up_down_edges)
        self.downSlice.define_edge(up_down_edges)

        left_right_edges = {
            Direction.UP: self.upSlice,
            Direction.DOWN: self.downSlice,
            Direction.FRONT: self.frontSlice,
            Direction.BOTTOM: self.bottomSlice
        }
        self.leftSlice.define_edge(left_right_edges)
        self.rightSlice.define_edge(left_right_edges)

        front_bottom_edges = {
            Direction.UP: self.upSlice,
            Direction.DOWN: self.downSlice,
            Direction.LEFT: self.leftSlice,
            Direction.RIGHT: self.rightSlice
        }
        self.frontSlice.define_edge(front_bottom_edges)
        self.bottomSlice.define_edge(front_bottom_edges)
