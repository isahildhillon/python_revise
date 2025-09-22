class MyClass:
    value = 10  # Class attribute

# Create an instance
obj = MyClass()

# Access class attribute
print(obj.value)  # Output: 10

# Shadow the class attribute by defining an instance attribute with the same name
obj.value = 20

# Now it uses the instance attribute
print(obj.value)  # Output: 20

# The class attribute is still 10
print(MyClass.value)  # Output: 10

del obj.value
print(obj.value) # print 10
