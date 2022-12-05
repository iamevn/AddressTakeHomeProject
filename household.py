from dataclasses import dataclass


@dataclass
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
