import math

class Vec3:
    def __init__(self, e0=0, e1=0, e2=0):
        self.e = [e0, e1, e2]

    def x(self):
        return self.e[0]

    def y(self):
        return self.e[1]

    def z(self):
        return self.e[2]

    def __neg__(self):
        return Vec3(-self.e[0], -self.e[1], -self.e[2])

    def __getitem__(self, i):
        return self.e[i]

    def __setitem__(self, i, value):
        self.e[i] = value

    def __iadd__(self, v):
        self.e[0] += v.e[0]
        self.e[1] += v.e[1]
        self.e[2] += v.e[2]
        return self

    def __isub__(self, v):
        self.e[0] -= v.e[0]
        self.e[1] -= v.e[1]
        self.e[2] -= v.e[2]
        return self

    def __imul__(self, t):
        self.e[0] *= t
        self.e[1] *= t
        self.e[2] *= t
        return self

    def __idiv__(self, t):
        if t == 0:
            raise ZeroDivisionError("Division by zero")
        self.e[0] /= t
        self.e[1] /= t
        self.e[2] /= t
        return self

    def length(self):
        return math.sqrt(self.length_squared())

    def length_squared(self):
        return self.e[0] * self.e[0] + self.e[1] * self.e[1] + self.e[2] * self.e[2]

    def __str__(self):
        return f"{self.e[0]} {self.e[1]} {self.e[2]}"

    def __add__(self, v):
        return Vec3(self.e[0] + v.e[0], self.e[1] + v.e[1], self.e[2] + v.e[2])

    def __sub__(self, v):
        return Vec3(self.e[0] - v.e[0], self.e[1] - v.e[1], self.e[2] - v.e[2])

    def __mul__(self, v):
        if isinstance(v, Vec3):
            return Vec3(self.e[0] * v.e[0], self.e[1] * v.e[1], self.e[2] * v.e[2])
        elif isinstance(v, (int, float)):
            return Vec3(v * self.e[0], v * self.e[1], v * self.e[2])
        else:
            raise TypeError("Unsupported operand type for multiplication")

    def __rmul__(self, t):
        return self.__mul__(t)

    def __truediv__(self, t):
        if t == 0:
            raise ZeroDivisionError("Division by zero")
        return self.__mul__(1 / t)

    def __rtruediv__(self, t):
        if self.e[0] == 0 or self.e[1] == 0 or self.e[2] == 0:
            raise ZeroDivisionError("Division by zero")
        return Vec3(t / self.e[0], t / self.e[1], t / self.e[2])

    def dot(self, v):
        return self.e[0] * v.e[0] + self.e[1] * v.e[1] + self.e[2] * v.e[2]

    def cross(self, v):
        return Vec3(
            self.e[1] * v.e[2] - self.e[2] * v.e[1],
            self.e[2] * v.e[0] - self.e[0] * v.e[2],
            self.e[0] * v.e[1] - self.e[1] * v.e[0],
        )

    def unit_vector(self):
        return self / self.length()

    def __eq__(self, v):
        if not isinstance(v, Vec3):
            return False
        return self.e == v.e

    def __ne__(self, v):
        return not self.__eq__(v)

# Type aliases for Vec3
Point3 = Vec3  # 3D point
Color = Vec3  # RGB color
