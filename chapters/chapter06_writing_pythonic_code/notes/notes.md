# CHAPTER 06 | WRITING PYTHONIC CODE

## Glossary
* **Escape Character (\)** - the backslash is used as an escape character, allowing the insertion of characters that are 
  otherwise difficult or "illegal" to use in a string 
  * Ex). Single Quote - `print('It\'s a great day!')` --> It's a great day!
* **Raw Strings** - string literals that have an `r` prefix, and they don't treat the backslash characters as escape 
                    characters. Instead, they just put the backslashes back into the string
* **String Formatting (String Interpolation)** - _f-strings_ are the process of creating strings that include other 
                                                 strings and has had a long history in Python
* **Shallow Copy** - a new compound object (like a list or dictionary) is created, but populates it with references to 
                     the objects found in the original. _Basically, any changes made to a copy of the object do NOT 
                     reflect in the original object_
* **Interpolate** - to insert (something of a different nature) into something else. In this context, a formatted string
* **Ternary Expression** - a _conditional expression_ is a concise, one-line way to evaluate a condition and return one 
                           of two values
* **`in`** - a membership operator used to determine if a specific value exits within a collection or sequence such as 
             a tuple 
* **`timeit`** - a built-in module used to accurately measure the execution time of small code snippets

## The Zen of Python
```python
import this
```

## Learning to Love Significant Indentation
* Grouping blocks of Python code using indentation can seem odd, because other languages begin and end their blocks 
  with braces, { and }
  * But programmers in non-Python languages usually indent their blocks too, just like Python programmers, to make their
    code more readable
* Python does not have _significant whitespace_, because Python doesn't restrict how you can use non indentation 
  whitespace (both 2 + 2 and 2+2 are valid Python expressions)
```shell
>>> from __future__ import braces
  File "<python-input-1>", line 1
    from __future__ import braces
                           ^^^^^^
SyntaxError: not a chance
```

## Commonly Misused Syntax
* Carrying habits from other programming languages you may have learned is very common, but it is important to follow
  Python conventions

### *Use enumerate() Instead of range()*
* The following example is less Pythonic and more complicated to read:
```shell
>>> # UnPythonic Example
>>> animals = ["cat", "dog", "moose"]
>>> for i in range(len(animals)):
...     print(i, animals[i])
...     
0 cat
1 dog
2 moose
```
* Calling `enumerate()` instead to iterate over a sequence directly are preferable to using the old-fashioned 
  `range(len())`:
```shell
>>> # Pythonic Example
>>> animals = ["cat", "dog", "moose"]
>>> for i, animal in enumerate(animals):
...     print(i, animal)
...     
0 cat
1 dog
2 moose
```
* If you need only the items but not the indexes, you can still directly iterate over the list in a Pythonic way:
```shell
>>> # Pythonic Example
>>> animals = ["cat", "dog", "moose"]
>>> for animal in animals:
...     print(animal)
...     
cat
dog
moose
```

### *Use the with Statement Instead of open() and close()*
```shell
>>> # UnPythonic Example
>>> fileObj = open("spam.txt", "w")
>>> fileObj.write("Hello, world!")
13
>>> fileObj.close()
```
* Writing code this way can lead to unclosed files if, say, an error occurs in a `try` block and the program skips the 
  call to `close()`. For example:
```shell
>>> try:
...     fileObj = open("spam.txt", "w")
...     eggs = 42 / 0  # A zero divide error happens here.
...     fileObj.close()  # This line never runs.
... except:
...     print("Some error occurred")
...     
Some error occurred
```
* Instead, use the `with` statement to automatically call `close()` when the xecution leaves the `with` statement's 
  block:
```shell
>>> with open("spam.txt", "w") as fileObj:
...     fileObj.write("Hello, world!")
...
```
* Even there is no specific call to `close()`, the `with` statement will know to call it when the execution leaves the 
  block

### *Use is to Compare with None Instead of ==*
* Whenever you compare a value to `None`, you should almost always use the `is` operator rather than the `==` operator
* Using `is None` checks for object identity (a unique identifier assigned to an object when it is created)
* You should NOT use the `is` operator with the values `True` and `False`. Instead, use the `==` operator to comapre a 
  value with `True` or `False`

## Formatting Strings

