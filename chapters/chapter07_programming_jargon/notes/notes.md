# CHAPTER 07 | PROGRAMMING JARGON

## Glossary
* **Python Interpreter** - the actual software that reads the text of a _.py_ file and carries out its instructions
* **Implementation** - software created to follow a specification
* **Compiler** - a software that translates computer code written in one programming language into another language
* **Just-In-Time Compiler** - a component of a runtime environment that improves performance by compiling code into 
                              native machine code _during_ program execution, rather than _before_ running it
* **Reference Implementation** - a complete program that serves as a definitive "gold standard" for a technical 
                                 specification or standard
* **Memory Leaks** - where a programmer forgets to free memory (archaic)
* **Double-Free Bugs** - where programmers freed the same memory twice, leading to data corruption
* **Garbage Collections** - a form of automatic memory management that tracks when to allocate and free memory so the 
                            programmers doesn't have to
* **Literal** - a text in the source code for a fixed, typed-out value
* **Keywords** - set of names reserved for use as part of the language and cannot be used as variable names 
                 (that is, identifiers)
* **Object** - a representation of a piece of data, such as a number, some text, or a more complicated data structure, 
               such as a list or dictionary
* **Value** - the data the object represents, such as the integer `42` or the string `hello`
* **Identity** - refers to an object's unique "address" in the computer's memory
* **Identifier** - a user-defined name used to identify variables, functions, classes, modules, or other objects
* **Item (Element)** - an object that is inside a container object, like a list or dictionary
* **Mutable** - if you can change an object's value, it is _mutable_
* **Immutable** - if you cannot change an object's value, it is _immutable_
* **In-Place** - describes an operation that modifies an existing object directly rather than creating and returning a 
                 new one
* **Index Operator** - represented by square brackets ([]) and used to access individual elements (values) within an 
                       ordered collection, such as a string, list, or tuple
* **Index** - refers to the numerical position of an item within an ordered sequence
* **Zero-Based Indexing** - the first element of a sequence (such as a list, string, or tuple) is accessed using the 
                            index 0
* **Key-Value Pair** - the fundamental building blocks of dictionaries, it's what they're comprised of
* **Hash** - an integer that acts as a sort of fingerprint for a value
* **Hash() Function** - returns an integer hash value for an object, typically used by Python for fast lookups in 
                        dictionaries and sets
* **Container** - an object of any data type that contain multiple other objects (lists & dictionaries)
* **Sequence** - an object of any container data type with ordered values accessible through integer indexes. Strings, 
                 tuples, lists, and bytes objects are sequence data type
* **Mapping** - an object of any container data type that uses keys instead of an index
* **Dunder Methods** - (short for "double underscore") are special, predefined methods with name starting and ending 
                       with `__`
* **Module** - a Python program that other Python programs can import so they can use the module's code
* **Package** - a collection of modules that you form by placing a file named `__init__.py` inside a folder. You use the
                folder's name as the name of the package
* **Callable Operator** - the double parentheses placed after the object (`call()`)
* **Callable Object** - any object that you can call using a pair of parentheses, and optionally, a series of arguments
* **First-Class Object** - you can store them in variables, pass them as arguments in function calls, return them from
                           function calls, and do anything else you can do with an object
* **Alias(es)** - different names for existing functions
* **Expressions** - a combination of values, variables, operators, and function calls that the interpreter evaluates to 
                    produce a single value
* **Statements** - a complete instruction that the interpreter can execute to perform an action
* **Block** - begins with indentation and ends when that indentation returns to the previous indent level
* **Clause (Block)** - also reffered to as a "block", is a structural component of a compound statement 
                       (such as `if`, `while`, `for`, or `try`)
* **Clause Header** - the first line of a clause within a compound statement, beginning with a uniquely identifying 
                      keyword such as `if`, `else`, `def`, and ends with a colon (:)
* **Variable** - names that refer to objects
* **Attribute** - any name following a dot
* **Function** - a collection of code that runs when called
* **Method** - is a function (or _callable_) that is associated with a class, just as an attribute is a variable 
               associated with an object
