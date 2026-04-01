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
* ****

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

 

