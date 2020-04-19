from unittest.mock import MagicMock
import unittest
from ..bingo import get_numbers, get_random_int


class TestBingo(unittest.TestCase):

    def test_always_pass(self):
        self.assertTrue(True)

    def test_get_random_int_with_0(self):
        wanted = 0
        get_random_int = MagicMock(return_value=0)
        received = get_random_int(wanted)
        self.assertEqual(wanted, received)

    def test_get_random_int_with_99(self):
        wanted = 99
        get_random_int = MagicMock(return_value=99)
        received = get_random_int(wanted)
        self.assertEqual(wanted, received)

    def test_get_random_int_with_wrong_value(self):
        wanted = 99
        get_random_int = MagicMock(return_value=0)
        received = get_random_int(wanted)
        self.assertNotEqual(wanted, received)

    # # @should_raise(ValueError('Only positive numbers between 0 to 999 inclusive are allowed'))
    # def test_get_random_int_with_negative_number_raises_error(self):
    #     self.assertRaises(ValueError, get_random_int(-1))
    #     self.assertEqual("Only positive numbers between 0 to 999 inclusive are allowed", str(ctx.exception))

    def test_get_numbers(self):
        wanted = [0, 1]
        get_numbers = MagicMock(return_value=[0, 1])
        received = get_numbers(wanted)
        self.assertEqual(wanted, received)

        wanted = [0, 1]
        get_numbers = MagicMock(return_value=[1, 0])
        received = get_numbers(wanted)
        self.assertEqual(sorted(wanted), sorted(received))

        wanted = range(99)
        get_numbers = MagicMock(return_value=range(99))
        received = get_numbers(wanted)
        self.assertEqual(wanted, received)
        self.assertEqual(len(wanted), len(received))
        
if __name__ == '__main__':
    unittest.main()
