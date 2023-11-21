from weapon import Weapon
from Exception import OutOfRangeError


class Lance_missiles_anti_air(Weapon):
    def __init__(self):
        super().__init__(ammunitions=40, range=20)

    def fire_at(self, x: int, y: int, z: int):
        self.z = z
        if self.z > 0:
            print("tir autorisé ")

        else:
            super().fire_at(x, y, z)
            raise OutOfRangeError("hors de la zone de tir!")
