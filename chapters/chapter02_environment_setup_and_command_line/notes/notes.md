# CHAPTER 02 | ENVIRONMENT SETUP AND THE COMMAND LINE

## Glossary
* **Environment Setup** - the process of organizing your computer so you can
                          write code
* **Filesystem** - how your operating system organizes data to be stored and
                   retrieved
* **Filename** - name of a file
* **Path** - specifies the location of the file on the computer
* **File Extension** - tells you a file's type
* **Folders (Directories)** - contain files and other folders
* **Root Folder (/)** - the origin of a directory 
* **POSIX** - a set of standards for Unix-like operating systems
* **Current Working Directory (cwd)** - the specific folder in the file system 
                                        where your Python script or interactive
                                        session is running at a given moment 
* **Absolute Path** - always begins with the root folder
* **Relative Path** - relative to the program's cwd
* **dot (.)** - a single period is shorthand for "this directory"
* **dot-dot (..)** - two periods means the "parent folder"
* **Program** - any software application that you can run
* **Process** - a running instance of a program 
* **Command Line** - also known as "CLI", is a text-based program that lets
                     you enter commands to interact with the operating system
                     and run programs
* **Graphic User Interface** - also known as "GUI", presents visual information
                               to a user to guide them through tasks more 
                               easily than the command line does
* **Shell Prompt** - displayed by the terminal which allows you to enter
                     commands 
* **Command Line Arguments** - bits of text you enter after the command name
                               and provide the command with specific options or
                               additional directions
* **Command Line Options** - also known as "flags", are single-letter or 
                             short-word command line arguments
* **-c flag** - this command line option allows you to run a small amount of
                throwaway Python code that you run once and then discard
* **Subprocess** - refers to a new process started by a Python program to run
                   an external command or program, such as a shell script or
                   another executable
* **Glob Patterns** - global patterns are wildcard characters that use (*) or
                      (?)
* **`ls`** - a command that displays the folders and files in the cwd
* **`-l`** - a switch (flag) displays more than what the `ls` command shows; it
             displays a long-listing format that includes file size, 
             permissions, last modification timestamps, and other information
* **`cp`** - a command used to copy by creating a duplicate
* **. (period)** - to search in the cwd
* **`mv`** - a command that moves and/or renames files and folders on macOS
             and Linux
* **`rm`** - a command on both macOS and Windows that deletes files and folders
* **Environment Variables** - often hold systemwide settings that every program would find useful. They are
                              dynamic key-value pairs stored outside an application's source code that affect how
                              running processes behave on a computer
* **echo** - a command that's primary job is to display text or variables that you pass to it as arguments. It literally
             "echoes" back whatever you type
* **`.command`** - a plain text file that contains shell commands associated with the Terminal application. When you
                   double-click a `.command` file in Finder, it automatically opens a Terminal window and executes the
                   command(s) inside it, as if you typed them manually
* **`chmod`** - the change mode command changes the permissions of a file
* **`u`** - the symbol represents a permission category meaning - user (the file owner)
* **`+`** - the symbol means - add this permission
* **`x`** - means execute permission
* ****


## The Filesystem
* A filesystem has two key properties:
  1. a _filename_
  2. a _path_ - specifies the location of a file on the computer
* Additional volumes, such as DVD drive or USB flash drive, will appear
  differently on different operating systems:
  * Windows - they appear as new, lettered root drives, such as D:\ or E:\
  * macOS - they appear as new folders within the /_Volumes_ folder
  * Linux - they appear as new folders within the /_mnt_ ("mount") folder
* Folder names and filenames are not case-sensitive on Windows and macOS, but
  they are on Linux

### *Paths in Python*
* On Windows, the backslash (\) separates folders and filenames, but on macOS
  and Linux, the forward slash (/) separates them
* Instead of writing code both ways to make your Python scripts cross-platform
  compatible, you can use the `pathlib` module and / operator instead
* The typical way yto import `pathlib`:
  * `from pathlib import Path`
* As long as the leftmost object in an expression is a `Path` object, you can
  use the / operator to join together `Path` objects or strings

