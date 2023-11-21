from Exception import OutOfRangeError
from weapon import Weapon


class Lances_torpilles(Weapon):
    def __init__(self):
        super().__init__(ammunitions=15, range=20)

    def fire_at(self, x: int, y: int, z: int):
        if z <= 0:
            print("cible atteignable")
        else:
            super().fire_at(x, y, z)
            raise OutOfRangeError("cible inatteignable")
