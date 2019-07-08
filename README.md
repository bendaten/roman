# Extended Roman Numerals System

## Original System

The ancient Romans did not recognize **zero** as a number, nor did they consider negative numbers. Therefore their
system started with 1.

### Symbols:

* Level ones
  * I = 1
  * V = 5
  * X = 10
  
* Level tens
  * X = 10
  * L = 50
  * C = 100
  
* Level hundreds
  * C = 100
  * D = 500
  * M = 1000
  
### Convention

In each level the convention is a list of symbols based on the level
- 1 = [1]
- 2 = [1,1]
- 3 = [1,1,1]
- 4 = [1,2]
- 5 = [2]
- 6 = [2,1]
- 7 = [2,1,1]
- 8 = [2,1,1,1]
- 9 = [1,3]

For example the number 1 is in the ones level and and has the convention of [1] = 1 is the first symbol from that
level 'I', therefore 1 is represented by the symbol 'I'.

On that level the number 3 has the convention [1,1,1] and therefor it will be represented by 'III'

The number 4 uses the [1,2] convention and so it will be represented by 'IV' and 9 by 'IX'

Now the number 200 is in the hundreds level and uses the convention [1,1] so it is represented by 'CC' and 900 by 'CM'

### Combine

The resulting strings are placed from left to right where the highest level is on the left.

- 111 = 100 + 10 + 1 = 'C X I'
- 888 = 'DCCC LXXX VIII'
- 999 = 'CM XC IX'

### Highest number

We can still use 'M's to represent numbers on the thousands level but since there is no symbol for 5000 we can't
represent numbers larger or equal to 4000 since per the 4 = [1,2] convention we need the second symbol.

Therefore the largest number possible for the original system is 3999 or 'MMM CM XC IX'

_Note - the spaces between the roman 'digits' are just for clarification but 3999 should be written as 'MMMCMXCIX'_

## Extended System

In order to break the limit of the 1000 symbol or to avoid exhausting all the leters in the alphabet, we can use a
 caret '^' to the right of the symbol to multiply it by 1000. Therefore 'V^' is 5000, X^^ is 10,000,000, and L^^^^
 is 50,000,000,000,000.
 
Since the original system was not created with an extension in mind, 'M' becomes an exception since we could have
 represented 1000 by 'I^'. Due to this exception the string (or substring) 'I^' becomes illegal.
 
### Examples

- 11,111 is 'X^ M C X I'
- 9,999,999 is 'M^X^^ C^M^ X^C^ MX^ CM XC IX'

## Implementation

The class `Roman` has two static methods:
  
 ```
roman.Roman 
@staticmethod 
def convert_to_roman(number: int) -> str
Convert a decimal integer to a Roman numeral string
Params:
number – a positive integer
Returns:
the Roman numeral
Raises:
ValueError – if the number is zero or negative
```

```
roman.Roman 
@staticmethod 
def convert_to_decimal(roman: str) -> int
Convert a Roman numeral to a decimal
Params:
roman – a Roman numeral
Returns:
the resulting decimal
Raises:
ValueError – if the string is not a Roman numeral
```

The class holds a static cache and both numbers and Roman numerals are added to it during conversion. The conversion
methods check the cache first.