```terminal
>>> from pathlib import Path
>>> Path('spam') / 'bacon' / 'eggs'

```
* PosixPath (POSIX) is a set of standards for Unix-like operating systems

### *The Home Directory*
* All users have a folder called the _home directory_ or _home folder_ for 
  their own files on the computer
* You can get a `Path` object of the home folder by calling `Path.home` after
  importing `Path` from `pathlib`

```terminaloutput
>>> from pathlib import Path
>>> Path.home()
PosixPath('/Users/djweeaboo')
```

### *The Current Working Directory*
* Every program that runs of your computer has a _current working directory_
```terminaloutput
>>> from pathlib import Path
>>> import os
>>> Path.cwd()
PosixPath('/Users/djweeaboo/dev/learning/beyond_the_basic_stuff_with_python/chapters/chapter02_environment_setup_and_command_line')
```

### *Absolute vs. Relative Paths*
* There are two ways to specify a file path:
  1. An absolute path, which always begins with the root folder
  2. A relative path, which is relative to the program's cwd
* There are also the _dot_ (.) and _dot-dot_ (..) folders, that are not real
  folders but special names you can use in a path
  * One period is shorthand for "this directory" and two periods means the 
    "parent folder"

## Programs and Processes
* A _program_ is any software application that you can run, such as a web 
  browser, spreadsheet application, or word processor
* A _process_ is a running instance of a program
  * For example: One calculator program running multiple times as multiple,
    separate processes
* _Processes_ remain separate from each other, even when running the same
  program
* macOS way of viewing a list of running processes:
  * Applications > Utilities > Activity Monitor.app

## The Command Line
* The _command line_ (CLI) is a text-based program that lets your enter 
  commands to interact with the operating system and run programs
* _Graphical User Interface_ (GUI) allows the user to interact with the 
  computer through more than just a text-based interface
* The command line program exists in an executable file on your computer. In 
  this context, we often call it a shell or shell program:
  * macOS - the shell program is at /bin/bash

### *Opening a Terminal Window*
* Simply use the Terminal.app

### *Running Programs from the Command Line*
* To run a program or command, simply enter its name into the command line:
  * Ex). `open -a Calculator`
* Program names and commands are only case-sensitive on Linux-based systems
* Entering these calculator program names into the command line is equivalent
  to running the Calculator program from the Start menu, Finder, or Dash
* The calculator program name works as a command because the _open_ program
  exist in folders that are included in the `PATH` environment variables
* To tell the command line on macOS and Linux to first check the cwd, you must
  enter "./" before the filename
* If the program isn't in a folder listed in `PATH`, you have two options:
  1. Use the `cd` command to change the cwd to the folder that contains the
     program, and then enter the program name
  2. Enter the full file path (absolute path) for the executable program file
* On Windows, if a program ends with the file extension _.exe_ or _.bat_,
  including the extension is optional: entering `calc` does the same things as
  entering `calc.exe`
* Executable programs in macOS and Linux often don't have file extensions
  marking them as executable; rather, they have the executable permissions set

### *Using Command Line Arguments*
* _Command Line Arguments_ provide the command with specific options or
  additional directions
  * Ex). When you run a Python script from a terminal window with the `python yourScript.py` 
    command, the `yourScript.py` part is an argument telling the `python`
    program what file to look in for the instructions it should carry out
* _Command Line Options_ (also called flags, switches, or simply options) are a
  single-letter or short-word command line arguments
* On Windows, command line options begin with a forward slash (/)
* On macOS and Linux, command line options (flags) begin with a single dash (-)
  or double dash (--)
* Command line options are often case-sensitive on macOS and Linux, but are
  case-insensitive on Windows
* Folders and filenames are common command line arguments, if the folder or
  filename has a space as part of its name, enclose the name in double quotes
  to avoid confusing the command line
  * Ex). If you want to change directories to a folder called _Vacation Photos_, 
    entering `cd Vacation Photos` would make the command line think you're 
    passing two different arguments, `Vacation` and `Photos`. Instead, 
    you should enter `cd "Vacation Photos"`

