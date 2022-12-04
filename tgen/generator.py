from math import floor
import opensimplex

SIZE = WIDTH, HEIGHT = 1000, 1000
SCALE = 0.1

BASE_HEAT_PERIOD = 1000

def triangle_wave(n: float, period: float) -> float:
    return 2 * abs(n / period - floor(n / period + 0.5))

def get_base_heat(x: float, z: float) -> float:
    # return 2 * abs(z / BASE_HEAT_PERIOD - floor(z / BASE_HEAT_PERIOD + 1 / 2))
    return triangle_wave(z, BASE_HEAT_PERIOD)

def get_noise_heat(x: float, z: float) -> float:
    return (opensimplex.noise2(x / 100, z / 100) + 1) / 2


def get_global_heat(x: float, z: float) -> float:
    return get_base_heat(x, z) * get_noise_heat(x, z)


def get_height(x: float, z: float) -> float:
    return get_global_heat(x, z) * 255
