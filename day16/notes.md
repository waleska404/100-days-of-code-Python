* Procedural programming: one that directly instructs a device on how to finish a task in logical steps. This paradigm uses a linear top-down approach and treats data and procedures as two different entities. Based on the concept of a procedure call, Procedural Programming divides the program into procedures, which are also known as routines or functions, simply containing a series of steps to be carried out.

Simply put, Procedural Programming involves writing down a list of instructions to tell the computer what it should do step-by-step to finish the task at hand.


* Packages VS. Modules:

## What are Python Modules?
A module is a pythonic statement which contains multiple functions in it. Modules act as a pre-defined library in the code, which is accessible to both coder and user.

The python modules also store pre-defined functions from the library while the execution of code is going on.

Example of Python Module:
```
import math
from math import pow
pow(2,8)
print(pow)
Output:

<built-in function pow>
>>>
```
## What are Python Packages?
A package is the form of a collection of tools which helps in the initiation of the code. A python package acts as a user-variable interface for any source code. This makes a python package work at a defined time for any functionable code in the runtime.

Example of Python Package:
```
import math
print("math package")
Output:

math package
>>>
```
## Differences Between Python Modules and Packages
1. A package holds the file __init__.py for every user-oriented code. But this does not apply to modules in runtime for any user-specific codes.
2. A module is a file containing Python code in run time for a user-specific code. A package also modifies the user interpreted code in such a way that it gets easily functioned in the run time.

A python “module” consists of a unit namespace, with the locally extracted variables. And some parsed functions as:

* Constants and variables
* Class definitions of properties
* Really any old value or new one.
* A module usually corresponds to a single file.
* A debugging tool in the user interface library.
* There are a few generally used tools that help the coder build a new platform using the modules for a good execution of codes. This installs and distributes packages all over the library in runtime also.

Using a well structured and standard layout for the package makes it easy to employ user-specific tools. It also simplifies the executions in runtime.

## What actually makes a Python Package different from Modules?
This is a generally asked question, what makes a python package different from a module. A python package works on a library, defining the codes as a single unit of any particular function. While the modules are a separate library themselves, which have inbuilt functions. The reusability of packages makes it more preferable over modules.

### Explicit Namespaces
This provides the default namespace in the code, which is processed for the first time. These namespaces act as a source code in the identification of the code. A new coder can, however, import them from the library as well. But it is always advisable to know the general namespaces for the proper execution of the code.
```
def thisistech():
    a='Greetings!'
thisistech()
Output:

>>> thisistech
<function thisistech at 0x030BFCD0>
>>>
```
### Convenience API
This is basically a method to namespace certain objects within the code. It gets the user to the core of the code and hence easily identifies the errors also. This also helps in parsing the codes in such a way that they may act as a user interface code in the runtime.
```
import hello
hello.hey()
'Hey, there!'
Output:

Error
```
