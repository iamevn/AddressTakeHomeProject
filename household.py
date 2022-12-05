import re

from dataclasses import dataclass
from functools import total_ordering


@dataclass(eq=True, frozen=True)  # generate __hash__() automatically
class Address:
  """US Address with fields for street address, city, and state.

  Instances of this class are frozen so fields can not be assigned to.

  TODO(evan): normalize fields based on
  https://pe.usps.com/text/pub28/28apc_002.htm
  """

  street: str
  city: str
  state: str

  def __post_init__(self):
    """Normalize Address values.

    This is done after __init__() is finished but before anything else
    gets a hold of the object so we can forcibly update the values
    with `object.__setattr__()` despite being frozen.
    """
    street = Address.normalize_street(self.street)
    city = Address.normalize_city(self.city)
    state = Address.normalize_state(self.state)

    object.__setattr__(self, 'street', street)
    object.__setattr__(self, 'city', city)
    object.__setattr__(self, 'state', state)

  def __repr__(self):
    return f'Address({self.street}, {self.city}, {self.state})'

  @classmethod
  def normalize_street(cls, street: str) -> str:
    """Normalize street addresses by converting to all-caps and
    cleaning abbreviations from the end of words.

    Appreviations have trailing "." characters removed.

    TODO(evan): consider further canonicalizing abbreviations
    based on USPS standards: https://pe.usps.com/text/pub28/28apc_002.htm
    """
    caps = street.upper()
    nodots = re.sub(r'\.(\W)|\.$', r'\1', caps)
    nocomma = re.sub(r',(\W)|,$', r'\1', nodots)
    singlespace = re.sub(r' +', ' ', nocomma)

    return singlespace.strip()

  @classmethod
  def normalize_city(cls, city: str) -> str:
    """Normalize cities by converting to all-caps and cleaning."""
    return city.upper().strip()

  @classmethod
  def normalize_state(cls, state: str) -> str:
    """Normalize states by converting to all-caps and cleaning.

    TODO(evan): consider mapping names to 2 letter codes (eg: Washington -> WA)
    """
    return state.upper().strip()


@dataclass(eq=True, frozen=True)
@total_ordering  # generate comparison methods from __eq__() and __lt__()
class Person:
  """Person with a first and last name, an age, and an address.

  Instances of this class are frozen so fields can not be assigned to.
  """

  firstname: str
  lastname: str
  age: int
  address: Address

  def __post_init__(self):
    """Error out early if trying to construct an invalid Person object."""
    if not isinstance(self.firstname, str):
      raise TypeError(f'firstname must be a string, got {self.firstname}')

    if not isinstance(self.lastname, str):
      raise TypeError(f'lastname must be a string, got {self.lastname}')

    if not isinstance(self.age, int):
      raise TypeError(f'age must be an integer, got {self.age}')

    if not isinstance(self.address, Address):
      raise TypeError(f'address must be an Address object, got {self.address}')

  def __repr__(self):
    return (f'Person({self.firstname}, {self.lastname},'
            f' {self.age}, {self.address})')

  def __lt__(self, other):
    if not (hasattr(other, "firstname") and hasattr(other, "lastname")):
      return NotImplemented
    return (self.lastname, self.firstname) < (other.lastname, other.firstname)

  def isAdult(self) -> bool:
    return self.age >= 18
