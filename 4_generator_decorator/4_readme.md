# Send value to a generator
```python
def admission_cell():
    print("Hello! Welcome to The Pathify")
    name=yield # at this line program has just printed above statement and wait for any value to come using .send function
    while True:
        print(f"{name} is granted admission to The Pathify")
        name=yield # this now again waits for new value, id dont added this will keep running loop

student = admission_cell()
next(student) # run and wait to get data (till line 3)
student.send("Sahil")
```

---

> ✅ **How to control a generator in Python** — specifically:

* Using `**yield from**` (you wrote "field from" — likely a typo),
* And how to **close** a generator properly.

Let’s explain both in a clear, copy-pasteable way.

---

## 🔹 1. `yield from` — Delegating to a Sub-generator

### ✅ What is `yield from`?

`yield from` is used when you want one generator to **delegate part of its operations to another generator**.

### 🧪 Example:

```python
def sub_generator():
    yield 1
    yield 2

def main_generator():
    yield 0
    yield from sub_generator()  # Delegates to sub_generator
    yield 3

for val in main_generator():
    print(val)

# Output:
# 0
# 1
# 2
# 3
```

### 🔍 Why use `yield from`?

* Cleaner than writing a loop like:

  ```python
  for item in sub_generator():
      yield item
  ```

---

## 🔹 2. Closing a Generator

Python generators can be **manually closed** using the `.close()` method.

### ✅ What `.close()` does:

* Stops the generator immediately.
* Raises a `GeneratorExit` inside the generator.

---

### 🧪 Example: `.close()` in Action

```python
def my_gen():
    try:
        yield 1
        yield 2
    except GeneratorExit:
        print("Generator was closed early.")

g = my_gen()
print(next(g))  # Output: 1
g.close()       # Stops the generator
# "Generator was closed early." is printed from inside
```

* After `.close()`, calling `next(g)` again will raise `StopIteration`.

---

# Decorators

A decorator is a function that: 
1. Takes another function as input
2. Adds extra behavior to it
3. And returns a new function

Think of it like "wrapping" a gift function to add something before or after it runs.

```python
# this is a decorator function decorating add
def log(func):
    def wrapper(*args, **kwargs):  # Accept any arguments
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log # set the decorator for add
def add(x, y):
    return x + y

print(add(5, 3))

# args will pass automatically to wrapper

```

Logg using decorator

```python
def log_activity(func):
    def wrapper(*args,**kwargs):
        print(f"calling function {func.__name__}")
        result=func(*args,**kwargs)
        print(f"Finished calling {func.__name__}")
        return result
    return wrapper

@log_activity
def add(x,y):
    return x+y

print(add(5,4))
```