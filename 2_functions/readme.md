# Scopes
1. Global  → names defined at the top-level of a module/script

2. Local  → names inside a function (temporary, disappears after function ends)

3. Enclosing  → names in outer (non-global) functions (used in nested functions)

4. Built in  → The built-in scope in Python is the highest level of scope and contains all of Python’s pre-defined functions, exceptions, and constants such as print(), len(), and ValueError. These are accessible anywhere in a Python program without needing to import or declare them

```python

msg='hello' # global scope

def access_global():
    global msg
    print(msg)
    
def sum():
    a = 2 # local scope
    b =3 # local scope
    print(a+b)

def outer():
    msg="this is outer msg" # Enclosed scope for inner function
    def inner():
        nonlocal msg
        msg="This is inner"
    inner()
    print(msg)

access_global()
sum()
outer()
```

# Args (Arguments) And Kwars ( keyword Argguments)

```python
def arguments(*args,**kwargs):
    print("Args ",args)
    print("Kwargs ", kwargs)

arguments("Tea","Coffee","Juice",age="22",country="India")

# Output
# Args  ('Tea', 'Coffee', 'Juice') --> Tuple
# Kwargs  {'age': '22', 'country': 'India'} --> Dictionary
```
> we can name then anything like *drink and **info 

---

# Handle Multiple Return
if value returned is stored in one variable it is tuple or we have to use same no of variable to save data as the number of returned values
```python
def multiple_return():
    '''    This function returns multiple values''' # this is a doc string
    return "Sahil",22,"India"

name,age,country = multiple_return()
print("My Name is ", name)
print("My Age is ", age)
print("My Country is ", country)

"""Output
My Name is  Sahil
My Age is  22
My Country is  India
"""
biodata = multiple_return()
print(biodata)


# Output ('Sahil', 22, 'India')

```

---
# Pure And Impure Functions

1. ***Pure Functions*** : Which dont alter the value of global variable
1. ***Impure Functions*** : Which alters the value of global variable

```python
msg="Hello Everybody"

def view_msg():
    """This is a pure function"""
    print(msg)

def update_msg():
    """this is a impure function"""
    global msg
    msg="This is new Value"
    print(msg)

view_msg()
update_msg()
```

---
# Recurise Function
The function which calls itself

```python
def print_numbers(n):
    if n==0:
        return "Printed All Numbers"
    print(n)
    return print_numbers(n-1)

print(print_numbers(5))
```

```bash
# Output
5
4
3
2
1
Printed All Numbers

```

---

# Lambda 

A **lambda function** in Python is a small, anonymous function defined with the `lambda` keyword, which can take any number of arguments but only one expression.

### Syntax and Declaration
- The basic syntax is: `lambda arguments: expression`.
- Example:
  ```python
  square = lambda x: x * x
  print(square(5))  # Output: 25
  ```
- Lambda functions do not have names and are often used for short, simple operations.

### Lambda with Multiple Arguments
- Lambda functions can have multiple arguments, but only one expression:
  ```python
  multiply = lambda a, b: a * b
  print(multiply(5, 6))  # Output: 30
  ```
- Useful for quick, disposable logic in-place.

### Common Uses in Python
- Commonly used with higher-order functions such as `map()`, `filter()`, and `reduce()`:
  - **Map example** doubles all values in a list:
    ```python
    a = [1, 2, 3, 4]
    doubled = list(map(lambda x: x * 2, a))
    print(doubled)  # Output: [2, 4, 6, 8]
    ```
  - **Filter example** finds even numbers:
    ```python
    n = [1, 2, 3, 4, 5, 6]
    even = list(filter(lambda x: x % 2 == 0, n))
    print(even)  # Output: [2, 4, 6]
    ```
  - **Sort/Key function use**:
    ```python
    items = [(2, 'b'), (1, 'a'), (3, 'c')]
    sorted_items = sorted(items, key=lambda x: x)
    print(sorted_items)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
    ```


### When and Why to Use Lambda Functions
- Suitable for short-lived operations where defining a full function is unnecessary.
- Keeps code compact for simple tasks.
- Especially useful as arguments to functions expecting another function, such as sorting and mapping operations.

### Lambda vs Regular Function Comparison

| Aspect           | Lambda Function                            | Regular Function             |
|------------------|--------------------------------------------|------------------------------|
| Definition      | `lambda x: x+1`                            | `def add(x): return x+1`     |
| Name            | Anonymous (usually unnamed)                 | Named                        |
| Body            | Single expression only                      | Can have multiple statements |
| Use Case        | Quick, throwaway logic, as arguments        | Complex logic, reusable      |
| Readability     | Short and concise                           | More descriptive             |

Lambda functions are essential for concise, functional-style code in Python, especially in scenarios needing anonymous or inline functions.


# if `__name__ ="__main__"`

suppose we have two python file Extra.py and home.py

> Welcome.py
```python
def welcome():
    print("Hello Sahil you are welcome home")

welcome()
```

> Home.py

```python
import Extra

extra.welcome()
```

> In this case the print statement will run twice once because we called function directly in Extra and one after importing in Home TO Avoid this we will do it like below


> Welcome.py
```python
def welcome():
    print("Hello Sahil you are welcome home")

if __name__ = "__main__":
    welcome()
```

> In this way if the file is run directly without importing welcome function will call and if we call it by importing it another file It Will Not be called directly By Welcome file but it will be called by Home File So This way we can avoid it from running twice


# Ways of Imorting In Python

1. `import os` : will import all functions from os
2. `from os import mkdir` imports only specific function from package/lib

> adding `__init__.py` empty file in a folder it converts it to python package But from python 3.3 we don't need to do it anymore it is now optional.