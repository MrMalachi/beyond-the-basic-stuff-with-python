# CHAPTER 05 | FINDING CODE SMELLS

## Glossary
* **Code Smell** - a source code pattern that signals potential bugs
* **Duplicate Code** - any source code that you could have created by copying and pasting some other code into your
                       program
* **Constants** - variables whose names are written in uppercase letters to indicate that their value shouldn't change 
                  after their initial assignment
* **Dead Code** - code that is unreachable or logically can never run
* **Stubs (no operation)** - placeholders for future code containing a `pass` statement within functions or classes that have yet to be
              implemented
* **Print Debugging** - the practice of placing temporary `print()` calls in a program to display the values of 
                        variables
* **List Comprehensions** - a concise way to create complex list values
* **Flag Arguments** - boolean arguments to function or method calls
* **Flag** - a value that indicates a binary setting, such as "enabled" or "disabled", and it's often represented by a 
             Boolean value (`True` or `False`)

## Duplicate Data
* The most common smell is _duplicate code_:
```python
print("Good morning!")
print("How are you feeling?")
feeling = input()
print(f"I am happy to hear that you are feeling {feeling}.")

print("Good afternoon!")
print("How are you feeling?")
feeling = input()
print(f"I am happy to hear that you are feeling {feeling}.")

print("Good evening!")
print("How are you feeling?")
feeling = input()
print(f"I am happy to hear that you are feeling {feeling}.")
```
* Generally, copying and pasting code once or twice within a program is fine, BUT start to consider deduplicating code
  when three or four copies exist is more efficient by creating a function and using a for loop to iterate through a 
  list:
```python
def ask_feeling(time_of_day):
    print(f"Good {time_of_day}!")
    print("How are you feeling?")
    feeling = input()
    print(f"I am happy to hear that you are feeling {feeling}.")

for time_of_day in ["morning", "afternoon", "evening"]:
    ask_feeling(time_of_day)
```
* Duplicate code is a code smell because it makes your code harder to change consistently

## Magic Numbers
* Some of the numbers that appear in your source code can confuse other programmers (or you a couple of weeks after 
  writing them)
```python
expiration = time.time() + 604800
```
* Instead of wondering what the significance of the `expiration` variable's expiration date, you can replace the "magic"
  numbers with _constants_
```python
# Set up constants for different time amounts
SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR   = 60 * SECONDS_PER_MINUTE
SECONDS_PER_DAY    = 24 * SECONDS_PER_HOUR
SECONDS_PER_WEEK   = 7  * SECONDS_PER_DAY

--snip--

expiration = time.time() + SECONDS_PER_WEEK  # Expire in one week
```
* Using separate constants allows you to easily change their variables value in the future
* Note that constat variables should never change values while the program is running
* The term _magic number_ can also apply to non-numeric values:
```python
while True:
    print("Set solar panel direction:")
    direction = input.lower()
    if direction in ("north", "south", "east", "west"):
        break

print(f"Solar panel heading set to: {direction}")
if direction == "nrth":
    print("Warning: Facing north is inefficient for this panel.")
```
* The typo bug in the `nrth` string in the program above is syntactically correct, and the program does not crash. 
  However, if constants are used and the same typo was made, it would cause the program to crash because Python would
  notice that a `NRTH` constant does not exist:
```python
# Set up constants for each cardinal direction
NORTH = "north"
SOUTH = "south"
EAST = "east"
WEST = "west"

while True:
    print("Set solar panel direction: ")
    direction = input().lower()
    if direction in (NORTH, SOUTH, EAST, WEST):
        break

print(f"Solar panel heading set to: {direction}")
if direction == "NRTH":
    print("Warning: Facing north is inefficient for this panel.")
```
* The `NameError` exception is now raised when the program is run because of the `NRTH` typo
* _Magic numbers_ are a code smell because they don't convey their purpose, making your code less readable, harder to
  update, and prone to undetectable typos
* The solution is to use constant variables

## Commented-Out Code and Dead Code
* If commented-out code remains in place, it's a complete mystery why it was removed and under what condition it might
  ever be needed again
* _Dead code_ is misleading because programmer's reading it assume it's an active part of the program when it's 
  effectively the same as commented-out code
* _Stubs_ are an exception to these code smells
* Alternatively, you can implement within a function with a `raise` `NotImplemenetedError` statement
* To fix these code smells, use a version control so you can remove the code from your program and, if needed, easily 
  add it back later

## Print Debugging
* _Print debugging_ is deceptively quick and simple, but often requires multiple iterations of rerunning the program 
  before you display the information you need to fix your bug
* The solution: use a debugger or set up logfiles for your program
  * By using a _debugger_, you can run your programs one line of code at a time and inspect any variable. It will save 
    you time in the long run
  * _Longfiles_ can record large amounts of information from your program so you can compare one run of it to previous 
    run
    * In Python, the `logging` module provides the functionality you need to easily create logfiles by using just three
      line of code
    ```python
    import logging
    logging.basicConfig(filename='log_filename.txt', level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')
    logging.debug('This is a log message')
    ```
* After importing the `logging` module and setting up its basic configuration, you can call `logging.debug()` to write
  information to a text files, as opposed to using `print()` to display it onscreen

## Variables with Numeric Suffixes
* When writing programs, you might need multiple variables that store the same kind of data. In those cases, do not 
  lazily add a numeric suffix to it
  * Ex). `password`, `password2`
* Be more descriptive instead:
  * Ex). `password`, `confirm_password` 
* If you're using numeric suffixes for a series of variables, consider replacing them with a data structure, such as a
  list or dictionary

## Classes That Should Just Be Functions or Modules
* Compared to other languages, Python uses a casual approach to organizing code, because its code isn't required to 
  exist in a class or other boilerplate structure

## List Comprehensions Within List Comprehensions
* Nested list comprehensions (or nested set and dictionary comprehensions) cram a lot of complexity into a small amount 
  of code, making your code hard to read

## Empty except Blocks and Poor Error Messages
* Catching exceptions is one of the primary ways to ensure that your programs will continue to function even when 
  problems arise
* When an exception is raised but there is no `except` block to handle it, the Python program crashes by immediately 
  stopping. This could result in losing your unsaved work or leaving files in a half-finished state
* Handling exceptions with poor messages is another code smell because the user needs enough information to know how to 
  fix the problem 
* Error messages are for the user, not the programmer, and should explain what happened as well as what the user should 
  do about it

## Code Smell Myths

### *Myth: Functions Should Have Only One return Statement at the End*
* Trying to achieve a single `return` statement per function or method often requires a convoluted series of `if-else` 
  statements that's far more confusing that having multiple `return` statements

### *Myth: Functions Should Have at Most One try Statement*
* "Functions and methods should do one thing" - separation of concerns, is good advice in general. But taking this to 
  mean that exception handling should occur in a separate function goes too far

### *Myth: Flag Arguments Are Bad*

### *Myth: All Global Variables Are Bad*
* More like, Global _Constant_ Variables Are Bad is a myth

### *Myth Comments Are Unnecessary*