### *Running Python Code from the Command Line with -c*
* The `-c` command line option (flag) allows you to run a small amount of
  throwaway Python code thaat you run once and then discard
  * Ex). Enter the following into the terminal window:
    * ```terminaloutput
      (bb_venv) djweeaboo@WeebTrax-MacBook-Air chapter02_environment_setup_and_command_line % python -c "print('Hello, world')"
      Hello, world  
      ```
* The `-c` switch is handy when you want to see the results of a single
  Python instruction and don't want to waste time entering the interactive
  shell
  * Ex). You could quickly display the output of the `help()` function and then
    return to the command line:
    * ```terminaloutput
      (bb_venv) djweeaboo@WeebTrax-MacBook-Air chapter02_environment_setup_and_command_line % python -c "help(len)"
      Help on built-in function len in module builtins:
      len(obj, /)
          Return the number of items in a container.
      ```

### *Running Python Programs from the Command Line*
* Python programs are text files that have the _.py_ file extension, but
  they're NOT executable files; rather, the Python interpreter reads these
  files and carries out the Python instructions in them
* On macOS and Linux, the interpreter's executable file is _python3_
* Running the commands `python yourScript.py` or `python3 yourScript.py` will 
  run the Python instructions saved in a file named _yourScript.py_

### *Running the py.exe Program*
* On Windows, Python installs a _py.exe_ program in the _C:\Windows_ folder.
  This program is identical to _python.exe_ but accepts an additional command
  line argument that lets you run any Python version installed on your computer

### *Running Commands from a Python Program*
* Python's `subprocess.run()` function found in the `subprocess` module, can 
  run shell commands within your Python program and then present the command 
  output as a string
* For example, the following code runs the `ls -al` command:
  * ```python
    >>> import subprocess, locale
    >>> procObj = subprocess.run(['ls', '-al'], stdout=subprocess.PIPE)
    >>> outputStr = procObj.stdout.decode(locale.getdefaultlocale()[1])
    >>> print(outputStr)
    total 24
    drwxr-xr-x  6 djweeaboo  staff    192 Mar  2 09:52 .
    drwxr-xr-x  5 djweeaboo  staff    160 Feb 23 20:30 ..
    -rw-r--r--@ 1 djweeaboo  staff  10244 Mar  2 09:48 .DS_Store
    drwxr-xr-x@ 9 djweeaboo  staff    288 Mar  5 15:13 .idea
    drwxr-xr-x@ 7 djweeaboo  staff    224 Mar  2 10:01 beyond_the_basic_stuff_with_python
    drwxr-xr-x  8 djweeaboo  staff    256 Feb 23 20:22 python_crash_course
    ```
* A _subprocess_ in Python refers to a new process by a Python program to run an
  external command or program, such as a shell script or another executable
* The `subprocess` module, part of Python's standard library, provides a
  powerful and secure way to interact with the operating system at a lower
  level than older functions like `os.system`
  * But if you prefer to use the terminal, then continue using it, rather than
    using the Python console

### *Minimizing Typing with Tab Completion*
* Modern command lines offer features to minimize the amount of typing 
  necessary. The _tab completion_ feature (also called command line completion
  or autocomplete) lets a user type the first few characters of a folder or
  filename and then press the TAB key to have the shell fill in the rest of the
  name
* Tab completion is so useful, that many GUI IDEs and text editors include this
  feature as well

### *Viewing the Command History*
* In their _command history_, modern shells also remember the commands you've
  entered by pressing the up arrow key. This fills the command line with the
  last command you entered
* You can cycle through previous commands by continuing to press the up arrow
  key and also start a fresh prompt by pressing CTRL-C
* You can view the command history by running the `history` command

### *Working with Common Commands*
* This section contains a short list of the common commands you'll use in the
  command line:

#### Match Folder and Filenames with Wildcard Characters
* Many commands accept folder and filenames as command line arguments such as
  (*) and (?)
* The asterisk character matches any number of characters, whereas the question
  mark character matches any single character
* _Wildcard characters_ that use (*) and (?) are called _glob patterns_ 
  (global patterns)
