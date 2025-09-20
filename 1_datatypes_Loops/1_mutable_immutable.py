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