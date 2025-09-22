# Method resolution order
class A:
    def greet():
        print("Hello From Class A")


class B(A):
    def greet():
        print("Hello From Class B")

        
class C(A):
    def greet():
        print("Hello From Class C")

class D(B,C):
    pass

D.greet() # Hello From Class B

# if we add C first and B after that
class D(C,B):
    pass

D.greet() # Hello From Class C
# method or variable will be used from the first class which is inheritied

print(D.__mro__) # to check it