import unittest
from weapon import Weapon
from Exception import NoAmmunitionError


class TestWeapon(unittest.TestCase):

    def test_fire_at_no_ammunition(self):
        # Créer une arme avec 0 munitions
        weapon = Weapon(ammunitions=0, range=10)

        # Utiliser un décorateur de contexte pour intercepter l'exception
        with self.assertRaises(NoAmmunitionError) as context:
            weapon.fire_at(1, 2, 3)

        # Vérifier que l'exception a le bon message
        self.assertEqual(str(context.exception), "Out of ammunition: 0")


if __name__ == '__main__':
    unittest.main()
