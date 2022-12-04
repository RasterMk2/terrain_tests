from PIL import Image
from itertools import product
from tgen import generator, voronoi

#
# def coord_iterable_2d(width: int, height: int):
#     return product(range(width), range(height))
#
#
# def main():
#     img = Image.new('L', generator.SIZE)
#
#     for x, y in coord_iterable_2d(*generator.SIZE):
#         img.putpixel(
#             (x, y),
#             int(generator.get_height(x, y))
#         )
#
#     img.save('img.png')

def main():
    field = voronoi.VoronoiGrid(10, 10)

    field.get_nearest_point(0.5, 0.5)