* _Glob patterns_ let you specify patterns and filenames
  * Ex). You could run the `dir` or `ls` command to display all the files and
    folders in the cwd. But if you wanted to see just the Python files, 
    `dir *.py` or `ls *.py` means "any group of characters, followed by .py"
    * ```terminaloutput
      (bb_venv) djweeaboo@WeebTrax-MacBook-Air exercises % ls *.py
      abcTraceback.py         zeroDivideTraceback.py
      ```

#### Change Directories with cd
* Running `cd ~/[destination folder]` changes the shell's cwd to the destination
  folder:
  * ```terminaloutput
    (bb_venv) djweeaboo@WeebTrax-MacBook-Air exercises % cd ~/Desktop 
    (bb_venv) djweeaboo@WeebTrax-MacBook-Air Desktop %
    ```
* To change the cwd to the user's home folder, enter `cd ~` on macOS and Linux
  and `cd %USERPROFILE%` on Windows
* To change the parent directory of the cwd, use the .. folder name:
  * ```terminaloutput
    (bb_venv) djweeaboo@WeebTrax-MacBook-Air Desktop % cd ..
    (bb_venv) djweeaboo@WeebTrax-MacBook-Air ~ % 
    ```

#### List Folder Contents with dir and ls
* The `ls` command for macOS and Linux or the `dir` command on Windows displays
  the folders and files in the cwd
* You can display the the contents of another folder by running `dir 
  [another folder]` or `ls [another folder]`
* The `-l` and `-a` switches (flags) are useful arguments for the `ls` command
  * By default, `ls` displays only the names of files and folders, but to 
    display a long-listing format that includes file size, permissions, last
    modification timestamps, and other information, use `-l`
  * ```terminaloutput
    (bb_venv) djweeaboo@WeebTrax-MacBook-Air ~ % ls   
    Applications
    Desktop
    Documents
    Downloads
    Library
    Movies
    Music
    Padme's Ruminations - Revenge of the Sith [25GKkfXJUVU].mp4
    Pictures
    Public
    PycharmProjects
    dev
    (bb_venv) djweeaboo@WeebTrax-MacBook-Air ~ % ls -al
    total 27536
    drwxr-x---+  41 djweeaboo  staff      1312 Mar  5 10:11 .
    drwxr-xr-x    5 root       admin       160 Feb 23 20:47 ..
    -r--------    1 djweeaboo  staff         7 Nov  4  2024 .CFUserTextEncoding
    -rw-r--r--@   1 djweeaboo  staff     26628 Mar  5 09:58 .DS_Store
    drwx------+   2 djweeaboo  staff        64 Mar  4 18:10 .Trash
    -rw-------@   1 djweeaboo  staff      3957 Jan 29 13:19 .bash_history
    -rw-r--r--    1 djweeaboo  staff       539 Jul  9  2025 .bash_profile
    drwx------   32 djweeaboo  staff      1024 Feb  5 23:35 .bash_sessions
    -rw-r--r--    1 djweeaboo  staff       154 Feb  5 23:53 .bashrc
    drwxr-xr-x    4 djweeaboo  staff       128 Jun 11  2025 .cache
    -rw-r--r--    1 djweeaboo  staff        23 Jul  9  2025 .condarc
    drwxr-xr-x    3 djweeaboo  staff        96 Jul  9  2025 .config
    drwx------    3 djweeaboo  staff        96 Jan 23  2025 .cups
    drwxr-xr-x@  10 djweeaboo  staff       320 Feb  4  2025 .docker
    drwxr-xr-x    4 djweeaboo  staff       128 Jul 16  2025 .ipynb_checkpoints
    drwxr-xr-x    3 djweeaboo  staff        96 Jul  9  2025 .ipython
    drwxr-xr-x    4 djweeaboo  staff       128 Jul 16  2025 .jupyter
    -rw-------@   1 djweeaboo  staff        20 Mar  5 10:11 .lesshst
    drwxr-xr-x    5 djweeaboo  staff       160 May 12  2025 .local
    drwxr-xr-x    3 djweeaboo  staff        96 Jun 11  2025 .matplotlib
    drwxr-xr-x@   4 djweeaboo  staff       128 Jul  7  2025 .mcode
    -rw-------@   1 djweeaboo  staff       492 Mar  5 15:17 .python_history
    -rw-r--r--    1 djweeaboo  staff       281 Jul  9  2025 .tcshrc
    -rw-------    1 djweeaboo  staff      9306 Jun 11  2025 .viminfo
    -rw-r--r--    1 djweeaboo  staff       635 Jul  9  2025 .xonshrc
    -rw-r--r--    1 djweeaboo  staff        83 Jun 11  2025 .zprofile
    -rw-------@   1 djweeaboo  staff     17698 Mar  4 17:09 .zsh_history
    drwx------   41 djweeaboo  staff      1312 Mar  5 10:00 .zsh_sessions
    -rw-r--r--@   1 djweeaboo  staff       200 Mar  2 10:06 .zshrc
    drwx------@   4 djweeaboo  staff       128 Dec  5  2024 Applications
    drwx------@   4 djweeaboo  staff       128 Feb 23 20:15 Desktop
    drwx------@   9 djweeaboo  staff       288 Mar  4 16:48 Documents
    drwx------+ 205 djweeaboo  staff      6560 Mar  2 09:23 Downloads
    drwx------@  99 djweeaboo  staff      3168 Jan 28 17:53 Library
    drwx------    8 djweeaboo  staff       256 Nov  8 08:41 Movies
    drwx------+  13 djweeaboo  staff       416 Jan 27 20:31 Music
    -rw-r--r--@   1 djweeaboo  staff  13989393 Mar  9  2025 Padme's Ruminations - Revenge of the Sith [25GKkfXJUVU].mp4
    drwx------+   6 djweeaboo  staff       192 Jun 12  2025 Pictures
    drwxr-xr-x+   4 djweeaboo  staff       128 Nov  4  2024 Public
    drwxr-xr-x@   5 djweeaboo  staff       160 Jul  9  2025 PycharmProjects
    drwxr-xr-x    5 djweeaboo  staff       160 Feb 23 20:30 dev
    ```

