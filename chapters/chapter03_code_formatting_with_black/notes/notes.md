# CHAPTER 03 | CODE FORMATTING WITH BLACK

## Glossary
* **Code Formatting** - applying a set of rules to source code to give it a certain appearance for the purpose of
                        maintainability and readability 
* **Black** - a code formatting tool that can automatically format your source code into a consistent, readable style,
              without changing your program's behavior
* **Style Guide** - a document that outlines a set of formatting rules a software project should follow
* **Indentation** - the whitespace at the beginning of a code line
* **Vertical Spacing** - the placement of blank lines between lines of code
* **`--check`** - a flag used to check formatting without modifying

## How to Lose Friends and Alienate Co-Workers
* Although you might start out coding on your own, programming is often a collaborative activity. If several programmers
  working on the same source code files write in their own style, the code can become an inconsistent mess, even if it
  runs without error... or worse, the programmers will constantly be reformatting each other's code to their own style,
  wasting time causing arguments
* Formatting using _Black_ helps to avoid these issues by automatically formatting your source code into a consistent,
  readable style, without changing your program's behavior

## Style Guides for PEP 8
* An easy way to write readable code is to follow a _style guide_, a document that outlines a set of formatting rules a
  software project should follow

## Horizontal Spacing
* Horizontal spaces help separate distinct parts of code from each other, making them easier to identify 

### *Use Space Characters for Indentation*
* _Indentation_ is the whitespace at the beginning of a code line, and you can use one of two whitespace characters:
  a space or a tab
* Because tabs represent a varying width of whitespace, you should avoid using them in your source code
* As for the length of each indentation level, the common practice in Python code is four spaces per level of indentation

### *Spacing Within a Line*
* Spaces are important for making different parts of a code line appear visually distinct

#### Put a Single Space Between Operators
* If you don't leave spaces between operators and identifiers, your code will appear to run together

#### Put No Spaces Before Separators and a Single Space After Separators
* The items lists and dictionaries, as well as the parameters in functions should be separated with commas and a single
  space after them
```python
def spam(eggs, bacon, ham):
    weights = [42.0, 3.1415, 2.718]
```
* Black automatically inserts a space after commas and removes spaces before them

#### Don't Put Spaces After a Function, Method, or Container Name
* We can readily identify function and method names because they're followed by a set of parentheses, so don't put
  spaces between the name and the opening parentheses

#### Don't Put Spaces After Opening Brackets or Before Closed Brackets

#### Put Two Spaces Before End-of-Line Comments
```python
print("Hello, world!")  # Display greeting.
```

## Vertical Spacing
* _Vertical spacing_ is the placement of blank lines between lines of code
* PEP 8 has several guidelines for inserting blank lines in code: it states that you should not separate functions with
  two blank lines, and methods within a class with one blank line

### *A Vertical Spacing Example*
* What Black _can't_ do is decide where blank lines within your functions, methods, or global scope should go
  * Which of those lines to group together is a subjective decision that is up to the programmer

### *Vertical Spacing Best Practices*
* One of Python's lesser-known features is that you can use a semicolon to separate multiple statements on a single line
```python
print("What is your name?"); name = input()
```
* But just because this is technically more _Pythonic_, does not make it more readable, therefore, Black splits these
  statements into separate lines
* PEP 8 also recommends that you split import statements per module:
```python
import math
import os
import sys
```

## Black: The Uncompromising Code Formatter
* Black automatically formats the code inside your _.py_ files
* You can't change many of the rules that Black follows, which is why it's described as "the uncompromising code 
  formatter"

### *Installing Black*
* Install Black using the `pip` tool that comes with Python inside a virtual environment:
```shell
(bb_venv) malachibrown@Malachis-iMac beyond-the-basic-stuff-with-python % python -m pip install black
```
* The `-m` flag stands for module-name, and allows you to run a package without needing to know exactly where it's
  installed on your computer
* Note, if you want to use `pip` to install it to the user account use:
```shell
(bb_venv) malachibrown@Malachis-iMac beyond-the-basic-stuff-with-python % python3 -m pip install --user black
```

### *Running Black from the Command Line*
```shell
(bb_venv) malachibrown@Malachis-iMac chapter02_environment_setup_and_command_line % python -m black test_script.py 
reformatted test_script.py

All done! ✨ 🍰 ✨
1 file reformatted.
```
* If you want to run Black over every _.py_ file in a folder, specify a single folder instead of an individual file:
```shell
(bb_venv) malachibrown@Malachis-iMac chapters % python -m black .
reformatted /Users/malachibrown/dev/learning/beyond-the-basic-stuff-with-python/chapters/chapter01_dealing_with_errors_asking_for_help/exercises/zeroDivideTraceback.py
reformatted /Users/malachibrown/dev/learning/beyond-the-basic-stuff-with-python/chapters/chapter01_dealing_with_errors_asking_for_help/exercises/abcTraceback.py

All done! ✨ 🍰 ✨
2 files reformatted, 1 file left unchanged.
```

#### Adjusting Black's Line Length Setting
* The history of the 80 character line dates back to the era of punch card computing in the 1920s when IBM introduced
  punch cards that had 80 columns and 12 rows.
* But, modern-day high resolution screens can display text that is more than 80 characters wide, so if you want to tell
  Black to format your code with, for example, a 120-character line-length limit, use the `l 120` command line option:
```shell
(bb_venv) malachibrown@Malachis-iMac exercises % python -m black -l 120 abcTraceback.py 
reformatted abcTraceback.py

All done! ✨ 🍰 ✨
1 file reformatted.
```

#### Disabling Black's Double Quoted String Setting
* Black automatically changes any string literals in your code from using single quotes to double quotes unless the
  string contains double quote characters
* Use the `-S` command line option (flag) to make sure Black does not change the type of quotes you use:
```shell
(bb_venv) malachibrown@Malachis-iMac exercises % python -m black -S abcTraceback.py 
```

#### Previewing the Changes Black Will Make
* Although Black won't rename your variables or change your program's behavior, you might not like the style changes
  Black makes
* If you want to stick to your original formatting, you could either use version control for your source code, maintain
  your own backups, or even easier, you can preview the changes Black would make without letting it actually alter your
  files by running Black with the `--diff` command line option:
```shell
(bb_venv) malachibrown@Malachis-iMac exercises % python -m black --diff abcTraceback.py 
```
* Note, there is no way to undo a change when using Black! You need to either make backup copies if your source code or
  use version control software, such as Git, before running Black


### *Disabling Black for Parts of Your Code*
* By adding `# fmt: off` and `# fmt: on` comments, you can tell Black ro turn off its code formatting for these lines
  and then resume code formatting afterward:
```python
# Set up constants for different time amounts:
# fmt: off
SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR   = 60 * SECONDS_PER_MINUTE
SECONDS_PER_DAY    = 24 * SECONDS_PER_HOUR
SECONDS_PER_WEEK   = 7  * SECONDS_PER_DAY
# fmt: on
```
* Running Black on this file now won't affect the unique spacing, or any other formatting, in the code between these two
  comments
* Note, good formatting can be invisible, but poor formatting can make reading code frustrating 








