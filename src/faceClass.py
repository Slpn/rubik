from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import ForwardRef
from types_1 import Color, Direction, Edge, Edges
import numpy as np


@dataclass
class Slice(ABC):

    orientation: Direction = field(init=False)
    edges: Edges = field(default=None, init=False)
    conf: np.array[Color] = field(init=False)
    color = Color

    @abstractmethod
    def define_edge(self):
        pass

    @abstractmethod
    def rotate(self):
        pass


class UpSlice(Slice):

    def __post_init__(self) -> None:
        self.orientation = Direction.UP
        self.conf = np.full((3, 3), Color.WHITE)
        self.color = Color.WHITE

    def define_edge(self, edges: Edges):
        if (self.edges == None):
            self.edges = edges

    def rotate(self):
        pass


class DownSlice(Slice):

    def __post_init__(self) -> None:
        self.orientation = Direction.DOWN
        self.conf = np.full((3, 3), Color.YELLOW)
        self.color = Color.YELLOW

    def define_edge(self, edges: Edges):
        if (self.edges == None):
            self.edges = edges

    def rotate(self):
        pass


class LeftSlice(Slice):

    def __post_init__(self) -> None:
        self.orientation = Direction.LEFT
        self.conf = np.full((3, 3), Color.ORANGE)
        self.color = Color.ORANGE

    def define_edge(self, edges: Edges):
        if (self.edges == None):
            self.edges = edges

    def rotate(self):
        pass


class RightSlice(Slice):

    def __post_init__(self) -> None:
        self.orientation = Direction.RIGHT
        self.conf = np.full((3, 3), Color.RED)
        self.color = Color.RED

    def define_edge(self, edges: Edges):
        if (self.edges == None):
            self.edges = edges

    def rotate(self):
        pass


class BottomSlice(Slice):

    def __post_init__(self) -> None:
        self.orientation = Direction.BOTTOM
        self.conf = np.full((3, 3), Color.BLUE)
        self.color = Color.BLUE

    def define_edge(self, edges: Edges):
        if (self.edges == None):
            self.edges = edges

    def rotate(self):
        pass


class FrontSlice(Slice):

    def __post_init__(self) -> None:
        self.orientation = Direction.FRONT
        self.mid = Color.GREEN
        self.conf = np.full((3, 3), Color.GREEN)
        self.color = Color.GREEN

    def define_edge(self, edges: Edges):
        if (self.edges == None):
            self.edges = edges

    def rotate(self):
        pass
