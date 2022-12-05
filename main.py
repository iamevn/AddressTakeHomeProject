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
  # fileinput handles opening files specified as command line args
  # and reading from stdin when no args are provided
  with fileinput.input() as f:
    reader = csv.DictReader(f, fieldnames=CSV_FIELDS)
    for row in reader:
      age = int(row["age"])
      address = Address(row['street address'], row['city'], row['state'])
      person = Person(row["firstname"], row["lastname"], age, address)
      print(person)


def needsHelp() -> bool:
  args = set(sys.argv[1:])
  return '--help' in args or '-h' in args


if __name__ == '__main__':
  if needsHelp():
    sys.stderr.write(HELP_TEXT)
    sys.exit(1)

  main()