### *Use Raw Strings If Your String Has Many Backslashes*
* Raw strings aren't a different string data type, they're just a convenient way to type string literals that contain 
  several backslash characters

**Input:**
```python
# Normal string interprets \n as a newline
print("Normal string: Line 1\\nLine 2")

# Raw string treats \n as literal characters
print(r"Raw string: Line 1\nLine 2")
```
**Output:**
```python
Normal string: Line 1
Line 2
Raw string: Line 1\nLine 2
```
* Raw strings basically just ignore escape characters, printing the string literally (the exact way to typed it)

### *Format Strings with F-Strings*
* Originally, the `+` operator concatenated strings together, but this resulted in many quotes and pluses
* The `format()` string methods adds the _Format Specification Mini-Language_, which involves using `{}` brace pairs in
  a way similar to the `%s` conversion specifier. However, the method is somewhat convoluted and can produce unreadable 
  code
* _F-strings_ (format strings) offer a more convenient way to create strings that include other strings
* Because you can put variable names and expressions inline inside the string, your code becomes more readable than 
  using the old ways of string formatting

## Making Shallow Copies of Lists
* If you omit both indexes from a list `[:]`, the starting index is `0` (the start of the list) and the ending index 
  defaults to the end of the list
  * This effectively creates a copy of the list:
  ```shell
  >>> spam = ["cat", "dog", "rat", "eel"]
  >>> eggs = spam[:]
  >>> eggs
  ['cat', 'dog', 'rat', 'eel']
  >>> id(spam) == id(eggs)
  False
  ```
* Notice that the identities of the lists in `spam` and `eggs` are different. The `eggs = spam[:]` line creates a 
  _shallow copy_ of the list in `spam`, whereas `eggs = spam` would copy only the reference to the list. But the `[:]` 
  looks a bit odd, and using the `copy` module's `copy()` function to produce a shallow copy if the list is more 
  readable:
```shell
>>> # Pythonic Example
>>> import copy
>>> spam = ["cat", "dog", "rat", "eel"]
>>> eggs = copy.copy(spam)
>>> id(spam) == id(eggs)
False
```
* Keep in mind, using both of these methods create _shallow copies_

## Pythonic Ways to Use Dictionaries
* Dictionaries are the core of many Python programs because of the flexibility that key-vale pairs provide by mapping 
  one piece of data to another

### *Use get() and setdefault() with Dictionaries*
* Trying to access a dictionary key that doesn't exist results in a `KeyError`, so programmers often write unPythonic 
  code to avoid the situation like this:
```python
# UnPythonic Example 
number_of_pets = {"dogs": 2}
if "cats" in number_of_pets:  # Check if 'cats' exist as a key.
    print("I have", number_of_pets["cats"], "cats.")
else:
    print("I have 0 cats.")
```
* This pattern happens so often that dictionaries have a get() method that allows you to specify a default value to 
  return when a key doesn't exist in the dictionary
```python
# Pythonic Example Using get() method
number_of_pets = {"dogs": 2}
print(f"I have {number_of_pets.get("cats", 0)} cats.")
```
* The `number_of_pets.get("cats", 0)` call checks whether the key `'cats'` exists in the `number_of_pets` dictionary. If
  it does, the method returns the value for the `'cats'` key. If it doesn't, it returns the second argument, `0`, 
  instead
* Using the `get()` method to specify a default value to use for nonexistent keys is shorter and more readable than 
  using `if-else` statements
* Conversely, you might want to set a default value if a key doesn't exist
* For example, if the dictionary in `number_of_pets` doesn't have a `'cats'` key, the instruction 
  `number_of_pets["cats"] += 10` would result in a `KeyError` error. So you might want to add code that checks for the 
  key's absence AND sets a default value:
```python
# UnPythonic Example
number_of_pets = {"dogs": 2}
if "cats" not in number_of_pets:
    number_of_pets["cats"] = 0

number_of_pets["cats"] += 10
number_of_pets["cats"]
```
* But this pattern is also common, so dictionaries have a more Pythonic `setdefault()` method. The following code is 
  equivalent to the previous:
```python
# Pythonic Example Using setdefault() method
number_of_pets = {"dogs": 2}
number_of_pets.setdefault("cats", 0)  # Does nothing if 'cats' exists.

number_of_pets["cats"] += 10
number_of_pets["cats"]
```
* If you're writing `if` statements that check whether a key exists in a dictionary and sets a default value if the key 
  is absent, use the `setdefult()` method instead

