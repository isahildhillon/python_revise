# Bytes - Immutable
data = b'hello'
print(data)
print(type(data))

# Output
#b'hello'
# <class 'bytes'>


# Byte Array - Mutable
data1= bytearray([65,66,67])
print(data1)
# Output : bytearray(b'ABC')

# MEmory View
mv= memoryview(data)
s=mv[2:4]
print(s.tobytes())