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

  def __repr__(self):
    return f'Address({self.street}, {self.city}, {self.state})'


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

  def _is_valid_operand(self, other):
    return (hasattr(other, "firstname") and
            hasattr(other, "lastname") and
            hasattr(other, "age"))

  def __lt__(self, other):
    if not self._is_valid_operand(other):
      return NotImplemented
    return ((self.lastname, self.firstname, self.age) <
            (other.lastname, other.firstname, other.age))

  def isAdult(self) -> bool:
    return self.age >= 18
