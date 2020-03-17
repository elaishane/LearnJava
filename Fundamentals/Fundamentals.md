# Python Fundamentals

## Comments:
* __Comments__ are any text to the right of # symbol and is mainly useful as notes for the reader of the program.
* Comments explain __Assumptions__,__Important Decisions__,__Important Details__,__Problems__ you are trying to solve.
* __Note:__ Python does not have multi-line comment

## Identifier:
* Identifier is a name given to programming elements like variables,functions strings,etc.
* Identifer Rules:
  * Name can contain any A-Z,a-z,0-9,_(underscore).
  * Name cannot begin with digits
  * Names are case-sensitive
  * Keywords should be in lower case

| Code      | Result |
| :-----------: | :-----------: |
|  and = 20      | SyntaxError: Invalid Syntax       |
| 1abc = 20   | SyntaxError: Invalid Syntax       |
| _abc = 20 | OK|
| _ = 20| OK|


## Naming Conventions:

* Package/Module/Class/Variable/Functions Names should start with all lower case letters. Multiple words should be seperated with _.
* Constants should be in all upper case letters. Multiple words should be seperated with _.

## Data Types:
* Python has following standard data types:
  * Numbers -> int,float
  * String -> str
  * Boolean -> bool
  * List -> list
  * Tuple -> tuple
  * Set -> set
  * Dictionary -> dict

## Variables:
* Variables are programming elements whose value can changes during the execution of the program.
* type() method would return the class of the object specified.

### Note:
1. Python does not have char datatype
2. Python does not support any constant declaration.


### Numbers:

* Number data types store numeric values.
* Number objects are created when you assign a value to them.
* Python supports following types:
  * int (signed integers)
  * float (floating point real values)
  * complex(complex numbers)

### Integers:

* Integers are positive and negative whole numbers and have unlimited precision.
* Integers can be written in Decimal(Base 10)
* Octal(Base 8),Hexadecimal(Base 16) and Binary(Base 2)
  

  **Hex**-> start with 0x or 0X followed by 0-9 & A-F/a-f.
  **Octal**-> start with 0o or 0O followed by 0-7.
  **Binary**-> start with 0b or 0B followed by 0-1.

### Floating Point:

* Floating point numbers have a decimal point and/or optional signed exponent e/E
  
  ```python
  a = 1.23
  print(a)

  '''
  Output: 1.23
  '''
  ```

  ```python
  b = 4.2e2
  print(b)
  '''
  Output: 420
  '''
  ```

  ```python
  c = 4.2e-2
  print(c)
  '''
  Output: 0.042
  '''
  ```