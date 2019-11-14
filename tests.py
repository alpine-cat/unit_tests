import unittest
from unittest.mock import patch
from units import Soldier

class TestSoldiers(unittest.TestCase):
    def test_if_soldier_xp_is_not_int(self):
        s = Soldier()
        s.xp = 'jmdf'
        self.assertIsInstance(s.xp, int)
    
    def test_if_soldier_xp_is_more_than_50(self):
        s = Soldier()
        s.xp = 100
        self.assertNotEqual(s.xp,100)
        self.assertEqual(s.xp, 50)

    def test_if_damage_more_than_hp(self):
        s = Soldier()
        s.get_damage(150)
        self.assertEqual(s.hp, 0)

    def test_if_hp_is_str(self):
        """Тест не должен отработать"""
        s = Soldier()
        s.hp = 'i'
        self.assertEqual(s.hp, 'i')

    def test_if_damage_is_float(self):
        s = Soldier()
        s.get_damage(4.5)
        self.assertEqual(s.hp, 95.5)

    def test_attack_xp_raise(self):
        s1 = Soldier()
        s2 = Soldier()
        s1.attack(s2)
        self.assertEqual(s1.xp,1)

    def test_attack_cooldown_is_1_soldier_not_active(self):
        s1 = Soldier()
        s2 = Soldier()
        s1.attack(s2)
        self.assertFalse(s1.is_active)

    def test_soldier_is_active(self):
        s = Soldier()
        self.assertTrue(s.is_active)


if __name__ is '__main__':
    unittest.main()