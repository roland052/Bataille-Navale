from weapon import Weapon
from Exception import OutOfRangeError


class Lance_missile_antisurface(Weapon):

    def __init__(self):
        super().__init__(ammunitions=50, range=100)

    def fire_at(self, x: int, y: int, z: int):
        if z != 0:
            super().fire_at(x, y, z)
            raise OutOfRangeError("la cible n'est pas admissible")
        else:
            print("la cible est atteignable")
