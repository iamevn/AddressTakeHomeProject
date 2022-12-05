import unittest

from household import Address, Person

# Tests can be run with `python -m unittest` from the base project directory


class TestEquality(unittest.TestCase):

  def setUp(self):
    self.addressA = Address("123 Example St", "Seattle", "WA")
    self.addressB = Address("456 Some Other Lane", "San Francisco", "CA")

  def test_simple_equals(self):
    A = Person("John", "Doe", 35, self.addressA)
    B = Person("John", "Doe", 35, self.addressA)
    self.assertEqual(A, A)
    self.assertEqual(A, B)

  def test_simple_not_equals(self):
    A = Person("John", "Doe", 35, self.addressA)
    B = Person("Jane", "Smith", 15, self.addressB)
    self.assertNotEqual(A, B)

  def test_not_equals_same_address(self):
    A = Person("John", "Doe", 35, self.addressA)
    B = Person("Jane", "Smith", 15, self.addressA)
    self.assertNotEqual(A, B)

  def test_not_equals_different_address(self):
    A = Person("John", "Doe", 35, self.addressA)
    B = Person("John", "Doe", 35, self.addressB)
    self.assertNotEqual(A, B)


class TestAge(unittest.TestCase):

  def setUp(self):
    self.address = Address("123 Example St", "Seattle", "WA")

  def test_isAdult(self):
    self.assertTrue(Person("John", "Doe", 9999, self.address).isAdult())
    self.assertTrue(Person("John", "Doe", 35, self.address).isAdult())
    self.assertTrue(Person("John", "Doe", 19, self.address).isAdult())
    self.assertTrue(Person("John", "Doe", 18, self.address).isAdult())

  def test_not_isAdult(self):
    self.assertFalse(Person("John", "Doe", 17, self.address).isAdult())
    self.assertFalse(Person("John", "Doe", 16, self.address).isAdult())
    self.assertFalse(Person("John", "Doe", 1, self.address).isAdult())
    self.assertFalse(Person("John", "Doe", 0, self.address).isAdult())


class TestOrdering(unittest.TestCase):

  def setUp(self):
    self.address = Address("123 Example St", "Seattle", "WA")

  def test_lastname_ordering(self):
    A = Person("John", "A", 35, self.address)
    B = Person("John", "B", 35, self.address)
    C = Person("John", "C", 35, self.address)

    self.assertLess(A, B)
    self.assertLess(A, C)
    self.assertLess(B, C)

    self.assertGreater(B, A)
    self.assertGreater(C, A)
    self.assertGreater(C, B)

    self.assertListEqual(sorted([C, A, B]), [A, B, C])
    self.assertListEqual(sorted([C, B, A]), [A, B, C])
    self.assertListEqual(sorted([C, A]), [A, C])

  def test_firstname_ordering(self):
    A = Person("A", "Smith", 35, self.address)
    B = Person("B", "Smith", 35, self.address)
    C = Person("C", "Smith", 35, self.address)

    self.assertLess(A, B)
    self.assertLess(A, C)
    self.assertLess(B, C)

    self.assertGreater(B, A)
    self.assertGreater(C, A)
    self.assertGreater(C, B)

    self.assertListEqual(sorted([C, A, B]), [A, B, C])
    self.assertListEqual(sorted([C, B, A]), [A, B, C])
    self.assertListEqual(sorted([C, A]), [A, C])

  def test_combined_ordering(self):
    A = Person("Jane", "Doe", 28, self.address)
    B = Person("John", "Doe", 27, self.address)
    C = Person("Jane", "Smith", 15, self.address)

    self.assertLess(A, B)
    self.assertLess(A, C)
    self.assertLess(B, C)

    self.assertGreater(B, A)
    self.assertGreater(C, A)
    self.assertGreater(C, B)

    self.assertListEqual(sorted([A, B, C]), [A, B, C])
    self.assertListEqual(sorted([C, A, B]), [A, B, C])
    self.assertListEqual(sorted([B, A, C]), [A, B, C])
    self.assertListEqual(sorted([C, A]), [A, C])
