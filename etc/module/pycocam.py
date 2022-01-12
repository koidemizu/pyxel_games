import math
import pyxel


class Pycocam:
    __PI = 3.141
    __PI2 = 6.283

    def __init__(self, width, height):
        self._theta = None
        self.z = 0
        self.focallength = 5
        self.fov = 45
        self.theta = 0
        self.width = width
        self.height = height

    @property
    def theta(self):
        return self._theta

    @theta.setter
    def theta(self, v):
        v %= self.__PI2
        self._theta = v

    def line(self, p1, p2, col):
        try:
            px_1 = self._coordstopx(self._perspective(p1))
            px_2 = self._coordstopx(self._perspective(p2))
        except ZeroDivisionError:
            return
        pyxel.line(px_1[0], px_1[1], px_2[0], px_2[1], col)

    def point(self, p, col):
        try:
            px = self._coordstopx(self._perspective(p))
        except ZeroDivisionError:
            return
        pyxel.pset(px[0], px[1], col)

    def _perspective(self, p):
        x, y, z = p
        y *= -1

        x_rot = x * math.cos(self.theta) - z * math.sin(self.theta)
        z_rot = x * math.sin(self.theta) + z * math.cos(self.theta)

        dz = z_rot - self.z

        m_xz = x_rot / dz
        m_yz = y / dz

        out_z = self.z + self.focallength
        out_x = m_xz * out_z
        out_y = m_yz * out_z
        return (out_x, out_y)

    def _map(self, v, a, b, c, d):
        return ((v - a) / (b - a)) * (d - c) + c

    def _coordstopx(self, coords):
        x, y = coords
        radius = self.focallength * math.tan(self.fov / 2 / 360)
        pixel_x = self._map(x, -radius, radius, 0, self.width)
        pixel_y = self._map(y, -radius, radius, 0, self.height)
        return (pixel_x, pixel_y)