#### List Subfolder Contents with dir /s and find
* On macOS, the `find . -name` command displays the cwd's folders and their
  subfolders
  * Ex). ```python
         (bb_venv) djweeaboo@WeebTrax-MacBook-Air chapter02_variables_data % find . -name "*.py"     
         ./Exercises/hello.py
        ./Exercises/famous_quote.py
        ./Exercises/personal_message.py
        ./Exercises/full_name.py
        ./Exercises/apostrophe.py
        ./Exercises/name_cases.py
        ./Exercises/favorite_number.py
        ./Exercises/stripping_names.py
        ./Exercises/simple_message.py
        ./Exercises/number_eight.py
        ./Exercises/simple_messages.py
        ./Exercises/name.py
        ./Exercises/file_extensions.py
         ```
* The . (period) tells `find` to start searching in the cwd. The `-name` option
  tells `find` to find folders and filenames by name. The `"*.py"` tells `find`
  to display folders and files with name that match the `*.py` pattern
  * Note that the `find` command requires the argument after `-name` to be
    enclosed in double quotes

#### Copy Files and Folders with copy and cp
* To create a duplicate of a file or folder in a different directory, run
  `cp [source file or folder] [destination folder]`
  * Ex). ```terminaloutput
    (bb_venv) djweeaboo@WeebTrax-MacBook-Air Exercises % ls
    apostrophe.py           full_name.py            number_eight.py         some_sub_folder
    famous_quote.py         hello.py                personal_message.py     stripping_names.py
    favorite_number.py      name.py                 simple_message.py
    file_extensions.py      name_cases.py           simple_messages.py
    (bb_venv) djweeaboo@WeebTrax-MacBook-Air Exercises % cp apostrophe.py some_sub_folder 
    (bb_venv) djweeaboo@WeebTrax-MacBook-Air Exercises % cd some_sub_folder 
    (bb_venv) djweeaboo@WeebTrax-MacBook-Air some_sub_folder % ls
    apostrophe.py
        ```

