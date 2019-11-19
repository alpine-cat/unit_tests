import unittest
from unittest.mock import patch, Mock
from units import Soldier


class TestSoldiers(unittest.TestCase):
    def test_if_soldier_xp_is_not_int(self):
        s = Soldier()
        s.xp = 'jmdf'
        self.assertIsInstance(s.xp, int)
    
    def test_if_soldier_xp_is_more_than_50(self):
        s = Soldier()
        s.xp = 100
        self.assertNotEqual(s.xp, 100)
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
        self.assertEqual(s1.xp, 1)

    def test_attack_cooldown_is_1_soldier_not_active(self):
        s1 = Soldier()
        s2 = Soldier()
        s1.attack(s2)
        self.assertFalse(s1.is_active)

    def test_soldier_is_active(self):
        s = Soldier()
        self.assertTrue(s.is_active)

    @patch("units.Soldier.attack_chance")
    def test_if_attack_chance_less_than_05(self, mock):
        mock.return_value = 0.1
        s = Soldier()
        s2 = Soldier()
        s.attack(s2)
        self.assertEqual(s2.hp, 100)

    def test_if_attack_chance_more_than_05(self):
        s1 = Soldier()
        s2 = Soldier()
        exp = s1.xp
        s1.attack_chance = Mock(return_value=0.6)
        s1.damage = Mock(return_value=8.5)
        s1.attack(s2)
        self.assertEqual(s2.hp, 91.5)
        self.assertEqual(s1.xp, exp+1)
        self.assertFalse(s1.is_active)


if __name__ is '__main__':
    unittest.main()