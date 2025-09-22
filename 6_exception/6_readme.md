# Try Catch
```python
try:
    print(5/0)
except:
    print("Error occurred")
else: # will run if no error
    print("Run perfectlly")
finally:
    print("The task is over")
```


we can raise our own error using raise

## Custom Exception

```python
class CustomError(Exception):
    '''A Simple Custom Error'''
    pass

age=int(input("Enter Your Age : "))
if age>=18:
    print("You can vote")
else:
    raise CustomError("You can not vote")
```


# Enum
Enums  are a way to define a set of  constant values.
Absolutely — here's a **real-life example** using enums in Python that you might actually encounter in a real application:

---

### 💼 Example: Order Status in an E-commerce App

Let’s say you're building an online store. Every order can be in one of a few states:

* **Pending**
* **Shipped**
* **Delivered**
* **Cancelled**

You can represent this with an enum:

```python
from enum import Enum

class OrderStatus(Enum):
    PENDING = "Pending"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"
```

---

### ✅ How It Would Be Used

```python
def track_order(status):
    if status == OrderStatus.PENDING:
        return "Your order is being processed."
    elif status == OrderStatus.SHIPPED:
        return "Your order is on the way!"
    elif status == OrderStatus.DELIVERED:
        return "Your order has been delivered."
    elif status == OrderStatus.CANCELLED:
        return "Your order was cancelled."
    else:
        return "Unknown status."

# Usage
print(track_order(OrderStatus.SHIPPED))
```

**Output:**

```
Your order is on the way!
```

---

### 🚫 Why Not Just Use Strings?

If you used strings instead:

```python
track_order("Shipped")  # What if someone types "shipped" or "shiped"?
```

Using enums makes your code **more robust**, **less error-prone**, and easier to maintain.

---
