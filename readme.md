# Evan Minsk's Expeditors Take-Home Exercise

Run with `$ python main.py input.csv`. (Alternatively: `$ cat input.csv | python main.py`.)

Run tests with `$ python -m unittest` from the base of this repo.

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