### *Use collections.defaultdict* for Default Values
* You can use the `collections.defaultdict` class to eliminate `KeyError` errors entirely
* This class lets you create a default dictionary by importing the `collections` module and calling 
  `collections.defaultdict()`, passing it a data type to use for a default value
* For example, yby passing `int` to `collections.defaultdict()`, you can make a dictionary-like object that uses `0` 
  for a default value of nonexistent keys:
```shell
>>> import collections
>>> scores = collections.defaultdict(int)
>>> scores
defaultdict(<class 'int'>, {})
>>> scores["John"] += 1  # No need to set a value for the 'John' key first.
>>> scores
defaultdict(<class 'int'>, {'John': 1})
>>> scores["Zoe"]  # No need to set a value for the 'Zoe' key first.
0
>>> scores["Zoe"] += 40 
>>> scores
defaultdict(<class 'int'>, {'John': 1, 'Zoe': 40})
```
* You can also pass `list` to use an empty list as the default value:
```shell
>>> import collections
>>> books_read_by = collections.defaultdict(list)
>>> books_read_by["John"].append("Dune Book 1")
>>> books_read_by["John"].append("The Black Box")
>>> len(books_read_by["John"])
2
>>> len(books_read_by["Zoe"])  # The default is an empty list.
0
```
* If you need a default for every possible key, it's much easier to use `collections.defaultdict()` that to use a 
  regular dictionary and constantly call the `setdefault` method

### *Use Dictionaries Instead of a switch Statement*
* A switch statement in other programming languages is a sort of `if-elif` chain that runs code based on which one of 
  many values a specific variable contains
* Some Python programmers prefer to set up a dictionary value instead of using `if-elif` statements because it's more 
  concise
```python
holiday = {"Winter": "New Year's Day",
           "Spring": "May Day",
           "Summer": "Juneteenth",
           "Fall": "Halloween"}.get("season", "Personal day off")
```
* Using a dictionary will result in more concise code, BUT it can also make your code harder to read

## Conditional Expression: Python's "Ugly" Ternary Operator
* _Ternary operators_ (officially called _conditional expressions_), evaluate an expression to one of two values based 
  on a condition. Normally you would do this with a Pythonic `if-else` statement:
```shell
>>> # Pythonic Example
>>> condition = True
>>> if condition:
...     message = "Access granted"
... else:
...     message = "Access denied"
... 
>>> message
'Access granted'
```
* It is called _ternary_ because it consists of exactly three conditions:
```python
age = 20
status = "Adult" if age >= 18 else "Minor"
```
* Conditional expressions aren't exactly Pythonic, but they're not UnPythonic either

## Working with Variable Values
* You'll often need to check and modify the values that variables store. Python has several ways of doing this

### *Chaining Assignment and Comparison Operators*
* When you have to check whether a number is within a certain range, you might use the Boolean `and` operator like this:
```python
# UnPythonic Example
if 42 < spam and spam < 99:
```
* But Python lets you chain comparison operators so you don't need to use the `and` operator. The following code is 
  equivalent to the previous example:
```python
# Pythonic Example
if 42 < spam < 9:
```
* The same applies to chaining the `=` assignment operator. You can set multiple variables to the same value in a single
  line of code:
```shell
# Pythonic Example
>>> spam = eggs = bacon = "string"
>>> spam == eggs == bacon == "string"
True
```
* Chaining operators is a small but useful shortcut in Python, but usingn them incorrectly can cause problems leading 
  to bugs

### *Checking Whether a Variable Is One of Many Values*
* You may come across needing to check whether a single variable is one of multiple possible values. You can do this 
  using the `or` operator:
```python
>>> spam == "cat" or spam == "dog" or spam == "moose"
```
* But all of those redundant `spam ==` parts make this expression a bit unwieldy
* Instead, you cn put multiple values into a tuple and check for whether a variable's value exists in that tuple using 
  the `in` operator:
```python
>>> # Pythonic Example
>>> spam = "cat"
>>> spam in ("cat", "dog", "moose")
True
```
* Not only is this idiom easier to understand, it's also slightly faster, according to `timeit`