* **Iterable Objects** - iterables are any object capable of returning its member one at a time, allowing it to be 
                         looped over using a `for` loop
* **Iterator Objects** - an iterator is an object that contains a countable number of values
* **Syntax** - the set of rules for the valid instructions in a given programming language
* **Syntax Error** - occurs when the Python interpreter encounters code that the interpreter does not understand
* **Runtime Error** - when a running program fails to perform some task, such as trying to open a file that doesn't 
                      exist or dividing a number by zero
* **Logical Error** - a _semantic_ error is a mistake that occurs when a program runs without crashing but produces the 
                    wrong output or behaves unexpectedly
* **Parameter(s)** - a placeholder variable defined in a function's signature that represents the data the function 
                   expects to receive
* **Argument(s)** - the actual value or object passed into a function or method when you call it
* **Type Casting** - the process of creating a new object based on the original object in order to assign a new data 
                     type
* **Type Coercion** - the automatic (implicit) conversion of a value from one data type to another by the interpreter 
                      during an operation
* **Attribute** - simple variables attached to an object (`obj.name = "Alice"`) and are stored directly in the object's 
                  path
* **Properties** - managed attributes that look like regular attributes to the user, but trigger hidden methods 
                   (getters and setters) when accessed or modified
* **Machine Code** - Every time you execute Python code, its first translated to bytecode, and then it's passed on to the
                     Python Virtual Machine where it's made into machine code
* **Instruction Set** - relates to how the language interacts with hardware and how the language interacts with hardware 
                        and how developers can simulate process behavior
* **Binary** - a compiled program composed of machine code
* **Bytecode** - carried out by a software interpreter program instead of directly by the CPU
* **Scripting Language** - typically interpreted at runtime, used for automation, orchestration, or glue code, and often 
                           interacts with an existing system (OS, browser app)
* **Script** - a linear sequence of instructions, executed by an interpreter, and usually tied to a specific task or 
               environment
* **Programming Language** - designed to build complete systems, manage memory, control flow, architecture, and support
                             modularity (functions, classes, packages)
* **Program** - a standalone executable system with a defined entry point (`main`, `if__name__ == "__main__":`) and 
                structured into modules, layers, and components 
* **Language** - a programming language is used for communication with a computer, in order to tell the computer what to 
                 do, how to do it, in a way it understands
* **Language Implementation** - the actual software that runs code written in that language. Implementation parses your 
                                code (checks syntax, builds an internal structure (Abstract Syntax Tree)), translates 
                                it (converts into bytecode, machine, code, intermediate form), and then executes it 
                                (runs instructions on the CPU)
* **Library** - a collection pre-written, reusable code that developers can "borrow" to perform common tasks instead of 
                having to write everything from scratch
* **Standard Library** - a collection pf pre-written code that is bundled with a programming language's installation and
                         available to all developers by default
* **Framework** - a pre-built, structured foundation of code, tools, and libraries that simplifies software development 
                  by providing a standardized reusable skeleton
* **Inversion of Control** - the flow of the program is managed by an external framework or container rather than the 
                             custom code itself
* **Software Development Kit (SDK)** - a bundled set of tools; libraries, documentation, code samples, and debuggers 
                                       that enables developers to create applications for specific platforms
* **Engine** - a software engine is a core component of a complex software system, such as game engines, physics 
               engines, recommendation engines, database engines, chess engines, and search engines
* **Application Programming Interface (API)** - a set of rules and protocols that allows different software applications
                                                to communicate and share data with each other

## Definitions
* Although computer jargon can be confusing and intimidating for new programmers, it's a necessary shorthand because 
  several terms in Python and software development have subtle differences in meaning

### *Python the Language and Python the Interpreter*
* When we say, "Python runs a program" or "Python will raise an exception", we're talking about the _Python Interpreter_
* When we say, "the Python interpreter", we're almost always talking about _CPython_, the Python interpreter maintained
  by the Python Software Foundation
