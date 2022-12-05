import unittest

from household import Address

# Tests can be run with `python -m unittest` from the base project directory


class TestEquality(unittest.TestCase):

  def test_simple_equals(self):
    A = Address('123 Example St', 'Seattle', 'WA')
    B = Address('123 Example St', 'Seattle', 'WA')
    self.assertEqual(A, A)
    self.assertEqual(A, B)

  def test_simple_not_equals(self):
    A = Address('123 Example St', 'Seattle', 'WA')
    B = Address('456 Some Other Lane', 'San Francisco', 'CA')
    self.assertNotEqual(A, B)

  def test_simple_not_equals_street(self):
    A = Address('123 Example St', 'Seattle', 'WA')
    B = Address('456 Some Other Lane', 'Seattle', 'WA')
    self.assertNotEqual(A, B)

  def test_simple_not_equals_city(self):
    A = Address('123 Example St', 'Seattle', 'WA')
    B = Address('123 Example St', 'San Francisco', 'WA')
    self.assertNotEqual(A, B)

  def test_simple_not_equals_state(self):
    A = Address('123 Example St', 'Seattle', 'WA')
    B = Address('123 Example St', 'Seattle', 'CA')
    self.assertNotEqual(A, B)


class TestHashability(unittest.TestCase):

  def test_address_hashable(self):
    A = Address('123 Example St', 'Seattle', 'WA')
    B = Address('456 Some Other Lane', 'Seattle', 'WA')
    C = Address('123 Example St', 'San Francisco', 'WA')
    D = Address('123 Example St', 'Seattle', 'CA')
    E = Address('456 Some Other Lane', 'San Francisco', 'CA')
    addresses = {A, B, C, D, E}
    self.assertEqual(len(addresses), 5)
    self.assertTrue(A in addresses)

  def test_address_hash_stable(self):
    A = Address('123 Example St', 'Seattle', 'WA')
    B = Address('456 Some Other Lane', 'Seattle', 'WA')
    self.assertEqual(len({A, B, A, A, A, B}), 2)


class TestNormalization(unittest.TestCase):

  def assertStreetNormalizes(self, unnormalized, normalized):
    """Fail if the first argument does not equal the second after
    being normalized as a street."""
    self.assertEqual(Address.normalize_street(unnormalized), normalized)

  def assertCityNormalizes(self, unnormalized, normalized):
    """Fail if the first argument does not equal the second after
    being normalized as a city."""
    self.assertEqual(Address.normalize_city(unnormalized), normalized)

  def assertStateNormalizes(self, unnormalized, normalized):
    """Fail if the first argument does not equal the second after
    being normalized as a state."""
    self.assertEqual(Address.normalize_state(unnormalized), normalized)

  def test_address_is_normalized(self):
    A = Address('123 Example St.', 'Seattle ', 'wa')
    self.assertStreetNormalizes(A.street, A.street)
    self.assertCityNormalizes(A.city, A.city)
    self.assertStateNormalizes(A.state, A.state)

  def test_normalize_state_caps(self):
    self.assertStateNormalizes('WA', 'WA')
    self.assertStateNormalizes('wa', 'WA')
    self.assertStateNormalizes('Wa', 'WA')
    self.assertStateNormalizes('wA', 'WA')
    self.assertStateNormalizes('nj', 'NJ')

  def test_normalize_state_whitespace(self):
    self.assertStateNormalizes('sd  ', 'SD')
    self.assertStateNormalizes(' WA  ', 'WA')
    self.assertStateNormalizes('              wa  ', 'WA')

  def test_normalize_city_caps(self):
    self.assertCityNormalizes('SEATTLE', 'SEATTLE')
    self.assertCityNormalizes('Seattle', 'SEATTLE')
    self.assertCityNormalizes('seattle', 'SEATTLE')
    self.assertCityNormalizes('seaTTLE', 'SEATTLE')

  def test_normalize_city_whitespace(self):
    self.assertCityNormalizes('Seattle   ', 'SEATTLE')
    self.assertCityNormalizes('        Vancouver', 'VANCOUVER')
    self.assertCityNormalizes('     Everett        ', 'EVERETT')

  def test_normalize_street_caps(self):
    self.assertStreetNormalizes('123 EXAMPLE ST', '123 EXAMPLE ST')
    self.assertStreetNormalizes('123 example st', '123 EXAMPLE ST')
    self.assertStreetNormalizes('123 Example st', '123 EXAMPLE ST')
    self.assertStreetNormalizes('123 example ST', '123 EXAMPLE ST')

  def test_normalize_street_abbreviation_periods(self):
    self.assertStreetNormalizes('123 Example st.', '123 EXAMPLE ST')
    self.assertStreetNormalizes('123 Exa.mple st.', '123 EXA.MPLE ST')
    self.assertStreetNormalizes('123 Exa.mple st', '123 EXA.MPLE ST')
    self.assertStreetNormalizes('123 Exa.mple. st.', '123 EXA.MPLE ST')
    self.assertStreetNormalizes('123 .predot st.', '123 .PREDOT ST')

  def test_normalize_street_whitespace(self):
    self.assertStreetNormalizes('123 Example st ', '123 EXAMPLE ST')
    self.assertStreetNormalizes(' 123 Example st', '123 EXAMPLE ST')
    self.assertStreetNormalizes('    123 Example st   ', '123 EXAMPLE ST')
