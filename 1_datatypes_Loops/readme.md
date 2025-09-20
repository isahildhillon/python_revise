## Objects

In python everything is object

**Object**  Has identity , type and value

***Mutable*** That can be Changed
***ImMutable*** That can't be Changed , variable can be changed to point at something different but if pointing at same its value will not change

```python 

a = 10
print("a id:", id(a))

a += 5  # changing value of a
print("a id after change:", id(a))  # different id → new object

# Immutable Example: string
s = "hello"
print("\ns id:", id(s))

s += " world"
print("s id after change:", id(s))  # new id → new object

lst = [1, 2, 3]
print("\nlst id:", id(lst))

lst.append(4)  # modify in place
print("lst id after append:", id(lst))  # same id → same object
```

```bash
# Output
a id: 140718482945224
a id after change: 140718482945384

s id: 2508076283296
s id after change: 2508076407152


lst id: 2895371001856
lst id after append: 2895371001856

```

* Immutable objects → new identity when changed (because now variable points to other object)
* Mutable objects → same identity when changed



> Always check the imutability by identity not value



# 🐍 Python Data Types

Python has several **built-in data types** which are categorized into **mutable** and **immutable**.

---

## 🔹 1. Numeric Types

* **int** → integers (whole numbers, unlimited precision)
* **float** → decimal numbers (floating-point)
* **complex** → complex numbers with real and imaginary parts

```python
x = 10          # int
y = 3.14        # float
z = 2 + 3j      # complex
```

✅ **Immutable** – changing their value creates a new object.

---

## 🔹 2. Sequence Types

### a) **List**

* Ordered, mutable, allows duplicates
* Defined with `[]`

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")  # modifies in place
```

✅ **Mutable**

---

### b) **Tuple**

* Ordered, immutable, allows duplicates
* Defined with `()`

```python
coordinates = (10, 20, 30)
```

✅ **Immutable**

---

### c) **Range**

* Immutable sequence of numbers (often used in loops)

```python
nums = range(1, 10, 2)  # start, stop, step
```

✅ **Immutable**

---

## 🔹 3. Text Type

### **String (str)**

* Ordered, immutable, sequence of Unicode characters
* Defined with quotes `" "` or `' '`

```python
s = "Hello"
```

✅ **Immutable**

---

## 🔹 4. Set Types

### a) **Set**

* Unordered, mutable, no duplicates
* Defined with `{}` or `set()`

```python
s = {1, 2, 3, 3}
# s → {1, 2, 3}
```

✅ **Mutable**

---

### b) **Frozen Set**

* Unordered, immutable version of a set
* Defined with `frozenset()`

```python
fs = frozenset([1, 2, 3])
```

✅ **Immutable**

---

## 🔹 5. Mapping Type

### **Dictionary (dict)**

* Unordered, mutable, key-value pairs
* Keys must be immutable, values can be anything

```python
person = {"name": "Alice", "age": 25}
person["age"] = 26
```

✅ **Mutable**

---

## 🔹 6. Boolean Type

* Represents truth values: `True` or `False`
* Internally stored as integers (`1` and `0`)

```python
flag = True
```

✅ **Immutable**

---

## 🔹 7. None Type

* Represents the absence of a value
* Only one instance: `None`

```python
x = None
```

✅ **Immutable**

---

## 🔹 8. Binary Types

* **bytes** → Immutable sequence of bytes
* **bytearray** → Mutable sequence of bytes
* **memoryview** → Memory-efficient view of binary data

```python
b = b"hello"                  # bytes
ba = bytearray([65, 66, 67])  # bytearray
mv = memoryview(b)            # memoryview
```

---

## ✅ Summary Table

| Category | Type                | Mutable?    |
| -------- | ------------------- | ----------- |
| Numeric  | int, float, complex | ❌ Immutable |
| Sequence | list                | ✅ Mutable   |
|          | tuple               | ❌ Immutable |
|          | range               | ❌ Immutable |
| Text     | str                 | ❌ Immutable |
| Set      | set                 | ✅ Mutable   |
|          | frozenset           | ❌ Immutable |
| Mapping  | dict                | ✅ Mutable   |
| Boolean  | bool                | ❌ Immutable |
| None     | NoneType            | ❌ Immutable |
| Binary   | bytes               | ❌ Immutable |
|          | bytearray           | ✅ Mutable   |
|          | memoryview          | ✅ Mutable   |

---


> Bytes
```python
b = b"hello"
print("Bytes:", b)
print("First element:", b[0])     

```

> Bytes Aray
```python
# bytearray: mutable version of bytes
ba = bytearray([65, 66, 67])   # ASCII for 'A', 'B', 'C'
print("Bytearray:", ba)
print("As string:", ba.decode())

# Modify in place
ba[0] = 90   # Change 'A' (65) to 'Z' (90)
print("Modified Bytearray:", ba)
print("As string after change:", ba.decode())

```


>***Memoryview*** so means slicing makes copy but if we use memory view it wont make  copy

```python
data = bytearray(b"abcdef")
# Normal slice (copy)
s = data[5:10]
print(s)         # bytearray(b'fghij')

