import unittest

from household import Address

# Tests can be run with `python -m unittest` from the base project directory


class TestEquality(unittest.TestCase):

  def test_simple_equals(self):
    A = Address("123 Example St", "Seattle", "WA")
    B = Address("123 Example St", "Seattle", "WA")
    self.assertEqual(A, A)
    self.assertEqual(A, B)

  def test_simple_not_equals(self):
    A = Address("123 Example St", "Seattle", "WA")
    B = Address("456 Some Other Lane", "San Francisco", "CA")
    self.assertNotEqual(A, B)

  def test_simple_not_equals_street(self):
    A = Address("123 Example St", "Seattle", "WA")
    B = Address("456 Some Other Lane", "Seattle", "WA")
    self.assertNotEqual(A, B)

  def test_simple_not_equals_city(self):
    A = Address("123 Example St", "Seattle", "WA")
    B = Address("123 Example St", "San Francisco", "WA")
    self.assertNotEqual(A, B)

  def test_simple_not_equals_state(self):
    A = Address("123 Example St", "Seattle", "WA")
    B = Address("123 Example St", "Seattle", "CA")
    self.assertNotEqual(A, B)


class TestHashability(unittest.TestCase):

  def test_address_hashable(self):
    A = Address("123 Example St", "Seattle", "WA")
    B = Address("456 Some Other Lane", "Seattle", "WA")
    C = Address("123 Example St", "San Francisco", "WA")
    D = Address("123 Example St", "Seattle", "CA")
    E = Address("456 Some Other Lane", "San Francisco", "CA")
    addresses = {A, B, C, D, E}
    self.assertEqual(len(addresses), 5)
    self.assertTrue(A in addresses)

  def test_address_hash_stable(self):
    A = Address("123 Example St", "Seattle", "WA")
    B = Address("456 Some Other Lane", "Seattle", "WA")
    self.assertEqual(len({A, B, A, A, A, B}), 2)