* CPython is an _implementation_ of the Python language, written in C programming language
* _Jython_ is written in Java for running Python scripts that are interoperable with Java programs
* _PyPy_, a _just-in-time compiler_ for Python that compiles as programs execute, is written in Python
* All of these implementations run source code written in the _Python programming language_
* CPython is called the Python language's _reference implementation_ because if there's a difference between how CPython
  and another interpreter interpret Python code, CPython's behavior is considered canonical and correct

### *Garbage Collection*
* Memory allocation in many early programming languages was the source of numerous bugs because a programmer had to 
  instruct the program to allocate and then deallocate, or free, memory structures as needed
* To avoid bugs like _memory leaks_, or _double-free bugs_, Python has _garbage collections_
  * Think of garbage collection as memory recycling, because it makes memory available for new data
```shell
>>> def some_function():
...     print("some_function() called.")
...     spam = ["cat", "dog", "moose"]
...     
>>> some_function()
some_function() called.
```
* The programmer doesn't need to figure out how many bytes of memory to request because Python manages this 
  automatically. Python's garbage collector will free the local variables when the function call returns to make that 
  memory available for other data, making programming much easier and less bug-prone

### *Literals*
* Think of literal as a value that literally appears in source code text. Only the built-in data types can have literal 
  values in Python source code 
* Literals are a raw, fixed value (textual representations) written directly into source code, representing itself rather than stored variable or 
  calculated result

