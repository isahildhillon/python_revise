def gen():
    try:
        yield 1 
        yield 2
    except GeneratorExit:
        print("You all ready closed the genrator")


value = gen()

print(next(value))