#### Move Files and Folders with move and mv
* On macOS, you can move a source file or folder to a destination folder by
  running `mv [source file or folder] [destination file or folder]`
* On Windows, `move [source file or folder] [destination file or folder]` does
  the same thing
  * ```terminaloutput
    al@ubuntu:~/someFolder$ ls
    hello.py someSubFolder
    al@ubuntu:~/someFolder$ mv hello.py someSubFolder
    al@ubuntu:~/someFolder$ ls
    someSubFolder
    al@ubuntu:~/someFolder$ cd someSubFolder/
    al@ubuntu:~/someFolder/someSubFolder$ ls
    hello.py
    ```

#### Rename Files and Folders with ren and mv
* Running `mv [file or folder] [new name]` renames the file or folder on macOS
  and Linux, while running `ren [file or folder] [new name]` does the same on
  Windows
* Note that you can use the `mv` command on macOS and Linux for moving _and_
  renaming a file:
  * Ex). ```terminaloutput
    al@ubuntu:~/someFolder$ ls
    hello.py someSubFolder
    32 Chapter 2
    al@ubuntu:~/someFolder$ mv hello.py goodbye.py
    al@ubuntu:~/someFolder$ ls
    goodbye.py someSubFolder
         ```
* The `hello.py` file now has the name `goodbye.py`.

#### Delete Files and Folders with del anf rm
* To delete a file or folder on macOS or Linux, run `rm [file]` (`rm`) is short
  for, remove. To do the same on Windows, run `del [file or folder]`
* On macOS and Linux, you CANNOT use the `rm` command to delete folders. But
  you can run `-rm -r [folder]` to delete a folder and all of its contents

#### Make folders with md and mkdir
* On macOS and Linux, running `mkdir [new folder]` creates a new, empty folder. 
  On Windows, running `md [new folder]` does the same

#### Delete Folders with rd anf rmdir
* Running `rmdir [source folder]` deletes the source folder on macOS and Linux, 
  while running `rd [source folder]` on Windows does the same
