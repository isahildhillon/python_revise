# File Handling

Python file handling allows you to create, read, write, and delete files. Here’s a concise overview with examples:

---

### 📁 **Basic File Modes**

| Mode  | Description                        |
| ----- | ---------------------------------- |
| `'r'` | Read (default). File must exist.   |
| `'w'` | Write. Creates/overwrites file.    |
| `'a'` | Append. Creates if not exist.      |
| `'x'` | Create. Fails if file exists.      |
| `'b'` | Binary mode (e.g., `'rb'`, `'wb'`) |
| `'t'` | Text mode (default)                |

---

### 📖 **Reading Files**

```python
# Open and read a file
with open('example.txt', 'r') as f:
    content = f.read()
    print(content)
```

```python
# Read line by line
with open('example.txt', 'r') as f:
    for line in f:
        print(line.strip())
```

---

### ✍️ **Writing to Files**

```python
# Write (overwrites file)
with open('example.txt', 'w') as f:
    f.write("Hello, world!\n")
```

```python
# Append to file
with open('example.txt', 'a') as f:
    f.write("More content...\n")
```

---

### ✅ **Check if File Exists**

```python
import os

if os.path.exists('example.txt'):
    print("File exists.")
else:
    print("File does not exist.")
```

---

### ❌ **Delete a File**

```python
import os

os.remove('example.txt')
```

---

### 📋 **Other Useful Methods**

```python
f.read(size)     # Reads specified number of characters
f.readline()     # Reads one line
f.readlines()    # Returns list of all lines
f.write(text)    # Writes string to file
f.seek(0)  # set pointer to be at 0th position
```

---
