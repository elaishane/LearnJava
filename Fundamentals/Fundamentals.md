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