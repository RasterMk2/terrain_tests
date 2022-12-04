from abc import ABC, abstractmethod
from math import floor


def get_neighbor_coords(x: int, y: int) -> list[tuple[int, int]]:
    coords = []
    for x_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            coords.append((x + x_offset, y + y_offset))

    return coords

class Voronoi(ABC):
    @abstractmethod
    def get_nearest_point(self, x: float, y: float):
        pass

    @abstractmethod
    def get_cell_coords(self, x: float, y: float):
        pass


class VoronoiGrid(Voronoi):
    width: int
    height: int
    cells: list[list[tuple[float, float]]]

    def __init__(self, width: int, height: int, cells: list[list[tuple[float, float]]] = None):
        self.width = width
        self.height = height

        if cells is not None:
            self.cells = cells
        else:
            self.cells = [[(0, 0) for _ in range(width)] for _ in range(height)]

    def get_cell(self, x: int, y: int) -> tuple[float, float] | None:
        try:
            return self.cells[y][x]
        except IndexError:
            return None

    def get_cell_coords(self, x: float, y: float) -> tuple[int, int]:
        cell_x = floor(x * self.width)
        cell_y = floor(y * self.height)

        return cell_x, cell_y

    def get_nearest_point(self, x: float, y: float):
        points = []

        for coord in get_neighbor_coords(*self.get_cell_coords(x, y)):
            print(coord)
