#!/usr/bin/env python3

import fileinput
import sys
import csv

from household import Address, Person

HELP_TEXT = """
Extract household and occupant info from provided data files.

Data files should be provided either as arguments.
If no files are specified data will be read from stdin.

Data files are expected to be CSVs with fields for:

  first name, last name, street address, city, state, age

"""

CSV_FIELDS = [
  'firstname',
  'lastname',
  'street address',
  'city',
  'state',
  'age',
]


def main():
  people = readPeople()
  households = collateHouseholds(people)

  print('# Households:')
  for address, occupants in households.items():
    print(f'{address} ({len(occupants)} occupants)')

  print('\n# Adult occupants:')
  for person in sorted(p for p in people if p.isAdult()):
    name = f'{person.firstname} {person.lastname}'
    print(f'{name} - {person.address} - age {person.age}')


def readPeople() -> list[Person]:
  """Read list of people from either csv files or stdin."""
  people: list[Person] = []
  # fileinput handles opening files specified as command line args
  # and reading from stdin when no args are provided
  with fileinput.input() as f:
    reader = csv.DictReader(f, fieldnames=CSV_FIELDS)
    for row in reader:
      try:
        age = int(row['age'])
        address = Address(row['street address'], row['city'], row['state'])
        person = Person(row['firstname'], row['lastname'], age, address)
        people.append(person)
      except (TypeError, ValueError) as e:
        sys.stderr.write(f'Error processing row {row}\n{e}\n\n')
  return people


def collateHouseholds(people: list[Person]) -> dict[Address, list[Person]]:
  """group given people by shared addresses and return as a dict."""
  households: dict[Address, list[Person]] = {}
  for person in people:
    if person.address in households:
      households[person.address].append(person)
    else:
      households[person.address] = [person]
  return households


def needsHelp() -> bool:
  args = set(sys.argv[1:])
  return '--help' in args or '-h' in args


if __name__ == '__main__':
  if needsHelp():
    sys.stderr.write(HELP_TEXT)
    sys.exit(1)

  main()
