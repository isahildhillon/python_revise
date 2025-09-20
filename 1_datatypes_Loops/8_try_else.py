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