### *Keywords*
* Every programming language has its own [keywords](#glossary)

### *Objects, Values, Instances, and Identities*
* All [objects](#glossary) can be stored in variables, passed as arguments to function calls, and returned from function 
  calls
* All objects have a [value](#glossary), [identity](#glossary), and [data type](#glossary)
* Although somewhat confusing, some programmers use the term _value_ as a synonym for _object_, especially for simple 
  data types like integers or strings
  * For example: a variable that contains `42` is a variable that contains an integer value, but we can also say it's a 
                 variable that contains an integer object with a value of `42`
* An object is created with an _identity_ that is a unique integer you can view by calling the `id()` function
  * For example:
    ```shell
    >>> spam = ["cat", "dog", "moose"]
    >>> id(spam)
    4414761024
    ```
* The variable `spam` stores an object of the list data type. Its value is `["cat", "dog", "moose"]`. Its identity is 
  `4414761024`, although the integer ID varies each time a program runs so you'll likely get a different ID on your 
  computer
  * Although the data type and the object's identity will never change, an object's value can change
    * For example: adding a new object to the `spam` list may change its value, but it does not change its identity nor 
                   data type 
* Multiple [identifiers](#glossary) can refer to the same object
* In Python, all variables are technically references, not containers of values, regardless of their data type
  * Think of [variables as labels](https://www.google.com/imgres?q=think%20of%20variables%20as%20labels%20metaphor&imgurl=https%3A%2F%2Fsubstackcdn.com%2Fimage%2Ffetch%2Fw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep%2Fhttps%253A%252F%252Fsubstack-post-media.s3.amazonaws.com%252Fpublic%252Fimages%252F9e01589b-ea2b-45b0-b870-7cb56e672ae5_847x287.png&imgrefurl=https%3A%2F%2Famangaur.hashnode.dev%2Fpython-variables-are-not-boxes&docid=V7t2hJd3hhsxUM&tbnid=EXvliFCz8adU5M&vet=12ahUKEwiks86Xzc2TAxXlMlkFHeM4NF8QnPAOegQIGBAB..i&w=847&h=287&hcb=2&ved=2ahUKEwiks86Xzc2TAxXlMlkFHeM4NF8QnPAOegQIGBAB) because multiple variables can refer to the same object, that object can be "stored" in
    multiple variables
* Without understanding that the `=` assignment operator always copies the reference, not the object, you might 
  introduce bugs by thinking that you're making a duplicate copy of an object, when you're really copying the reference 
  to the original object (a copy of a copy)
* You can use the `is` operator to compare whether two object have the same identity, in contrast, the `==` operator 
  checks only whether object values are the same
    ```shell
    >>> spam is eggs
    True
    >>> bacon = {"name": "Zoe"}
    >>> spam == bacon
    True
    >>> spam is bacon
    False
    ```
* The variables `spam` and `eggs` refer to the same dictionary object, so their identities and values are the same. But 
  `bacon` refers to a separate dictionary object, even though it contains data identical to `spam` and `eggs`. The 
  identical data means `bacon` has the same value as `spam` and `eggs`, but they're two different objects with two 
  different identities

### *Items*
* For example:`["dog", "cat", "moose:]`
  * The strings in this list are called _items_

### *Mutable and Immutable*
* All objects in Python have a value, data type, and identity, and of these only the value can change
* Mutable Data Types:
  1. Lists
  2. Dictionaries
  3. Sets
  4. Bytearray
  5. Array
* Immutable Data Types:
  1. Integer
  2. Floating-Point Number (`float`)
  3. Boolean
  4. String
  5. Frozen Set
  6. Bytes
  7. Tuple
* Mutable objects can have their values modified [_in-place_](#glossary), but its _identity_ remains the same
* List concatenation creates a new list with a new identity. When this happens, the old list will eventually be freed 
  from memory by the garbage collector 
* A method that is called on an object such as `append()`, often modifies the object _in-place_

```shell
>>> bacon = "Goodbye"
>>> id(bacon)
4462405232
>>> bacon = "Hello"
>>> id(bacon)
4462405088
>>> bacon = bacon + ", world!"
>>> bacon
'Hello, world!'
>>> id(bacon)
4462390512
>>> bacon[0] = "J"
Traceback (most recent call last):
  File "<python-input-11>", line 1, in <module>
    bacon[0] = "J"
    ~~~~~^^^
TypeError: 'str' object does not support item assignment
```
* Strings are immutable, so you cannot change their value. Although it looks like the string's value in `bacon` is being 
  changed from `"Goodbye"` to `"Hello"`, it's actually being overwritten by a new string object with a new identity
* Similarly, an expression using string concatenation creates a new string object with a new identity. Attempting to 
  modify the string in-place with item assignment is not allowed in Python

```shell
>>> egss = ("cat", "dog", [2, 4, 6])
>>> id(egss)
4462322176
>>> id(egss[2])
4462379776
>>> egss[2] = egss[2] + [8, 10]
Traceback (most recent call last):
  File "<python-input-15>", line 1, in <module>
    egss[2] = egss[2] + [8, 10]
    ~~~~^^^
TypeError: 'tuple' object does not support item assignment
```
* As shown above, a tuple's value is defined as the objects it contains and the order of those objects. _Tuples_ are 
  immutable sequence objects that enclose values in parentheses. This means that items in a tuple cannot be overwritten
* BUT, a mutable list inside an immutable tuple can still be modified [_in-place_](#glossary):
```shell
>>> egss[2].append(8)
>>> egss[2].append(10)
>>> eggs
Traceback (most recent call last):
  File "<python-input-18>", line 1, in <module>
    eggs
>>> egss
('cat', 'dog', [2, 4, 6, 8, 10])
>>> id(egss)
4462322176
>>> id(egss[2])
4462379776
```
* Although this is an obscure special case, it's important to keep in mind. The tuple still refers to the same objects, 
  but if a tuple contains a mutable object and that object changes its value--that is, if the object mutates--the value 
  of the tuple also changes

### *Indexes, Keys, and Hashes*
* Python lists and dictionaries are values that contain multiple other values, and to access these values, you use an
  [index operator](#glossary) and an integer called an [index](#glossary) to specify which value you want to access
```shell
>>> spam = ["cat", "dog", "moose"]
>>> spam[0]
'cat'
>>> spam[-2]
'dog'
```
* Indexing can also be used for values other than lists, such as on a string to obtain individual characters:
```shell
>>> "Hello, world!"[0]
'H'
```
* Python dictionaries are organized into [key-value](#glossary) pairs
```shell
>>> spam = {"name": "Malachi"}
>>> spam["name"]
'Malachi'
```
* Although list indexes are limited to integers, a Python dictionary's index operator is a _key_ and can be any 
  [hashable](#glossary) object
* An object's hash (fingerprint) never changes for the lifetime of the object, and the objects with the same value must 
  have the same hash
* The string `name` in this instance is the key for the value `"Malachi"`. The `hash() function will return an object's 
  hash if the object is _hashable_ 
* Immutable objects, such as strings, integers, floats, and tuples, can be hashable. But lists 
  (as well as other mutable objects) are not hashable:
```shell
>>> hash("Hello")
2306958483081244736
>>> hash(42)
42
>>> hash(3.14)
322818021289917443
>>> hash((1, 2, 3))
529344067295497451
>>> hash([1, 2, 3])
Traceback (most recent call last):
  File "<python-input-32>", line 1, in <module>
    hash([1, 2, 3])
    ~~~~^^^^^^^^^^^
TypeError: unhashable type: 'list'
```
* A hash is different from an identity. Two different objects with the same value will have different identities but the 
  same hash:
```shell
>>> a = ("cat", "dog", "moose")
>>> b = ("cat", "dog", "moose")
>>> id(a), id(b)
(4462477616, 4462477856)
>>> id(a) == id(b)
False
>>> hash(a), hash(b)
(-5221601509188502906, -5221601509188502906)
>>> hash(a) == hash(b)
True
```
* The tuples above referred to by `a` and `b` have different identities, but their identical values mean they'll have 
  identical hashes. Note that a tuple is hashable if it contains only hashable items, and you cannot use a tuple that 
  contains an unhashable list as a key

### *Containers, Sequences, Mapping, and Set Types*
* The words [container](#glossary), [sequence](#glossary), and [mapping](#glossary) have meanings in Python that don't 
  necessarily apply to other programming languages
* Objects of _sequence_ data types can access values using integer indexes in the index operator (the [and] brackets) 
  and can also be passed to the `len()` function
* By "ordered", we mean that there is a first value, second value, and so on in the sequence
* A _mapping_ can be ordered or unordered. Dictionaries in Python 3.4 and earlier are unordered because there is no 
  first or last key-value pair in a dictionary
* Just because a dictionary is ordered doesn't mean its items are accessible through integer indexes
* Ordered dictionaries are also considered the same if they contain the same key-value pairs, even if the key-value 
  pairs are in a different order in each dictionary

### *Dunder Methods and Magic Methods*
* [Dunder Methods](#glossary), also called [magic methods](#glossary), are special methods in Python whose names begin 
  and end with two underscores 
* These methods are used for operator overloading. _Dunder_ is short for double underscore
* The most famous dunder method is `__init__()`, which initializes objects, and Python has a few dozen dunder methods

### *Modules and Packages*
* The [modules](#glossary) that come with Python are collectively called the _Python Standard Library_, but you can 
  create your own modules as well
* Packages contain multiple modules (that is, `.py` files) or other packages 
  (other folders containing `__init__.py` files)

### *Callables and First-Class Objects*
* Functions and methods aren't the only things that you can call in Python. Any object that implements the 
  [callable operator](#glossary)--the two parentheses `()`--is a [callable object](#glossary)
* For example, if you have a `def hello():` statement, you can think if the code as a variable named `hello` that 
  contains a function object. Using the callable operator on this variable calls the function in the variable: `hello()`
* Classes are an OOP concept, and a class is an example of a callable object that is not a function or method
* Functions are [_first-class objects_](#glossary) in Python - an entity that can be handled with the same flexibility 
  as any other data type like an integer or string
* Think of a `def` statement as assigning a function object to a variable. For example, you could create a `spam()` 
  function that you can then call:
```shell
>>> def spam():
...     print("Spam! Spam! Spam!")
...     
>>> spam()
Spam! Spam! Spam!
```
* You can also assign the `spam()` function object to other variables. When you call the variable you've assigned the 
  function object to, Python executes the function:
```shell
>>> egss = spam
>>> egss()
Spam! Spam! Spam!
```
* These are also called [aliases](#glossary). They're often used if you need to rename a function
* The most common use of _first-class functions_ is so you can pass functions to other functions
```shell
>>> def call_twice(func):
...     func()
...     func()
...     
>>> call_twice(spam)
Spam! Spam! Spam!
Spam! Spam! Spam!
```

## Commonly Confused Terms
* To communicate clearly with other programmers, you'll need to learn the difference between the following terms

### *Statements vs. Expressions*
* [_Expressions_](#glossary) are the instructions made up of operators and values that evaluate to a single value
* A value can be a variable (which contains a value) or a function call (which returns a value). So `2 + 2` is an 
  expression that evaluates down to the single value of `4`. But `len(my_name) > 4` and `my_name.upper()` or 
  `my_name == "Malachi"` are expressions as well
* A value by itself is also an expression that evaluates to itself
* [_Statements_](#glossary) are, effectively, all other instructions in Python
  * These include: `if` statements, `for` statements, `def` statements, `return` statements, and so on...
* Some statements can include expressions, such as an assignment statement like `spam = 2 + 2` or an `if` statement like
  `if my_name == "Malachi:"`
* Although Python 3 uses a `print()` function, Python 2 instead has a `print` statement. The difference is important to 
  note that the Python 3 `print()` function has a return value (which is always `None`), can be passed as an argument to
  other functions, and can be assigned to a variable
  * None of these actions are possible with statements, however, you can still use the parentheses in Python 2:
  ```shell
  >>> print "Hello, world!"  # run in Python 2
  Hello, world!
  >>> print("Hello, world!")  # run in Python 2
  Hello, world!
  ```
* Although this look like a function call, it's actually a `print` statement with a single string value wrapped in 
  parentheses, the same way assigning `spam = (2 + 2)` is equivalent to `spam = 2 + 2`
* A statement and an expression composed of a function call have subtle but real differences

### *Block vs. Clause vs. Body*
* The terms [_block_](#glossary), [_clause_](#glossary), and [_body_](#glossary) are often used interchangeably to refer
  to a group of Python instructions
* For example, the code that follows an `if` statement or `for` statement is called the statement's _block_. A new 
  block is required following statements that end with a colon, such as `if`, `else`, `for`, `while`, `def`, `class`, 
  and so on...
* The official Python documentation prefers the term _clause_ rather than block:
```python
if name == "Malachi":
    print("Hello, sir!")
    print("Would you like some tea?")
```
* The `if`statement above is the [_clause header_](#glossary), and the two `print()` calls nested in the `if` statement 
  are the [_clause suite_](#glossary) or [_body_](#glossary)

### *Variable vs. Attribute*
* [_Attributes_](#glossary) are associated with objects (the name before the dot/period):
```shell
>>> import datetime
>>> spam = datetime.datetime.now()
>>> spam.year
2026
>>> spam.month
4
```
* In the example above, `spam` is a variable that contains a `datetime` object (returned from `datetime.datetime.now()`)
  , and `year` and `month` are attributes of that object. Even in the case of, say, `sys.exit()`, the `exit()` function 
  is considered an attribute of the `sys` module object
* Other languages call attributes _fields_, _properties_, or _member variables_

### *Function vs. Method*
* [Functions](#glossary) include built-in functions or functions associated with a module:
```shell
>>> len("Hello")
5
>>> "Hello".upper()
'HELLO'
>>> import math
>>> math.sqrt(25)
5.0
```
* In the example above, `len()` is a function and `upper()` is a string method. [_Methods_](#glossary) are also considered
  attributes of the objects they're associated with
* Note that a period doesn't necessarily mean you're dealing with a method instead of a function. The `sqrt()` function 
  is associated with `math`, which is a module, not a class

### Iterable vs. Iterator
* [_Iterables_](#glossary) in `for` loops. Calling `range(3)` returns a range object, just like calling `list("cat")` returns a 
  list object
```shell
>>> for i in range(3):
...     print(i)  # body of the for loop
...     
0
1
2
>>> for i in ["c", "a", "t"]:
...     print(i)  # body of the for loop
...     
c
a
t
```
* Iterables also include all sequence types, such as range, list, tuple, and string objects, but also some container 
  objects, such as dictionary, set, and file objects
* However, more is going on under the hood in these `for` loop examples. Behind the scenes, Python is calling the 
  built-in `iter()` and `next()` functions for the `for` loop
* When used in a `for` loop, _iterable_ objects are passed to the built-in `iter()` function, which returns iter-_ator_ 
  objects. Although tge iterable object contains the items, the iterator object keeps track of which item is next to be 
  used in a loop. On each iteration of the loop, the iterator object keeps track of which item is next to be used in a 
  loop. On each iteration of the loop, the iterator object is passed to the built-in `next()` function to return the 
  next item in the iterable
```shell
>>> iterable_object = range(3)
>>> iterable_object
range(0, 3)
>>> iterable_object = iter(iterable_object)
>>> i = next(iterable_object)
>>> print(i)  # body of the for loop
0
>>> i = next(iterable_object)
>>> print(i)
1
>>> i = next(iterable_object)
>>> print(i)
2
>>> i = next(iterable_object)
Traceback (most recent call last):
  File "<python-input-21>", line 1, in <module>
    i = next(iterable_object)
StopIteration
```
* As shown above, an [_iterator_](#glossary) can only iterate over the items in an iterable once. This is similar to how 
  you can only use `open()` and `readline()` to read the contents of a file once before having to reopen the file to 
  read its contents again
* If you want to iterate over the iterable again, you must call `iter()` again to create another iterator object. You 
  can create as many iterator objects as you want; each will independently track the next item it should return
```shell
>>> iterable_object = list("cat")
>>> iterable_object
['c', 'a', 't']
>>> iterator_object1 = iter(iterable_object)
>>> iterator_object2 = iter(iterable_object)
>>> next(iterator_object1)
'c'
>>> next(iterator_object1)
'a'
>>> next(iterator_object2)
'c'
```
* Remember, _iterable objects_ are passed as an argument to the `iter()` function
**VS** the object returned from `iter()` is an _iterator_ object
* Iterator objects are passed to the `next()` function. When you create your own data types with `class` statements, you 
  can implement the `__iter__()` and `__next()__` special methods to use your object in `for` loops

### *Syntax vs. Runtime vs. Semantic Errors*
* There are many ways to categorize bugs, but at a high level, you could divide programming errors into three types: 
  [syntax errors](#glossary), [runtime errors](#glossary), and [semantic errors](#glossary)
* Syntax errors are also known as _parsing errors_, which occur when the Python interpreter can't parse the text of the 
  source code into valid instructions
  * In English, this error would be the equivalent of having incorrect grammar or a string of nonsense words like, 
    "by uncontaminated cheese certainly it's". Computers require specific instructions and can't read the programmer's 
    mind to determine what the program should do, so a program with a syntax error won't even run 
* A _runtime error_ in English, is the equivalent of giving an impossible instruction like, "Draw a square with three 
  sides"
  * If a runtime error is not addressed, the program will crash and display a traceback, but you can catch runtime 
    errors using `try-except` statements that run error handling code
  ```shell
  >>> slices = 8
  >>> eaters = 0
  >>> print("Each person eats", slices / eaters, "slices.")
  Traceback (most recent call last):
  File "<python-input-37>", line 1, in <module>
    print("Each person eats", slices / eaters, "slices.")
                              ~~~~~~~^~~~~~~~
  ZeroDivisionError: division by zero
  ```
* It's helpful to remember that the line number the traceback mentions is only the point at which the Python interpreter
  detected an error. The true cause of the error might be on the previous line of code or even much earlier in the 
  program 
* Syntax errors in the source code are caught by the interpreter before the program runs, but syntax errors can also 
  happen at runtime 
* A _semantic error_ (also called a _logical error_) is a more subtle bug because they won't cause error messages or 
  crashes, but the computer carries out instructions in a way the programmer didn't intend:
```shell
>>> print("The sum of 4 and 2 is", "4" + "2")
The sum of 4 and 2 is 42
```

### *Parameters vs. Arguments*
* [_Parameters_](#glossary) are the variable names between the parentheses in a `def` statement
* [_Arguments_](#glossary) are the values passed in a function call, which are then assigned to the parameters
```shell
>>> def greeting(name, species):
...     print(f"{name} is a {species}")
...     
>>> greeting("Rufus", "dog")
Rufus is a dog
```
* Remember, parameters and arguments are just other names for variables and values, respectively, when they are used in 
  this context

### *Type Coercion vs. Type Casting*
* You can convert an object of one type to an object of another type
  * For example: `int("42")` converts a string `"42"` to an integer `42`. In actuality, the string object `"42"` 
    isn't converted as much as the `int()` function creates a new integer object based in the original object
* When conversion is done _explicitly_ like this, we're _casting_ the object, although, programmers often still refer 
  to this process as converting the object
* Python will _implicitly_ do a type conversion, such as when evaluating the expression `2 + 3.0 + 5.0`. Values, such as
  `2` and `3.0`, are coerced to a common data type that the operator can work with. This conversion which is done 
  _implicitly_, is called type [_coercion_](#glossary)

### *Properties vs Attributes*
* In many languages, the terms [_property_](#glossary) and [_attribute_](#glossary) are used synonymously, but in Python 
  these words have distinct meanings
* An attribute, is a name associated with an object
* A property, allows programmers in Python to use getters and setters with much more clean syntax

### *Bytecode vs. Machine Code*
* Source code is compiled into a form of instructions called [_machine code_](#glossary) that the CPU directly carries 
  out. Machine code is composed of instructions from the CPU's [_instruction set_](#glossary)
* Python and Hardware Interaction:
  * Python is an _interpreted language_ that compiles source code into [_bytecode_](#glossary) (.pyc files). This bytecode is executed 
    by the Python Virtual Machine (PVM), which then translates it into the CPU's native instruction set (e.g., x86 ARM) 
    through underlying C functions 
* Instead of creating machine code that is carried out directly by CPU hardware, you create _bytecode_, also called 
  _portable code_ or _p-code_

### *Script vs. Program, Scripting Language vs. Programming Language*
* The difference between a script and a program, or even a scripting language and a programming language, are vague and 
  arbitrary
* One way to distinguish scripts from programs is by how the code executes
* [_Scripts_](#glossary) written in [_scripting languages_](#glossary) are interpreted directly from the source code, 
  whereas [_programs_](#glossary) written in [_programming languages_](#glossary) are compiled into binaries
* Python is commonly thought of as a scripting language, even though there is a compilation step to bytecode when a 
  Python program is run
* Meanwhile, Java isn't commonly thought of as a scripting language, even though it produces bytecode instead of machine 
  code binaries, just like Python 
* Technically, [_languages_](#glossary) aren't compiled or interpreted; rather, there are compiler or interpreter 
  [_implementations_](#glossary) of a language, and it's possible to create a compiler or interpreter for any language
* Scripting languages aren't necessarily less powerful, nor are compiled languages more difficult to work with

### *Library vs Framework vs. SDK vs. Engine vs. API*
* Using other people's code is a great time-saver, and you can often find code to use packaged as libraries, frameworks,
  SDKs, engines, or APIs
* A [_library_](#glossary) is a generic term for a collection of code made by a third party
* A library can contain functions, classes, or other pieces of code for a developer to use
* The developer doesn't need to know how the library code works; they only need to know how to call or interface with 
  the code in a library
* A [_standard library_](#glossary), such as the Python standard library, is a code library that is assumed to be 
  available to all implementations of a programming language
* A [_framework_](#glossary) is a collection of code that operates with [_inversion of control_](#glossary); the 
  developer creates functions that the framework will call as needed, as opposed to the developer's code calling 
  functions in the framework 
* Inversion control is often as, "don't call us, we'll call you"2
* A [_Software Development Kit_ (SDK)](#glossary) includes code libraries, documentation, and software tools to assist 
  in creating applications for a particular operating system or platform
  * Ex). Android SDK or iOS SDK for mobile apps for Android and iOS, or the Java Development Kit (JDK) for creating 
    applications for the Java Virtual Machine (JVM)
* An [_engine_](#glossary) is a large, self-contained system that can be externally controlled by the developer's 
  software. Developers usually call functions in an engine to perform a large, complex task
* An [_application programming interface_ (API)](#glossary) is the public-facing interface for a library, SDK, 
  framework, or engine. The API specifies how to call the functions or make requests of the library to access resources2