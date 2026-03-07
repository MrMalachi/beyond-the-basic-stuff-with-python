# CHAPTER 01 | DEALING WITH ERRORS & ASKING FOR HELP

## Glossary
* **Traceback (stack trace)** - shows the place in your program where the 
                              exception happened and the trail of function
                              calls that led up to it
* **Frame Summary** - the traceback's first function call, they show the
                      information inside a frame object
* **Frame Object** - hold local variables and other data associated with 
                     function calls, and are created when the function is
                     called and destroyed when the function returns
* **Linters** - lint software, or _linters_, are applications that analyze your
                source code to warn you of any potential errors
* **Static Analysis** - examining source code without running it
* **Pastebin** - stores your code at a short, public URL so you can share this
                 URL more easily than using a file attachment
* 






## How to Understand Python Error Messages
* Finding the answer to an error is a 2-step process:
  1. Examining the traceback
  2. Doing an internet search of the error message

### *Examining Tracebacks*
* Python programs crash when the code raises an exception that an `except`
  statement doesn't handle

**abcTraceback.py**
```python
def a():
    print("Start of a()")
    b() # Call b().

def b():
    print("Start of b()")
    c() # Call c().

def c():
    print("Start of c()")
    42 / 0  # This will cause a zero divided error.

a() # Call a().
```
* The `most recent call last` error text indicates that each of the function
  calls is listed in order, starting with the first function call and ending
  with the most recent

```terminaloutput
Traceback (most recent call last):
  File "/Users/djweeaboo/dev/learning/beyond_the_basic_stuff_with_python/chapters/chapter01_dealing_with_errors_asking_for_help/exercises/abcTraceback.py", line 13, in <module>              
    a() # Call a().
```
* `The <module>` text tells us this line is in the global scope
* The `print()` calls on lines 2, 6, and 10 aren't displayed in the traceback
  because only the lines containing function calls that lead up to the
  exception are displayed in the traceback

**zeroDivideTraceback.py**
```python
def spam(number1, number2):
    return number1 / (number2 - 42)

spam(101, 42)
```
* Sometimes, the traceback might indicate that an error is on the line after
  the true cause of the bug
* The traceback can indicate where things went wrong, but that isn't always
  the same as where the actual cause of a bug is

### *Searching for Error Messages*
* Search for error messages via the internet or A.I.

## Preventing Errors with Linters
* _Linters_ are applications that analyze your source code to warn you of any
  potential errors
* Although _linters_ won't catch all errors, _static analysis_ can identify 
  common errors caused by typos
* Many text editors and IDEs incorporate a linter that runs in the background 
  and can point out problems in real time
* Install a linting module called `Pyflakes`
  * `pip install --user pyflakes`

## How to Ask for Programming Help
* Avoid the following common mistakes when asking for help:
  * Asking if it’s okay to ask a question instead of just asking it
  * Implying your question instead of asking it directly 
  * Asking your question on the wrong forum or website 
  * Writing an unspecific post headline or email subject, such as “I have a
    problem” or “Please help”
  * Saying “my program doesn’t work” but not explaining how you want it
    to work 
  * Not including the full error message 
  * Not sharing your code 
  * Dealing with Errors and Asking for Help 9 
  * Sharing poorly formatted code 
  * Not explaining what you’ve already tried 
  * Not giving operating system or version information 
  * Asking someone to write a program for you

### *Limit Back and Forth by Providing Your Information Upfront*

### *State Your Question in the Forum of an Actual Question*

### *Ask Your Question on the Appropriate Website*

### *Summarize Your Question in the Headline*

### *Explain What You Want the Code to Do*

### *Include the Full Error Message*

### *Share Your Complete Code*
* _Minimal, Complete, Reproducible (MCR)_:
  * _Minimal_ - means your code example is as short as possible while still
    reproducing the problem you're encountering
  * _Complete_ - means that your code example contains everything it needs to
    reproduce the problem
  * _Reproducible_ - means that your code example reliably reproduces the
    problem you're describing

### *Make Your Code Readable with Proper Formatting*
* To ensure your code is properly formatted, copy and paste your code to a 
  _pastebin_ website, such as https://pastebin.com/ or https://gist.github.com/

### *Tell Your Helper What You've Already Tried*

### *Describe Your Setup*
* Provide your helpers the following information about your computer:
  * The operating system and version, such as "macOS Catalina"
  * The Python version running the program, such as "Python 3.7"
  * Any third-party modules your program uses and their versions, such as 
    "Django 2.1.1"
* You can find the versions of your installed third-party modules by running
  `pip list`
