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
* ****

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

