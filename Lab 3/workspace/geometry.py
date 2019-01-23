import math


class Geometry(object):

    @staticmethod
    def disk_area(radius):
        return math.pi * radius ** 2

    @staticmethod
    def ring_area(radius_inner, radius_outer):
        return math.pi * radius_outer ** 2 - math.pi * radius_inner ** 2

    @staticmethod
    def cone_surface_area(height, radius):
        return math.pi * radius * math.sqrt(radius ** 2 + height ** 2)

    @staticmethod
    def sphere_volume(radius):
        return 4/3 * math.pi * radius ** 3

    @classmethod
    def hollow_sphere_volume(cls, radius_inner, radius_outer):
        return cls.sphere_volume(radius_outer) - cls.sphere_volume(radius_inner)
