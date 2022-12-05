# Evan Minsk's Expeditors Take-Home Exercise

Run with `$ python main.py input.csv`. (Alternatively: `$ cat input.csv | python main.py`.)

Run tests with `$ python -m unittest` from the base of this repo.

(Requires Python version >= 3.6

## Assignment
 
### Exercise Summary:

This Developer Design and Development exercise is used in the evaluation process for potential new hire candidates.  Please approach this exercise as you would approach a design and development project at work and include unit tests.  Any documentation or explanations about your approach and assumptions are helpful.  Please send a link to your code repository when you are complete. 

### Requirements:

Write a standalone executable or script using the language of your preference (Java is the primary dev language at Expeditors).  Given the provided input data, print the expected output to the console or write to a text file.

### Input data:

```
"Dave","Smith","123 main st.","seattle","wa","43"
"Alice","Smith","123 Main St.","Seattle","WA","45"
"Bob","Williams","234 2nd Ave.","Tacoma","WA","26"
"Carol","Johnson","234 2nd Ave","Seattle","WA","67"
"Eve","Smith","234 2nd Ave.","Tacoma","WA","25"
"Frank","Jones","234 2nd Ave.","Tacoma","FL","23"
"George","Brown","345 3rd Blvd., Apt. 200","Seattle","WA","18"
"Helen","Brown","345 3rd Blvd. Apt. 200","Seattle","WA","18"
"Ian","Smith","123 main st ","Seattle","Wa","18"
"Jane","Smith","123 Main St.","Seattle","WA","13"
```

### Expected output:
 
Each household and number of occupants, followed by:
Each First Name, Last Name, Address and Age sorted by Last Name then First Name where the occupant(s) is older than 18

## Example output:

```
$ python main.py input.csv
# Households:
123 MAIN ST, SEATTLE, WA (4 occupants)
234 2ND AVE, TACOMA, WA (2 occupants)
234 2ND AVE, SEATTLE, WA (1 occupants)
234 2ND AVE, TACOMA, FL (1 occupants)
345 3RD BLVD APT 200, SEATTLE, WA (2 occupants)

# Adult occupants:
George Brown - 345 3RD BLVD APT 200, SEATTLE, WA - age 18
Helen Brown - 345 3RD BLVD APT 200, SEATTLE, WA - age 18
Carol Johnson - 234 2ND AVE, SEATTLE, WA - age 67
Frank Jones - 234 2ND AVE, TACOMA, FL - age 23
Alice Smith - 123 MAIN ST, SEATTLE, WA - age 45
Dave Smith - 123 MAIN ST, SEATTLE, WA - age 43
Eve Smith - 234 2ND AVE, TACOMA, WA - age 25
Ian Smith - 123 MAIN ST, SEATTLE, WA - age 18
Bob Williams - 234 2ND AVE, TACOMA, WA - age 26
```

## Notes

I broke this down into a few parts:

1. Read data from input.
2. Model required types as a couple simple classes.
3. Turn input into objects of these classes and perform some validation and normalization.
4. Group people by their address and output formatted clearly.

I organized these parts into small tasks and [created tickets](https://github.com/iamevn/AddressTakeHomeProject/issues?q=is%3Aissue)
for each.

The main wrinkle I noticed was that addresses in the input would need to be normalized since
the input contained similar addresses with different punctuation and capitalization
(e.g. `"123 main st "` and `"123 Main St."`).
I found the USPS's [Postal Addressing Standards](https://pe.usps.com/text/pub28/welcome.htm) which seemed like a good reference
and decided that I would normalize addresses by converting each part (street address, city, state) to allcaps and removing excess
whitespace. Then also further normalize the street address part by removing any `"."` and `","` from the end of words since
the USPS standard for abbreviations is to not include a `"."` at the end and for [secondary unit designators](https://pe.usps.com/text/pub28/28c2_003.htm) to not have a preceeding comma.

### Assumptions

For a real project I'd request clarifiaction on thse by either directly asking the appropriate person
or by calling these out in a design doc to be reviewed.

- Street suffixes ("ST", "AVE", etc.) are already abbreviated. It's true for the provided input but if this isn't true then
I'd need to implement further normalization by replacing common suffixes ([USPS has a nice table](https://pe.usps.com/text/pub28/28apc_002.htm)) with their abbreviated form.

- The state field in the input wouldn't require further normalization like abbreviation from name to two-letter code.

- The exact format for the address pre-normalization doesn't need to be tracked. If it did, I'd add fields to the `Address` class
for the raw display values while still using the normalized version for hashing and comparisons.

- People won't occur in the input multiple times. Could have built a set of `People` from the input instead of a list
if they did occur multiple times and should only be counted once.

- "older than 18" in the requirements means `age >= 18` since that's the common cutoff for things and age is continuous.
People often say things like "18 and a half" suggesting that you are exactly 18 at only a single pointin time .
If this isn't true the check in `Person.isAdult()` would need to change to use `>` rather than `>=`
(and the associated tests adjusted to have the boundary 1 higher).
 
- Output format is flexible, I went with more human-readable style but could have output as CSV like the input if this
were a tool in some pipeline.

- Input not malformed and if input is malformed then erroring out without processing the rest of input is okay.