* Note, the folder must be empty before you can remove it
  * Ex). ```
        (bb_venv) djweeaboo@WeebTrax-MacBook-Air python_crash_course % rmdir random 
        rmdir: random: Directory not empty`
        ```

#### Find Programs with where and which
* Running `which [program]` on macOS and Linux, or `where [program]` on Windows
  , tells the exact location of the program
* When you enter a command on the command line, your computer checks for the
  program in the folders listed in the `PATH` environment variable
* These commands can tell you which executable Python program is run when you enter `python` in the shell, but if you have multiple Python versions installed, your computer might have several executable programs of the same name
  * The one that is run depends on the order of folders in your `PATH` environment variable, and the `where` and `which` commands will output it
    * Ex). 
      ```terminaloutput
      (bb_venv) djweeaboo@WeebTrax-MacBook-Air python_crash_course % where python
      /Users/djweeaboo/dev/learning/beyond_the_basic_stuff_with_python/bb_venv/bin/python
      ```

#### Clear the Terminal with cls and clear
* Running `clear` on macOS and Linux, or `cls` on Windows, will clear all the
  text in the terminal window
* This is useful if you want to start with a fresh-looking terminal window

## Environment Variables and PATH
* This is an operating system (OS) concept. All running processes of a program, no matter the language in which it's 
  written, have a set of variables called _environment variables_ that can store a string
  * Ex). The `TEMP` environment variable folds the file path where any program can store temporary files
* When the operating system runs a program (such as the command line), the newly created process receives its own copy
  of the operating system's environment variables and values
* Note, you can change a process's environment variables, but those changes apply only to the process, not the operating
  system or any other process

### *Viewing Environment Variables*
* You can see a list of the terminal window's environment variables by running `env` on macOS and Linux or `set` on
  Windows
```terminaloutput
COMMAND_MODE=unix2003
SHELL=/bin/zsh
TMPDIR=/var/folders/ty/39slb6ns1tnb5xk7mcrjc4nh0000gn/T/
__CFBundleIdentifier=com.jetbrains.pycharm
HOME=/Users/malachibrown
SSH_AUTH_SOCK=/private/tmp/com.apple.launchd.VH9MOCoAFx/Listeners
XPC_SERVICE_NAME=0
PATH=/opt/homebrew/bin:/opt/homebrew/sbin:/Library/Frameworks/Python.framework/Versions/3.12/bin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin:/opt/pmk/env/global/bin:/Applications/PyCharm.app/Contents/MacOS
LOGNAME=malachibrown
USER=malachibrown
```
* The text on the left side of the equal sign (=) is the environment variable name, and the text on the right side is
  the string value
* You can also view the value of a single environment variable with the `echo` command
```terminaloutput
malachibrown@Malachis-iMac notes % echo $HOME
/Users/malachibrown
```
* You can think of the operating system's set of environment variables as the "master copy" from which a process copies
  its environment variables

### *Working with the PATH Environment Variable*
* When you enter a command, like `python3` on macOS and Linux, the terminal checks for a program with that name in the
  folder you're currently in. If it doesn't find it there, it will check the folders listed in the `PATH`
  environment variable
* Because environment variables can contain only a single string value, adding multiple folder names to the `PATH`
  environment variable requires using a special format:
  * On macOS and Linux, colons separate the folder name
```terminaloutput
malachibrown@Malachis-iMac notes % echo $PATH
/opt/homebrew/bin:/opt/homebrew/sbin:/Library/Frameworks/Python.framework/Versions/3.12/bin:/usr/local/bin:/System
/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr
/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd
/codex.system/bootstrap/usr/appleinternal/bin:/opt/pmk/env/global/bin:/Applications/PyCharm.app/Contents/MacOS
```
* The order of the folder names is important because if you have two files with the same filename, the program will run
  in the order that the folder appears first in the `PATH` environment variable

### *Changing the Command Line's PATH Environment Variable*
* You can change the current terminal window's `PATH` environment variable to include additional folders
* To temporarily add folders to `PATH` on macOS and Linux for testing, you can run:
```terminaloutput
malachibrown@Malachis-iMac notes % PATH=/new_folder:$PATH
malachibrown@Malachis-iMac notes % echo $PATH
/new_folder:/opt/homebrew/bin:/opt/homebrew/sbin:/Library/Frameworks/Python.framework/Versions/3.12/bin:/usr/local/bin...
```
* The `$PATH` part expands to the current value of the `PATH` environment variable, so you're adding to the new folder
  and a colon to the existing `PATH` value
* This method for adding folders to `PATH` apply only to the current terminal window and any programs run from it after
  the addition. If you open a new terminal window, it won't have your changes
* Permanently adding folders requires changing the operating system's set of environment variables

### *Permanently Adding Folders to PATH on macOS*
* To add folders to the `PATH` environment variables for all terminal windows on macOS and Linux, you'll need to modify
  the _.zshrc_ text file in your home folder and add the following lines:
```terminaloutput
export PATH=/newFolder:$PATH
```
* This line modifies `PATH` for all future terminal windows

## Running Python Programs Without the Command Line
* Windows has the Start menu, macOS has the Finder and Dock, and Ubuntu Linux has Dash
* Rather than running a _.py_ file by double-clicking, which will run the file from the Python Interactive Shell, or 
  running a _.py_ file from an IDE or command-line, you can instead set up your Python programs to easily run them from
  your operating system's launcher, just like other applications you've installed

### *Running Python Programs on macOS*
* On macOS, you can create a shell script to run you Python scripts by creating a text file with the _.command_ file
  extension: 

**Step 1 - Create & Save a launcher shell script using the `.command` file extension**
```text
touch ~/run_script.command
open -e ~/run_script.command

#!/usr/bin/env zsh
python3 /Users/malachibrown/path/to/test_script.py
```

**Step 2 - Make the launcher executable**
```text
chmod u+x run_script.command
```
* The full command above means - give the file owner permission to execute the file as a program
* Without execute permission, macOS treats the file like text, so double-clicking would either:
  * open the file in a text editor
  * or refuse to run it
* Adding `x` tells the system:
  * This file is allowed to run like a program

