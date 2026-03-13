# CHAPTER 04 | CHOOSING UNDERSTANDABLE NAMES

## Glossary
* **FUBAR** - fucked up beyond all repair (recognition)
* **`snake_case`** - separates words with an underscore, which looks like a flat snake in between each word
* **Constants** - a naming convention used to signal to developers that a variable's value is intended to remain 
                  unchanged throughout the program's execution
* **`camelCase`** - separates words by capitalizing the start of each word after the first, the uppercase letter looks
                    like a camel's hump
* **`PascalCase`** - named for its use in the Pascal programming language, is similar to `camelCase`, but capitalizes
                     the first word as well

## Casing Styles
* `snake_case` and `camelCase` are the most common styles  

## PEP 8's Naming Conventions

## Appropriate Name Length
* Variable names that are too short can be confusing, and too long of variable names can be tedious to type
  * Err on the side of too long

### *Too Short Names*
* A _one-or-two-letter name_ like `g` probably refers to some other word that begins with _g_, but there are many such 
  words
* Abbreviated nmes like `mon`, which could represent/stand for numerous things
* A single word name like `start` can be vague
* Dn't drp lttrs frm yr src cd

### *Too Long Names*
* In general, the larger the name's scop, the more descriptive it should be
* A short name like `payment` is fine for a local variable inside a single, short function. But `payment` might not be 
  descriptive enough if you use it for a global variable across a 10,000-line program, because such a large program 
  might process multiple kinds of payment data

#### Prefix in Names
* The use of common prefixes in names could indicate unnecessary detail in the name. If a variable is an attribute of a
  class, the prefix might provide information that doesn't need to be in the variable name
  * Ex). If you have a `Cat` class with a `weight` attribute, it's obvious that `weight` refers to the cat's weight
* _Hungarian notation_ is also unnecessary, which is the practice of using an abbreviation of the data type in names 
  * Ex). `strName`

#### Sequential Numeric Suffixes in Names
* Variable names like `payment1, payment2, payment3` don't tell the person reading the code what the difference is 
  between these payment values
  * The programmer should refactor these three variables into a single list or tuple variable named `payments` that 
    contain three values

## Make Names Searchable
* Keeping this rule in mind with naturally help you pick descriptive names instead of generic ones
* The name `email` is vague, so consider a more descriptive name like `emailAddress, downloadEmailAttachment, 
  emailMessage` or `replyToAddress`
* Not only, would such a name be more precise, it would bve easier to find in your source code files as well

## Avoid Jokes, Puns, and Cultural References

## Don't Overwrite Built-in Names
* You should never use Python's built-in (reserved) names for your own variables
  * Ex). If you name a variable `list` or `set`, you'll likely overwrite Python's `list()` and `set()` functions, 
    possibly causing bugs later in your code
  * Commonly overwritten Python names: `all, any, date, email, file, format, hash, id, input, list, min, max, object, 
    open, random, set, str, sum, test, type`
* Another common problem is naming your _.py_ files the same names as third-party modules because then you'll get an 
  error saying it doesn't exist since Python will think you're trying to import your _.py_ instead of the module

## The Worst Possible Variable Name Ever
* Ex). `data, var, temp`