mv = memoryview(data)
sub = mv[2:5]    # memoryview slice (no copy)
print(sub.tobytes())   # b'cde'
```


### What is a Byte?

A byte is the smallest addressable unit of memory in a computer.

It is 8 bits (1 byte = 8 binary digits).

Each bit is 0 or 1, so a byte can represent values from 0 → 255.

---

# 🔹String What is Encoding & Decoding?

* **Encoding** → Converting a **string (`str`)** into **bytes (`bytes`)** using a specific character encoding (like UTF-8, ASCII).
* **Decoding** → Converting **bytes (`bytes`)** back into a **string (`str`)**.

👉 Strings (`str`) in Python are sequences of **Unicode characters** (human-readable).
👉 Bytes (`bytes`) are raw **binary data** (machine-readable).

---

# 🔹 Example: Encoding

```python
text = "Hello 🌍"             # String (Unicode)
encoded = text.encode("utf-8")  # Encode into bytes
print(encoded)                  # b'Hello \xf0\x9f\x8c\x8d'
```

✅ `"🌍"` is stored in multiple bytes (`\xf0\x9f\x8c\x8d`) when encoded in UTF-8.

---

# 🔹 Example: Decoding

```python
decoded = encoded.decode("utf-8")  # Decode bytes back to string
print(decoded)                     # "Hello 🌍"
```

✅ Now we’re back to a proper `str`.

---

# 🔹 Encoding Errors

Sometimes a character can’t be represented in the chosen encoding (e.g., ASCII doesn’t support 🌍).
You can control what happens:

```python
text = "Hello 🌍"

# ASCII can't encode 🌍
encoded = text.encode("ascii", errors="ignore")   # remove invalid
print(encoded)   # b'Hello '

encoded = text.encode("ascii", errors="replace")  # replace with '?'
print(encoded)   # b'Hello ?'

encoded = text.encode("ascii", errors="xmlcharrefreplace")
print(encoded)   # b'Hello &#127757;'
```

---

# 🔹 Common Encodings

* **UTF-8** → Standard, supports all characters, variable-length (1–4 bytes).
* **ASCII** → Limited to 128 characters (English only).
* **UTF-16 / UTF-32** → Use 2 or 4 bytes per character, bigger files but fixed width.

---

# 🔹 Real-World Example: File I/O

```python
# Write as encoded bytes
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Hello 🌍")

# Read and decode automatically
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)   # "Hello 🌍"
```

👉 Python handles encoding/decoding automatically if you specify `encoding`.

---

# ✅ Summary

| Operation | Python Method    | Example                 |
| --------- | ---------------- | ----------------------- |
| Encode    | `str.encode()`   | `"Hi".encode("utf-8")`  |
| Decode    | `bytes.decode()` | `b"Hi".decode("utf-8")` |

* **Encoding** → `str → bytes`
* **Decoding** → `bytes → str`

---
> we encode so computer can understand and decode so we can understand
---


## Topics Name I dont need notes
1. Lists
2. Operator Overloading
3. set and frozen set
4. Dictonary
5. Conditionals ( If , If else , if elif else )

> There are some advance collections not used majorly  can be searhched them about online ( so ignored)

### short hand if else

```python
n=9
result= "Pass" if n>10 else "Fail"
```
---

## Loops

1. For Loop
```python
for i in range(1,5):
    print(i)

```
we can use enumarate() to get index , value both

```python
sweets=['Rasgulla','Ladoo','Ras Malai']
for index,value in enumerate(sweets):
    print(index,value)

# Output
# 0 Rasgulla
# 1 Ladoo
# 2 Ras Malai
```
> ***zip*** to run loop on more than one list once
```python
sweets=['Rasgulla','Ladoo','Ras Malai']
persons =['Sahil','Ram','Ankit']
for sweet,person in zip(sweets,persons):
    print(f"{person} Bought {sweet}")
    
```


2. while
```python
cups_of_coffee=5
while cups_of_coffee >0:
    print("i got one coffee")
    cups_of_coffee-=1
```


* break : to end loop
* continue : to skin current iteration



> Python For Else loop fallback only run if loop dont break
```python
nums = [1, 3, 5, 7]

for n in nums:
    if n % 2 == 0:
        print("Found even:", n)
        break
else:
    print("No even number found (fallback)")

```


## Python Else Usage

1. For Else ( saw above)
2. While Else :
Same rule: else runs if the loop finishes without break

```python
n = 3
while n > 0:
    print(n)
    n -= 1
else:
    print("Loop finished without break")
```

3. Try Except Else :
Only run if no exception
```python
try:
    x = int("123")
except ValueError:
    print("Conversion failed")
else:
    print("Conversion successful:", x)

# Output : Conversion successful: 123

try:
    x = int("Sahil")
except ValueError:
    print("Conversion failed")
else:
    print("Conversion successful:", x)
# Output : Conversion failed



# with finally
try:
    f = open("file.txt", "r")
except FileNotFoundError:
    print("File not found")
else:
    print("File opened successfully")
    f.close()
finally:
    print("Always runs")


```




## Walrus Operator(:=)
It assigns a value to a variable and returns it in the same expression.


```python 
# without walrus
line = input("Enter: ")
while line != "quit":
    print(f"You entered: {line}")
    line = input("Enter: ")

```
```python 
# with walrus 
while (line := input("Enter: ")) != "quit":
    print(f"You entered: {line}")

```