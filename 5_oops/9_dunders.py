class Number:
        # initialize
    def __init__(self, value):
        self.value = value

    # add
    def __add__(self, other):
        return Number((self.value + other.value)*1.18) # Say we have to add 18% Gst
    
    # equal
    def __eq__(self, other): 
        return self.value == other.value

a = Number(5)
b = Number(10)
c = a + b
print(c.value)       # 15
print(a == 5)        # False
