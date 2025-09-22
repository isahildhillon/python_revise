def gen():
    try:
        yield 1 
        yield 2
    except :
        print("You all ready closed the genrator")


value = gen()
print(next(value))
# value.close() # cleans memory too
print(next(value)) # if closed early we get error